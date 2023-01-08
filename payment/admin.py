from django.contrib import admin
from .models import Product, Order, ProductAdmin, OrderAdmin

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

