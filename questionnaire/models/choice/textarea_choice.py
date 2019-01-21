from django.db import models

from questionnaire.models.choice import Choice


class TextareaChoice(Choice):
    choice = models.TextField()
