from django.db import models


class IterFieldsValuesModel(models.Model):
    def __iter__(self):
        for field_name in self._meta.fields:
            value = getattr(self, field_name.name)
            yield (field_name.name, value)

    class Meta:
        abstract = True
