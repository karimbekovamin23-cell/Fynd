import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
            return

        self.group_name = f"user_{user.id}"

        print("JOIN GROUP:", self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

async def disconnect(self, close_code):

    if hasattr(self, "group_name"):

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        print("DISCONNECT:", self.group_name)

    else:
        print("DISCONNECT WITHOUT GROUP")

    async def send_notification(self, event):

        print("SEND TO CLIENT:", event)

        await self.send(text_data=json.dumps({
            "count": event.get("count", 1),
            "chat_id": event.get("chat_id")
        }))