from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index),
    path('nav/', navbar),
    path('', include("authentication.urls")),
    path('', include("django.contrib.auth.urls")),
    path('client/', include("client.urls")),
    path('graph/', include("graph.urls")),
    path('payment/', include("payment.urls")),
    path('chat/', include("letschat.urls")),
    path('trade/', include("trade.urls")),
    path('games/', include("games.urls")),
    path('pay_btc/', include("payBTC.urls")),

    path('split/', split),

    path('admin/', admin.site.urls),
]
