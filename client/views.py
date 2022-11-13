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
    return render(request, "indexClient.html", context={"date": date,
                                                        "modeFormat": modeFormat,
                                                        "form": form,
                                                        "dataStudents": Students.objects.all()})


def demande(request):
    return render(request, "demande.html")


def my_demande(request):
    return render(request, "my_demande.html")