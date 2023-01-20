from django.shortcuts import render


def letschat(request):
    return render(request, 'chat_room.html')


def room_name(request, name):
    return render(request, 'chat.html', {'room_name': name})

