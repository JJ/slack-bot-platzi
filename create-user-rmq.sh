#!/bin/bash


RABBITMQ_NODENAME=platzi
rabbitmq-server start -detached                             # Arranca el servidor
sleep 2                                                     # Necesario para lo siguiente
rabbitmqctl start_app                                       # Arranca app
echo "Arrancada aplicación"
echo $1
rabbitmqctl add_user platzi $1                              # Cambiar a una clave determinada
rabbitmqctl add_vhost platzi                                # Host virtual que vamos a usar
rabbitmqctl set_permissions -p platzi platzi ".*" ".*" ".*" # Permisos del usuario sobre el vhost
rabbitmqctl set_user_tags platzi management                 # Calificción del usuario nuevo.

