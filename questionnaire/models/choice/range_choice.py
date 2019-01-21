from django.db import models, transaction

from questionnaire.models.choice import Choice, ChoiceManager


class RangeChoiceManager(ChoiceManager):
    @transaction.atomic
    def create(self, *, question, question_choice):
        return super(ChoiceManager, self).create(
            question=question,
            min_choice=question_choice["value_min"],
            max_choice=question_choice["value_max"],
        )


class RangeChoice(Choice):
    min_choice = models.IntegerField()
    max_choice = models.IntegerField()

    objects = RangeChoiceManager()

    @property
    def boundaries(self):
        return self.min_choice, self.max_choice

    @property
    def range(self):
        return range(self.min_choice, self.max_choice+1)
