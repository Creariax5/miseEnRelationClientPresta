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
        return render(request, "index.html", context={"admin": admin,
                                                      "profiles": profiles,
                                                      "id": my_id,
                                                      "user": current_user,
                                                      "profile": profile})
    else:
        return render(request, "index.html")
