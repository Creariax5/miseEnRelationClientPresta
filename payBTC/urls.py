from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', pay_eth),
    path('paypal/<int:usd>/<str:address>/', paypal),
    path('eth/<int:eth>/<str:address>/<str:key>/<str:email>/', eth),
    path('compal/', compal, name="compal"),
]
