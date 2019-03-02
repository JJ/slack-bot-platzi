

class SlackComandos:
    """Una clase para contener los comandos de Slack """

    def __init__ (self):
        self.comandos = {}

    def nuevo( self, comando, funcion ):
        self.comandos[comando] = funcion

    def todos( self ):
        return self.comandos



