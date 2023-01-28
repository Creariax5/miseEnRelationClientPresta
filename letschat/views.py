from django.shortcuts import render, redirect


def letschat(request):
    return render(request, 'chat_room.html')


def room(request, room):
    username = request.user.username
    room_details = room
    return render(request, 'chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
