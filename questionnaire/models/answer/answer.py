from django.db import models

from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel
from questionnaire.models.question import Question
from questionnaire.models.answer.poll_answers import PollAnswers


class Answer(IterFieldsValuesModel):
    poll_answers = models.ForeignKey(PollAnswers, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_type = models.CharField(max_length=200)

    @property
    def answer_types(self):
        return {
            "Short Answer": "textanswer",
            "Long Answer": "textareaanswer",
            "Linear Scale": "rangeanswer",
            "Single Choice": "singleanswer"
        }

    @property
    def choice(self):
        return getattr(self, self.answer_types[self.answer_type]).value

    @property
    def empty(self):
        return not bool(getattr(self, self.answer_types[self.answer_type]).value)
