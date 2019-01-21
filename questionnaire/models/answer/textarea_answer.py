from django.db import models

from questionnaire.models.answer.answer import Answer


class TextareaAnswer(Answer):
    value = models.TextField()
