from django.db import models
from django.contrib import admin


class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    rarity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
