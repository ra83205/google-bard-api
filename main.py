import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from Bard import Chatbot
import urllib.parse
import json

app = FastAPI()

''' Add Origin

origins = [
    "http://localhost:Port"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''

class Message(BaseModel):
    session_id: str
    message: str


@app.post("/ask")
async def ask(request: Request, message: Message) -> dict:
    # Get the user-defined auth key from the environment variables
    user_auth_key = os.getenv('USER_AUTH_KEY')
    
    # Check if the user has defined an auth key,
    # If so, check if the auth key in the header matches it.
    if user_auth_key and user_auth_key != request.headers.get('Authorization'):
        raise HTTPException(status_code=401, detail='Invalid authorization key')

    # Execute your code without authenticating the resource
    chatbot = Chatbot(message.session_id)
    response = chatbot.ask(message.message)

    # print(response['choices'][0]['content'][0])
    return response

# @app.post("/v1/chat/completions")
@app.post("/bard")
async def ask(request: Request, message: Message) -> dict:
    # Get the user-defined auth key from the environment variables
    user_auth_key = os.getenv('USER_AUTH_KEY')
    
    # Check if the user has defined an auth key,
    # If so, check if the auth key in the header matches it.
    if user_auth_key and user_auth_key != request.headers.get('Authorization'):
        raise HTTPException(status_code=401, detail='Invalid authorization key')

    # Execute your code without authenticating the resource
    # chatbot = Chatbot(message.session_id)
    chatbot = Chatbot(os.getenv("SESSION_ID"))
    response = chatbot.ask_bard(message.message)
    # print(response)

    # print(response["choices"][0]["message"]["content"])
    return response
