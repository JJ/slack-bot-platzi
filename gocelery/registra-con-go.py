import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()
app = Celery('tasks',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

task_protocol=1
if __name__ == '__main__':
    ordenes =['tres', 'uno','uno','uno','dos','dos', 'tres']
    for i in ordenes:
        print( "Envía ", i )
        enviado = app.send_task("tasks.registra", [i], serializer='json')
