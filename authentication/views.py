from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


def register_user(request):
    my_login = True
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm(request.POST)
    return render(request, "register.html", context={"form": form,
                                                     "login": my_login})


def login_user(request):
    my_login = True
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Try again")
            return render(request, "login.html", context={"login": my_login})
    else:
        return render(request, "login.html", context={"login": my_login})


def logout_user(request):
    logout(request)
    return redirect('/')
