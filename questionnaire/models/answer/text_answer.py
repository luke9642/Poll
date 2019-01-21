from django.db import models

from questionnaire.models.answer.answer import Answer


class TextAnswer(Answer):
    value = models.CharField(max_length=200)