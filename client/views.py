import requests
import json
from django.shortcuts import render, redirect
from _datetime import datetime
from .formulaire import Students_from, Students
import sys

sys.path[:0] = ['../']
from authentication.models import Profile
from payment.models import Product


def indexClient(request):
    if request.method == "POST":
        form = Students_from(request.POST).save()
        return redirect('/client')
    else:
        form = Students_from
    modeFormat = "client"
    date = datetime.today()

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

    return render(request, "indexClient.html", context={"date": date,
                                                        "modeFormat": modeFormat,
                                                        "form": form,
                                                        "Students": Students.objects.all(),
                                                        "response": my_list})


def backpack(request):
    product = Product.objects.all()
    current_user = request.user
    my_objects = []
    if current_user.is_authenticated:
        profile = Profile.objects.filter(user=current_user)
        for pr in profile:
            my_objects = pr.my_objects
        for x in range(len(my_objects)):
            my_objects = my_objects.replace("[", "")
            my_objects = my_objects.replace("]", "")
        my_objects = list(my_objects.split(", "))
        print(my_objects)

    return render(request, "backpack.html", context={"product": product,
                                                     "my_objects": my_objects,
                                                     "profile": profile})


def demande(request):
    return render(request, "demande.html")


def my_demande(request):
    return render(request, "my_demande.html")
