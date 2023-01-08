from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.CharField(Product, max_length=20)
    buyer = models.CharField(User, max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price')
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'buyer', 'created')
    list_filter = ('product', 'buyer', 'created')
    search_fields = ('name', 'buyer')
