#!/usr/bin/env python

import pika
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')
credentials = pika.PlainCredentials('platzi', os.environ.get('RMQ_PASS'))

parameters= pika.URLParameters('amqp://platzi:{}@localhost:5672/platzi'.format(os.environ.get('RMQ_PASS')))

connection = pika.BlockingConnection( parameters )

channel = connection.channel()

channel.queue_declare(queue='platzi')

channel.basic_publish(exchange='',
                      routing_key='platzi',
                      body='Descarga')

print(" [x] Solicitada descarga")
connection.close()
