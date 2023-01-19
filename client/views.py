import requests
import json
from django.shortcuts import render, redirect
from _datetime import datetime
import sys
from .give_object import object_str_to_list, object_list_to_context

sys.path[:0] = ['../']
from authentication.models import Profile
from payment.models import Product


def pokedex(request):
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_names.json"

    headers = {
        "X-RapidAPI-Key": "2791ff7022mshc7cf931913ff7d6p16c6eejsna69458bab2e5",
        "X-RapidAPI-Host": "pokemon-go1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    pks = response.text
    aDict = json.loads(pks)
    my_list = []
    i = 1
    while i != 722:
        my_low = aDict[str(i)]['name'].lower()
        my_list.append(my_low)
        i += 1

    return render(request, "pokedex.html", context={"response": my_list})


def backpack(request):
    open_obj = False
    product = Product.objects.all()
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)

    my_objects = object_str_to_list(profile, current_user)
    product_list = object_list_to_context(product, my_objects)

    if request.method == "POST":
        claim = "0"
        claim = request.POST['this_id']
        if claim == "1":
            return render(request, "backpack.html", context={"product_list": product_list,
                                                             "my_objects": my_objects,
                                                             "profile": profile})

    if request.method == "POST":
        this_id = request.POST['this_id']
        open_obj = True
        return render(request, "backpack.html", context={"product_list": product_list,
                                                         "my_objects": my_objects,
                                                         "profile": profile,
                                                         "this_id": this_id,
                                                         "open_obj": open_obj})

    return render(request, "backpack.html", context={"product_list": product_list,
                                                     "my_objects": my_objects,
                                                     "profile": profile})


def demande(request):
    return render(request, "demande.html")


def my_pokemons(request):
    return render(request, "my_pokemons.html")
