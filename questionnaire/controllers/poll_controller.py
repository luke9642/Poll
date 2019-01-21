from django.db import transaction

from questionnaire.controllers.question_types_registry import Registry
from questionnaire.models import Poll, Question, PollAnswers


class PollController:
    def __init__(self, poll_hash):
        self.poll = Poll.objects.get_hash(poll_hash)

    @staticmethod
    @transaction.atomic
    def create_poll(name, author, questions):
        poll = Poll.objects.create(author=author, name=name)

        for question in questions:
            question_model = Question.objects.create(
                poll=poll,
                question_text=question["question_name"],
                question_type=question["question_type"],
                required=question["question_required"]
            )

            Registry.choice_cls(question["question_type"]).objects.create(
                question=question_model,
                question_choice=question["question_choice"]
            )

        return poll

    @transaction.atomic
    def add_answer(self, data):
        poll_answers = PollAnswers.objects.create(poll=self.poll)

        for question in self.poll.questions.all():
            if data.get(question.question_text, None):
                value = data[question.question_text]
                Registry.answer_cls(question.question_type).objects.create(
                    poll_answers=poll_answers, question=question, answer_type=question.question_type, value=value)

    @staticmethod
    def get_author_polls(author):
        return Poll.objects.filter(author=author)

    def get_all_answers(self):
        return self.poll.answers.all()

    def get_all_questions(self):
        return self.poll.questions.all()

    @transaction.atomic
    def delete_poll(self):
        self.poll.delete()
