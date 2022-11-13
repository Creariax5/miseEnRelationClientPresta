from django.urls import path
from .views import *

urlpatterns = [
    path('', indexClient),
    path('demande/', demande),
    path('my_demande/', my_demande),
]
