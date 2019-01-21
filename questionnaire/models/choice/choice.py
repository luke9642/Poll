from django.db import models, transaction

from questionnaire.models.question import Question
from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel


class ChoiceManager(models.Manager):
    @transaction.atomic
    def create(self, *, question, question_choice):
        return super().create(question=question, choice=question_choice)


class Choice(IterFieldsValuesModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = ChoiceManager()

    class Meta:
        abstract = True
