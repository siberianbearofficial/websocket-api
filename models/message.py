from datetime import datetime
from uuid import UUID


class Message:
    def __init__(self, uuid: UUID, user_uuid: UUID, data: str, created_at: datetime):
        self.uuid = uuid
        self.user_uuid = user_uuid
        self.data = data
        self.created_at = created_at

    def to_dict(self):
        return {
            'uuid': str(self.uuid),
            'created_at': datetime.isoformat(self.created_at),
            'user_uuid': str(self.user_uuid),
            'data': self.data
        }

    @staticmethod
    def from_dict(message_dict: dict) -> 'Message':
        return Message(
            uuid=UUID(message_dict['uuid']),
            user_uuid=UUID(message_dict['user_uuid']),
            data=message_dict['data'],
            created_at=datetime.fromisoformat(message_dict['created_at'])
        )
