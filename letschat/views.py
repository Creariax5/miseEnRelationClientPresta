from django.shortcuts import render
from .models import LastRoom


def letschat(request):
    return render(request, 'chat_room.html')


def room(request, my_room):
    r = LastRoom(room_name=my_room)
    r.save()
    username = request.user.username
    room_details = my_room
    return render(request, 'chat.html', {
        'username': username,
        'room': my_room,
        'room_details': room_details
    })
