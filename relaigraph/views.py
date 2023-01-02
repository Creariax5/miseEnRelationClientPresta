from django.shortcuts import render


def index(request):
    current_user = request.user
    admin = False
    if current_user.username == 'admin':
        admin = True
    my_id = current_user.id
    return render(request, "index.html", context={"admin": admin,
                                                  "id": my_id})
