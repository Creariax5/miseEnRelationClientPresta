import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import LastRoom


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        room = (LastRoom.objects.last()).room_name
        self.room_group_name = room

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    def chat_message(self, event):
        message = event['message']
        user = event['user']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user
        }))
