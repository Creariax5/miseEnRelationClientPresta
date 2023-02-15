from django.urls import path

from .views import *

urlpatterns = [
    path('', pay_eth),
    path('paypal/<int:usd>/<str:address>/', paypal),
    path('eth/<int:eth>/<str:address>/<str:key>/<str:email>/', eth),
    path('complete_sell/<str:nb>/<str:value>/', complete_sell),
    path('complete_buy/<str:nb>/<str:value>/', complete_buy),
    path('compal/', paypal_success, name="compal"),
]
