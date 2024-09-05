import socketio

from fastapi import FastAPI

from routers.user import router as user_router
from routers.message import router as message_router

from socket_manager import sio

app = FastAPI()


@app.get('/healtz', tags=['system'])
async def get_healtz():
    return 'healthy'


@app.get('/readyz', tags=['system'])
async def get_readyz():
    return 'ready'


@app.get('/publication/ready', tags=['system'])
async def get_publication_ready():
    return 'ready'


app.include_router(user_router, prefix='/rest/v1')
app.include_router(message_router, prefix='/rest/v1')

app = socketio.ASGIApp(sio, app)


@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)


@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)
