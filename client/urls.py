from django.urls import path
from .views import *

urlpatterns = [
    path('', pokedex),
    path('backpack/', backpack),
    path('demande/', demande),
    path('my_pokemons/', my_pokemons),
]
