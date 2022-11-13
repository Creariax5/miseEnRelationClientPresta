from django.db import models
from django.contrib import admin


class user(models.Model):
    pseudo = models.CharField(max_length=25)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    phoneNumber = models.IntegerField(max_length=25)
    birthday = models.DateField()


class userAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'firstName', 'lastName', 'email', 'phoneNumber', 'birthday')
    list_filter = ('pseudo', 'firstName', 'lastName', 'birthday')
    search_fields = ('name', 'firstName', 'lastName')
