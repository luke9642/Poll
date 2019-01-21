from django.db import models

from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel
from questionnaire.models.poll import Poll


class Question(IterFieldsValuesModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200)
    required = models.BooleanField()

    @property
    def question_types(self):
        return {
            "Linear Scale": "rangechoice_set",
            "Long Answer": "textareachoice_set",
            "Short Answer": "textchoice_set",
            "Single Choice": "singlechoice_set"
        }

    @property
    def choice(self):
        return next(choice for choice in getattr(self, self.question_types[self.question_type]).all())
