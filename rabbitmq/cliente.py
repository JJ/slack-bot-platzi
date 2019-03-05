#!/usr/bin/env python

from Conexion import Conexion

conexion = Conexion('../.env')

enlace = conexion.enlace

canal = conexion.canal

canal.basic_publish(exchange='',
                    routing_key='platzi',
                    body='Descarga')

print(" [x] Solicitada descarga")
enlace.close()
