import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = f"chat_{self.chat_id}"
        self.user = self.scope["user"]

        # подключаемся к группе чата
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):

        data = json.loads(text_data)
        message = data.get("message")
        user = self.scope["user"]

        if not message:
            return

        chat = await self.save_message(user.id, message)

        # 🔥 сообщение в чат (REALTIME)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": user.username
            }
        )

        # 🔥 определяем получателя
        if chat.buyer_id == user.id:
            receiver_id = chat.seller_id
        else:
            receiver_id = chat.buyer_id

        # ❌ не отправляем уведомление самому себе
        if receiver_id == user.id:
            return

        # 🔥 уведомление
        await self.channel_layer.group_send(
            f"user_{receiver_id}",
            {
                "type": "send_notification",
                "count": 1,
                "chat_id": self.chat_id
            }
        )


    async def chat_message(self, event):

        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"]
        }))


    @database_sync_to_async
    def save_message(self, user_id, message):

        msg = Message.objects.create(
            chat_id=self.chat_id,
            sender_id=user_id,
            text=message
        )

        return msg.chat