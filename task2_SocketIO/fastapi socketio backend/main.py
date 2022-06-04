import socketio
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = FastAPI()
socketio_app = socketio.ASGIApp(sio, app)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

#normal http requests

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/v2")
async def read_main():
    return {"message": "FastAPI is Nice"}


# socketio options

@sio.event
async def connect(sid, environ):
    print("connect ", sid)


@sio.on('message')
async def chat_message(sid, data):
    today = str(datetime.today().strftime('%Y-%m-%d'))
    print("message ", data)
    await sio.emit('response', 'Your message is  : ' + data + '  , You are still connected, Today is : ' + today)


@sio.event
async def disconnect(sid):
    print('disconnect ', sid)


