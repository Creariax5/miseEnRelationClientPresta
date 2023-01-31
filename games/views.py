from django.shortcuts import render


def games(request):
    return render(request, "games.html")


def chess(request):
    return render(request, "chess.html")
