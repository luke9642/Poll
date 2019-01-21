import hashlib

from django.contrib.auth import get_user_model
from django.db import models

from questionnaire.models.iter_fields_values_model import IterFieldsValuesModel


class PollManager(models.Manager):
    def get_hash(self, poll_hash):
        return next(poll for poll in super().all() if poll.hash == poll_hash)


class Poll(IterFieldsValuesModel):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    objects = PollManager()

    @property
    def hash(self):
        h = hashlib.sha3_256()
        h.update(str(self.pk).encode())
        h.update(str(self.name).encode())
        h.update(str(self.pub_date).encode())
        return h.hexdigest()

    @property
    def number_of_questions(self):
        return len(self.questions.all())
