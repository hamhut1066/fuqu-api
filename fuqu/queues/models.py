from django.conf import settings
from django.db import models


class Queue(models.Model):
    place = models.TextField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    day = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    minutes = models.IntegerField() # The number of minutes the user queued
    seconds = models.IntegerField() # The number of seconds the user queued