from channels.generic.websocket import AsyncJsonWebsocketConsumer


class StatusConsumer(AsyncJsonWebsocketConsumer):
    room_group_name = 'notify'

    async def connect(self):
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print('in connect')
        await self.accept()

    async def disconnect(self, code):
        print('in disconnect-before')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )
        print('in disconnect-after')

    async def status_notifier(self, event):
        await self.send_json(event)
