from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', pay_btc),

    path('admin/', admin.site.urls),
]
