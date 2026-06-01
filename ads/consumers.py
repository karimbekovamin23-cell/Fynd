import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group = f"chat_{self.chat_id}"
        self.user = self.scope["user"]

        if self.user.is_anonymous:
            await self.close()
            return

        await self.channel_layer.group_add(self.room_group, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "room_group"):
            await self.channel_layer.group_discard(self.room_group, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        text = (data.get("message") or "").strip()
        if not text:
            return

        user = self.user
        msg_time, receiver_id = await self.save_message(user.id, text)

        await self.channel_layer.group_send(
            self.room_group,
            {
                "type": "chat_message",
                "message": text,
                "username": user.username,
                "time": msg_time,
            },
        )

        if receiver_id and receiver_id != user.id:
            await self.channel_layer.group_send(
                f"user_{receiver_id}",
                {"type": "send_notification", "count": 1, "chat_id": self.chat_id},
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
            "time": event.get("time", ""),
        }))

    @database_sync_to_async
    def save_message(self, user_id, text):
        from .models import Chat, Message
        msg = Message.objects.create(
            chat_id=self.chat_id,
            sender_id=user_id,
            text=text,
        )
        chat = Chat.objects.only("buyer_id", "seller_id").get(pk=self.chat_id)
        receiver_id = chat.seller_id if chat.buyer_id == user_id else chat.buyer_id
        return msg.created_at.strftime("%H:%M"), receiver_id
