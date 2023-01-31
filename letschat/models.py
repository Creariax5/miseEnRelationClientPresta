from django.db import models
from datetime import datetime


# Create your models here.
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    last = models.IntegerField(default=0)


class LastRoom(models.Model):
    room_name = models.CharField(max_length=1000000)
