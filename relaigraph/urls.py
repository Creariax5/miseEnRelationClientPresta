from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index),
    path('', include("authentication.urls")),
    path('', include("django.contrib.auth.urls")),

    path('client/', include("client.urls")),
    path('client/', include("client.urls")),
    path('client/', include("client.urls")),

    path('graph/', include("graph.urls")),
    path('graph/', include("graph.urls")),
    path('graph/', include("graph.urls")),

    path('payment/', include("payment.urls")),

    path('admin/', admin.site.urls),
]
