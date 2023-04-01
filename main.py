import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from Bard import Chatbot

app = FastAPI()


class Message(BaseModel):
    session_id: str
    message: str


@app.post("/ask")
async def ask(request: Request, message: Message) -> dict:
    auth_key = os.getenv('AUTH_KEY')
    if not auth_key:
        raise HTTPException(status_code=401, detail='Authorization key is missing')

    if auth_key != request.headers.get('Authorization'):
        raise HTTPException(status_code=401, detail='Invalid authorization key')

    chatbot = Chatbot(message.session_id)
    response = chatbot.ask(message.message)
    return response