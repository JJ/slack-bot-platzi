import os
from dotenv import load_dotenv
import socket

load_dotenv()
hostname = socket.gethostname()
broker_url = 'amqp://platzi:{}@{}/platzi'.format(os.environ.get('RMQ_PASS'),hostname)
result_backend = 'redis://'

