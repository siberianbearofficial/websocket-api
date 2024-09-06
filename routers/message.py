from uuid import UUID

from fastapi import APIRouter, HTTPException

from dependency import MessageServiceDep, AuthenticatedUserDep
from schemas.message import MessageCreate

router = APIRouter(prefix='/messages', tags=['messages'])


@router.get('')
async def get_messages_handler(
        message_service: MessageServiceDep
):
    messages = await message_service.get_messages()

    return {
        'data': messages,
        'detail': 'Messages were selected.'
    }


@router.get('{uuid}')
async def get_message_handler(
        message_service: MessageServiceDep,
        uuid: UUID
):
    message = await message_service.get_message(uuid)
    if message is None:
        raise HTTPException(status_code=404, detail='Message not found.')

    return {
        'data': message,
        'detail': 'Message was selected.'
    }


@router.post('')
async def post_messages_handler(
        message_service: MessageServiceDep,
        message: MessageCreate,
        author: AuthenticatedUserDep
):
    message_uuid = await message_service.create_message(author.uuid, message)

    return {
        'data': str(message_uuid),
        'detail': 'Message was added.'
    }
