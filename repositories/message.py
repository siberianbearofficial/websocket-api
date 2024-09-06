import json
from os.path import exists
from uuid import UUID

from models.message import Message


class MessageRepository:
    def __init__(self):
        self.__messages = []

    async def get_messages(self) -> list[Message]:
        return list(map(Message.from_dict, self.__messages))

    async def get_message(self, uuid: UUID) -> Message:
        messages = await self.get_messages()
        return list(filter(lambda message: message.uuid == uuid, messages))[0]

    async def add_message(self, message: Message):
        self.__messages.append(message.to_dict())
