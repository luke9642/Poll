import json

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from questionnaire.controllers import question_types_registry
from questionnaire.controllers.poll_controller import PollController
from questionnaire.models import Poll


class CreateNewPollTest(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='temporary', password='temporary')
        self.client = Client()

    def test_redirect_user_to_login_page(self):
        response = self.client.post(reverse('poll_create'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/user/login?next=/poll/new/")

    def test_poll_creation(self):
        self.client.login(username='temporary', password='temporary')

        response = self.client.post(
            reverse('poll_create'),
            data=json.dumps({"title": "title1", "poll": []}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Poll.objects.all().count(), 1)
        self.assertEqual(Poll.objects.get().author.username, 'temporary')

    def test_user_creation(self):
        user = get_user_model().objects.get()

        self.assertEqual(user.username, 'temporary')


class PollControllerTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username='temporary', password='temporary')

        questions = [
            {
                "question_name": "question1",
                "question_type": "Linear Scale",
                "question_required": True,
                "question_choice": {
                    "value_min": 2,
                    "value_max": 7
                }
            },
            {
                "question_name": "question2",
                "question_type": "Long Answer",
                "question_required": False,
                "question_choice": {
                    "value": "lorem ipsum"
                }
            }
        ]

        poll = PollController.create_poll(author=user, name='poll1', questions=questions)
        self.poll_controller = PollController(poll.hash)

    def test_questions_length(self):
        questions = self.poll_controller.get_all_questions()

        self.assertEqual(questions.count(), 2)

    def test_questions_text(self):
        questions = self.poll_controller.get_all_questions()

        texts = ["question1", "question2"]

        for question, text in zip(questions, texts):
            with self.subTest(question=question, text=text):
                self.assertEqual(question.question_text, text)

    def test_questions_required(self):
        questions = self.poll_controller.get_all_questions()
        required = [True, False]

        for question, req in zip(questions, required):
            with self.subTest(question=question, req=req):
                self.assertEqual(question.required, req)


class QuestionTypesRegistryTest(TestCase):
    def setUp(self):
        self.linear_data = {
            "question_type": "Linear Scale",
            "question_choice": {
                "value_min": 2,
                "value_max": 7
            }
        }

        self.long_answer_data = {
            "question_type": "Long Answer",
            "question_choice": {
                "value": "lorem ipsum"
            }
        }

    def test_single_choice(self):
        self.assertEqual(
            question_types_registry.Registry.choice_cls("Single Choice"),
            question_types_registry.SingleChoice)

        self.assertEqual(
            question_types_registry.Registry.answer_cls("Single Choice"),
            question_types_registry.SingleAnswer)

    def test_linear_scale(self):
        self.assertEqual(
            question_types_registry.Registry.choice_cls("Linear Scale"),
            question_types_registry.RangeChoice)

        self.assertEqual(
            question_types_registry.Registry.answer_cls("Linear Scale"),
            question_types_registry.RangeAnswer)

    def test_short_text(self):
        self.assertEqual(
            question_types_registry.Registry.choice_cls("Long Answer"),
            question_types_registry.TextareaChoice)

        self.assertEqual(
            question_types_registry.Registry.answer_cls("Long Answer"),
            question_types_registry.TextareaAnswer)

    def test_long_answer(self):
        self.assertEqual(
            question_types_registry.Registry.choice_cls("Short Answer"),
            question_types_registry.TextChoice)

        self.assertEqual(
            question_types_registry.Registry.answer_cls("Short Answer"),
            question_types_registry.TextAnswer)