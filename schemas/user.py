from uuid import UUID

from pydantic import BaseModel


class UserRead(BaseModel):
    uuid: UUID
    username: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserWithPassword(BaseModel):
    uuid: UUID
    username: str
    password: str
