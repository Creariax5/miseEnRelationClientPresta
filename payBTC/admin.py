from django.contrib import admin
from .models import Trade, TradeAdmin

# Register your models here.
admin.site.register(Trade, TradeAdmin)
