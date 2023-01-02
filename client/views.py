import requests
import json
from django.shortcuts import render, redirect
from _datetime import datetime
from .formulaire import Students_from, Students


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
    while i != 906:
        my_list.append(aDict[str(i)]['name'])
        i += 1

    return render(request, "indexClient.html", context={"date": date,
                                                        "modeFormat": modeFormat,
                                                        "form": form,
                                                        "dataStudents": Students.objects.all(),
                                                        "response": my_list})


def demande(request):
    return render(request, "demande.html")


def my_demande(request):
    return render(request, "my_demande.html")
