from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse, JsonResponse


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


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    messages = Message.objects.filter(room=room)
    print(list(messages.values()))
    return JsonResponse({"messages": list(messages.values())})
