from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(null=True, blank=True)
    img = models.CharField(max_length=200)
    category = models.CharField(max_length=20, default="none")
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField(Product, max_length=20)
    buyer = models.CharField(User, max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'display')
    list_filter = ('category', 'price')
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'created')
    list_filter = ('product', 'buyer', 'created')
    search_fields = ('name', 'buyer')
