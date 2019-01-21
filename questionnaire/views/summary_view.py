from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from questionnaire.controllers.poll_controller import PollController


class SummaryView(LoginRequiredMixin, ListView):
    template_name = "questionnaire/summary.html"
    context_object_name = "questions"

    def get_queryset(self):
        questions = PollController(poll_hash=self.kwargs["poll_hash"]).get_all_questions()
        result = [self._get_question_data(question) for question in questions]
        return {"questions": result}

    def _get_question_data(self, question):
        answers = self._get_answers_data(question)

        result = {
            "id": question.id,
            "type": question.question_type,
            "question": question.question_text,
            "answers": answers
        }

        if question.question_type == "Linear Scale":
            result["labels"] = list(question.choice.range)
        elif question.question_type == "Single Choice":
            result["labels"] = list(answers.keys())

        return result

    def _get_answers_data(self, question):
        from itertools import groupby

        if question.question_type == "Single Choice":
            return {answer.choice: len(list(group)) for answer, group in groupby(question.answer_set.all())}
        elif question.question_type == "Linear Scale":
            choices = sorted(answer.choice for answer in question.answer_set.all())

            return {choice: len(list(group)) for choice, group in groupby(choices)}
        else:
            return [answer.choice for answer in question.answer_set.all() if not answer.empty]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = PollController(poll_hash=self.kwargs["poll_hash"]).poll
        return context
