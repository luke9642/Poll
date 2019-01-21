from django.db import models

from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel
from questionnaire.models.poll import Poll


class PollAnswers(IterFieldsValuesModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="answers")
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)
