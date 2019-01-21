from django.db import models

from questionnaire.models.answer.answer import Answer


class RangeAnswer(Answer):
    value = models.IntegerField()
