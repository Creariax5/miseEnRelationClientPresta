from datetime import datetime
from django.shortcuts import render


def indexGraph(request):
    modeFormat = "graphiste"
    date = datetime.today()
    return render(request, "indexGraph.html", context={"date": date,
                                                       "modeFormat": modeFormat})


def work(request):
    return render(request, "work.html")


def my_work(request):
    return render(request, "my_work.html")
