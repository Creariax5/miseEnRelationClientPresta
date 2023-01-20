from django.urls import path

from .views import *

urlpatterns = [
    path('', trade),
    path('room/<int:nb>', room),
]
