#!/usr/bin/env python

# Adaptado de https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
# Debe tener licencia libre

import os
import time
import re
from slackclient import SlackClient

from dotenv import load_dotenv
load_dotenv()

print( os.environ.get('BOT_FICHA') )
slack_client = SlackClient(os.environ.get('BOT_FICHA'))
starterbot_id = None
print(slack_client)

RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
ORDEN_EJEMPLO = "ve"
MENCION_REGEX = "^<@(|[WU].+?)>(.*)"

def procesa_comandos(eventos):
    """
       Procesa una lista de comandos y devuelve orden y canal, o bien None,None
    """
    for evento in eventos:
        if evento["type"] == "message" and not "subtype" in evento:
            user_id, message = procesa_mencion_directa(evento["text"])
            if user_id == starterbot_id:
                return message, evento["channel"]
    return None, None

def procesa_mencion_directa(texto):
    """
        Encuentra menciones directas y devuelve el ID mencionado o nada.
    """
    matches = re.search(MENCION_REGEX, texto)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def maneja_comando(comando, canal):
    """
        Ejecuta el comando si se conoce.
    """
    # Default response is help text for the user
    default_response = "No te entiendo. Prueba *{}*.".format(ORDEN_EJEMPLO)

    response = None
    if comando.startswith(ORDEN_EJEMPLO):
        response = "Por lo pronto vas bien"

    slack_client.api_call(
        "chat.postMessage",
        channel=canal,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("¡Vamos charlandero!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = procesa_comandos(slack_client.rtm_read())
            if command:
                maneja_comando(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Ha fallado. Lee más abajo para averiguar por qué")


