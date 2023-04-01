from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
from Bard import Chatbot

app = FastAPI()


class Message(BaseModel):
    session_id: str
    message: str


@app.post("/ask")
async def ask(request: Request, message: Message) -> dict:
    chatbot = Chatbot(message.session_id)
    response = chatbot.ask(message.message)
    return response
