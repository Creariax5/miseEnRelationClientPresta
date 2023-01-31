import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "1"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        pkm_id = text_data_json['pkm_id']
        user = text_data_json['user']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'pkm_id': pkm_id,
                'user': user
            }
        )

    def chat_message(self, event):
        pkm_id = event['pkm_id']
        user = event['user']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'pkm_id': pkm_id,
            'user': user
        }))
