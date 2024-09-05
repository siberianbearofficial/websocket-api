import json
from os.path import exists
from uuid import UUID

from models.message import Message


class MessageRepository:
    def __init__(self, filename: str):
        self.__filename = filename

        if not exists(filename):
            with open(filename, 'w') as message_file:
                json.dump([], message_file)

    async def get_messages(self) -> list[Message]:
        with open(self.__filename, 'r') as message_file:
            return list(map(Message.from_dict, json.load(message_file)))

    async def get_message(self, uuid: UUID) -> Message:
        messages = await self.get_messages()
        return list(filter(lambda message: message.uuid == uuid, messages))[0]

    async def add_message(self, message: Message):
        messages = await self.get_messages()
        messages.append(message.to_dict())
        with open(self.__filename, 'w') as message_file:
            json.dump(messages, message_file)
