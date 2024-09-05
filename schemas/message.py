from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class MessageRead(BaseModel):
    uuid: UUID
    created_at: datetime
    user_uuid: UUID
    data: str


class MessageCreate(BaseModel):
    data: str
