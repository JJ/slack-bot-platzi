import os
from PlatziAgenda import PlatziAgenda
from celery import Celery
from dotenv import load_dotenv


load_dotenv()

app = Celery('platzi-tareas',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

@app.task
def siguiente():
    agenda = PlatziAgenda()
    return agenda.siguiente
