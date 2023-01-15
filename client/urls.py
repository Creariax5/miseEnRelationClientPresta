from django.urls import path
from .views import *

urlpatterns = [
    path('', indexClient),
    path('backpack/', backpack),
    path('demande/', demande),
    path('my_demande/', my_demande),
]
