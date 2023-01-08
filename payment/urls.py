from django.urls import path
from .views import *

urlpatterns = [
    path('pay/<int:pk>', pay),
    path('complete/', paymentComplete, name="complete"),
    path('', store),
]
