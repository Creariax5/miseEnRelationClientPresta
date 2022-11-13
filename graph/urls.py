from django.urls import path
from .views import *

urlpatterns = [
    path('work/', work),
    path('my_work/', my_work),
    path('', indexGraph),
]
