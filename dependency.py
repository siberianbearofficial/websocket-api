from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from config import USERS
from repositories.message import MessageRepository
from schemas.user import UserRead
from services.message import MessageService

security = HTTPBasic()

message_repository = MessageRepository()
message_service = MessageService(message_repository)


async def get_authenticated_user(credentials: HTTPBasicCredentials = Depends(security)) -> UserRead:
    for user in USERS:
        if user.get('username') == credentials.username and user.get('password') == credentials.password:
            return UserRead(
                uuid=user.get('uuid'),
                username=user.get('username')
            )

    raise HTTPException(status_code=401, detail="Incorrect username or password")


async def get_message_service():
    return message_service


MessageServiceDep = Annotated[MessageService, Depends(get_message_service)]
AuthenticatedUserDep = Annotated[UserRead, Depends(get_authenticated_user)]
