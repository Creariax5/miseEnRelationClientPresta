from django.shortcuts import render


def store(request):
    return render(request, "store.html")


def pay(request):
    return render(request, "pay.html")
