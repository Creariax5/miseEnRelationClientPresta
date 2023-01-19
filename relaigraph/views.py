from django.shortcuts import render
import sys

sys.path[:0] = ['../']
from authentication.models import Profile


def index(request):
    current_user = request.user
    if current_user.is_authenticated:
        my_id = request.user.id
        admin = False
        if current_user.username == 'admin':
            admin = True
        profiles = Profile.objects.all()
        profile = Profile.objects.filter(user=current_user)
        if 'money' in request.POST:
            for pr in profiles:
                if pr.user.username == current_user.username:
                    pr.money += 10
                    pr.save()
                    print("add", current_user.username)
        elif 'give_all' in request.POST:
            for pr in profiles:
                pr.money += 10
                pr.save()
                print("add", current_user.username)
        if admin:
            return render(request, "admin.html", context={"admin": admin,
                                                          "profiles": profiles,
                                                          "id": my_id,
                                                          "user": current_user,
                                                          "profile": profile})
        else:
            return render(request, "admin.html", context={"admin": admin,
                                                          "profiles": profiles,
                                                          "id": my_id,
                                                          "user": current_user,
                                                          "profile": profile})

    else:
        return render(request, "index.html")


def navbar(request):
    return render(request, "navbar.html")


def split(request):
    return render(request, "split.html")
