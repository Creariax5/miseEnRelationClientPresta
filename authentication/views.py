from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .form import user


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def deconnection(request):
    pass
