import os, json, re

class PlatziAgenda:
    """Una clase para contener los elementos de la agenda de la web de Platzi"""

    def __init__ (self,  data_file = "data/cursos.json"):
        
        if not os.path.exists( data_file ):
            data_file = "../" + data_file

        with open(data_file) as f:
            self.agenda = json.load(f)
            self.primero = sorted(self.agenda.keys())[0]

    def siguiente(self):
        return self.agenda[self.primero]

    def codigos(self):
        return list(self.agenda.keys())

    def curso(self, codigo ):
        return self.agenda[codigo]
    
    def busca(self, aguja ):
        return {k: v for k, v in self.agenda.items() if v['titulo'].find( aguja ) >= 0 } or "No lo encuentro"



