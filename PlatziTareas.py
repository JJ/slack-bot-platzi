import os
from PlatziAgenda import PlatziAgenda
from celery import Celery,task
from dotenv import load_dotenv


load_dotenv()

app = Celery('platzi-tareas',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')),
             backend='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

@app.task
def siguiente():
    agenda = PlatziAgenda()
    return agenda.siguiente()

@app.task
def busca( argumento ):
    agenda = PlatziAgenda()
    resultado = agenda.busca( argumento )
    response = ""
    if resultado: 
        response = "Tenemos los siguientes cursos\n"
        for i in resultado:
            response = response + "→ " + resultado[i]['titulo']+"\n"

    else:
        response = "No hemos encontrado ningún curso con *{}*".format( argumento )    
    return response
