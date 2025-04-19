from django.db import models


class BaseManager(models.Manager):
    class Meta:
        abstract = True
        app_label = 'aula'
