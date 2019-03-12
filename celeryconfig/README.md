# Notas

Esta es una versión del cliente/worker del bot que usa dos cosas diferentes a la anterior

* Fichero de configuración [`celeryconfig.py`](celeryconfig.py) en vez de configurar a mano.
* Redis de backend en vez de usar el propio RabbitMQ, lo que da un aviso de deprecación.

Para ejecutarlo en el orden correcto, se puede arrancar con `foreman start`

(Tras instalar `foreman`, que es un gestor de tareas basado en Ruby, también usado por Heroku, y que es muy aconsejable)