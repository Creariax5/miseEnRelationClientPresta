from django.urls import path
from .views import *

app_name = 'letschat_app'
urlpatterns = [
    path('chatroom/', letschat),
    path('<str:room>/', room),
]
