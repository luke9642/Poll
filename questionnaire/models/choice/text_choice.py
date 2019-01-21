from django.db import models

from questionnaire.models.choice import Choice


class TextChoice(Choice):
    choice = models.CharField(max_length=200)
