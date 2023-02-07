from django.db import models
from django.contrib import admin


class Trade(models.Model):
    nb = models.CharField(default="0", max_length=20)
    buyer = models.CharField(default="none", max_length=20)
    buy_usd = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nb


class TradeAdmin(admin.ModelAdmin):
    list_display = ('nb', 'buyer', 'created', 'buy_usd')
    list_filter = ('nb', 'buyer', 'created')
    search_fields = ('nb', 'buyer')
