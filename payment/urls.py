from django.urls import path
from .views import *

urlpatterns = [
    path('pay/<int:pk>/<int:nb>', pay),
    path('complete/', paymentComplete, name="complete"),
    path('', store),
]
