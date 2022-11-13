from django.db import models
from django.contrib import admin


class Students(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('name',)
