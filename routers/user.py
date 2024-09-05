from uuid import uuid4

from fastapi import APIRouter

from config import USERS
from schemas.user import UserCreate

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/')
async def post_users(user: UserCreate):
    USERS.append({
        'uuid': uuid4(),
        'username': user.username,
        'password': user.password
    })
