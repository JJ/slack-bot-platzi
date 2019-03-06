import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()
app = Celery('registra-con-go',
             broker='amqp://platzi:{}@localhost/platzi'.format(os.environ.get('RMQ_PASS')))

if __name__ == '__main__':
    ordenes =['uno','uno','uno','dos','dos', 'tres']
    for i in ordenes:
        print( "Envía ", i )
        app.send_task("worker.registra", [i])
