#!/usr/bin/env python

import pika
import os
from dotenv import load_dotenv

class Conexion:
    """Encapsula la conexión a RabbitMQ"""
    
    enlace = None
    canal = None
    
    def __init__( self, dotenv_path=".env" ):
        load_dotenv(dotenv_path=dotenv_path)
        credentials = pika.PlainCredentials('platzi', os.environ.get('RMQ_PASS'))

        parameters= pika.URLParameters('amqp://platzi:{}@localhost:5672/platzi'.format(os.environ.get('RMQ_PASS')))

        self.enlace = pika.BlockingConnection( parameters )

        self.canal = self.enlace.channel()

        self.canal.queue_declare(queue='platzi')

    
