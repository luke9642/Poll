from django.db import models, transaction

from questionnaire.models.choice import ChoiceManager, Choice
from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel


class SingleChoiceManager(ChoiceManager):
    @transaction.atomic
    def create(self, *, question, question_choice):
        choice_base = super(ChoiceManager, self).create(question=question)

        for option in question_choice:
            Option.objects.create(choice=choice_base, text=option)

        return choice_base


class SingleChoice(Choice):
    objects = SingleChoiceManager()


class Option(IterFieldsValuesModel):
    choice = models.ForeignKey(SingleChoice, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=200)
