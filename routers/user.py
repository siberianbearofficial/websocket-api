from uuid import uuid4, UUID

from fastapi import APIRouter, HTTPException

from config import USERS
from schemas.user import UserCreate, UserRead
from socket_manager import sio

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
async def get_users():
    return {
        'data': list(map(lambda user_dict: UserRead(**user_dict), USERS)),
        'detail': 'Users were selected.'
    }


@router.get('/{uuid}')
async def get_user(uuid: UUID):
    users = list(filter(lambda user: user.get('uuid') == str(uuid), USERS))
    if not users:
        raise HTTPException(status_code=404, detail='User not found.')

    return {
        'data': UserRead(**users[0]),
        'detail': 'User was selected.'
    }


@router.post('/')
async def post_users(user: UserCreate):
    user_uuid = uuid4()
    USERS.append({
        'uuid': user_uuid,
        'username': user.username,
        'password': user.password
    })

    await sio.emit('user_added', {"data": str(user_uuid)})
    return {
        'data': str(user_uuid),
        'detail': 'User was added.'
    }
