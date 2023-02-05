from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', pay_btc),
    path('paypal/<int:usd>', paypal),

    path('admin/', admin.site.urls),
]
