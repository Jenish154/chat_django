import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatUser, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.username = self.scope['user']
        self.room_group_name = f"chat_{self.username}"
        self.user = await sync_to_async(ChatUser.objects.get)(username=self.username)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    def construct_message(self, messages):
        msg = {}
        for i in messages:
            msg['type'] = 'message'
            msg['content'] = i.content
            msg['sender'] = i.sender
            msg['created_at'] = i.created_at
        return msg

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        print(text_data_json, "this is the message \n\n\n")
        message = text_data_json['content']
        group_name = text_data_json['reciever']
        sender = await sync_to_async(ChatUser.objects.get)(username=text_data_json['sender'])
        reciever = await sync_to_async(ChatUser.objects.get)(username=group_name)
        print('sender is: ', sender, 'reciever is: ', reciever)
        if sender and reciever:
            new_msg = await sync_to_async(Message.objects.create)(sender=sender, reciever=reciever, content=text_data_json['content'])

            dt_str = new_msg.created_at.strftime('%Y-%m-%dT%H:%M:%S')
            json_str = json.dumps(dt_str)
            await self.channel_layer.group_send('chat_' + group_name, {
                'type': 'message',
                'content': message,
                'sender': sender.username,
                'reciever': reciever.username,
                'created_at': json_str,
            })
            await sync_to_async(new_msg.save)()

    async def message(self, event):
        print('event is: ', event)
        message = event['content']
        await self.send(text_data=json.dumps({'content': message, 'sender': event['sender'], 'reciever': event['reciever'], 'created_at': event['created_at']}))