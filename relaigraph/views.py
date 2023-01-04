from django.shortcuts import render
import sys
sys.path[:0] = ['../']
from authentication.models import Profile


def index(request):
    current_user = request.user
    admin = False
    if current_user.username == 'admin':
        admin = True
    my_follows = Profile.user
    my_id = current_user.id
    return render(request, "index.html", context={"admin": admin,
                                                  "id": my_id,
                                                  "follows": my_follows})
