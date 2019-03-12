# Ajusta para que lea del directorio superior
import os,sys
esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')
from PlatziAgenda import PlatziAgenda

# Biblioteca celery
from celery import Celery,task


app=Celery('agenda-platzi')
app.config_from_object('celeryconfig',force=True)

@app.task
def siguiente():
    agenda = PlatziAgenda()
    return agenda.siguiente()

@app.task
def busca( argumento ):
    agenda = PlatziAgenda()
    resultado = agenda.busca( argumento )
    response = ""
    if not "Encontrado" in resultado: 
        response = "Tenemos los siguientes cursos\n"
        for i in resultado:
            response = response + "→ " + resultado[i]['titulo']+"\n"
    else:
        response = "Lo siento: no hay ningún curso con *{}*\n".format(argumento)

    return response
