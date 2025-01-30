import chainlit as cl
import requests
import uuid
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

@cl.on_chat_start
async def start():
    print(uuid.uuid4())
    session_id = str(uuid.uuid4())
    # session_id = datetime.today().strftime('%Y%m%d%H%M%S')
    cl.user_session.set("session_id", session_id)
    await cl.Message(
        content="¡Hola! Bienvenidos a Pastelería La Palmera. Este medio es solo para consultas, no se reciben pedidos por este medio. Cualquier pedido que necesite realizar vía telefónica al 55 2 268988 o por nuestra pagina web."
    ).send()

@cl.on_message
async def main(message: cl.Message):

    msg = cl.Message(content=".")
    await msg.stream_token("..")
    await cl.sleep(1)
    
    session_id = cl.user_session.get("session_id")
    response = call_backend(message.content, session_id)

    msg.content = response
    await msg.update()

def call_backend(user_message, session_id) -> str:
    try:
        url = os.environ.get("RAG_MODEL")
        print("url", url)
        headers = {"Content-Type": "application/json", "sessionId": session_id}
        data = {"query": user_message}
        response = requests.post(url, json=data, headers=headers, timeout=(5, 40))
        response.raise_for_status()
        backend_response = response.json()
        print(backend_response)
        return backend_response['respuesta']
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar al backend: {e}")
        return "Disculpa no puedo responder en este momento"
    except requests.exceptions.Timeout as e:
        print(f"Error de timeout: {e}")
        return "Disculpa no puedo responder en este momento"