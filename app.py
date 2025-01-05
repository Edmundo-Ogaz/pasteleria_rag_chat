import chainlit as cl
import requests

import os
from dotenv import load_dotenv
load_dotenv()

@cl.on_message
async def main(message: cl.Message):
    response = call_backend(message.content)
    await cl.Message(
        content = response
    ).send()

def call_backend(user_message):
    try:
        url = os.environ.get("RAG_MODEL")
        headers = {"Content-Type": "application/json"}
        data = {"query": user_message}
        response = requests.post(url, json=data, headers=headers, timeout=(5, 50))
        response.raise_for_status()
        backend_response = response.json()
        print(backend_response)
        return backend_response['respuesta']
    except requests.exceptions.RequestException as e:
        print(f"Error al llamar al backend: {e}")
        return {"error": str(e)}
    except requests.exceptions.Timeout as e:
        print(f"Error de timeout: {e}")
        return {"error": str(e)}