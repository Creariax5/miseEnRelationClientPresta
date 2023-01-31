from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', games),
    path('chess/', chess),
]
