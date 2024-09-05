from datetime import datetime
from uuid import UUID, uuid4

from models.message import Message
from repositories.message import MessageRepository
from schemas.message import MessageCreate, MessageRead
from socket_manager import sio


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    async def get_messages(self) -> list[MessageRead]:
        messages = await self.message_repository.get_messages()
        return list(map(self.__model_to_schema, messages))

    async def get_message(self, uuid: UUID) -> MessageRead:
        message = await self.message_repository.get_message(uuid)
        return self.__model_to_schema(message)

    async def create_message(self, user_uuid: UUID, message: MessageCreate) -> UUID:
        message_uuid = uuid4()
        message_model = Message(
            uuid=message_uuid,
            user_uuid=user_uuid,
            data=message.data,
            created_at=datetime.now(tz=None)
        )

        await self.message_repository.add_message(message_model)
        await sio.emit("message_added", {"data": str(message_uuid)})
        return message_uuid

    @staticmethod
    def __model_to_schema(model: Message) -> MessageRead:
        return MessageRead(
            uuid=model.uuid,
            user_uuid=model.user_uuid,
            data=model.data,
            created_at=model.created_at
        )
