

class SlackComandos:
    """Una clase para contener los comandos de Slack """

    def __init__ (self):
        self.comandos = {}
        self.comandos_str = ()
        
    def nuevo( self, comando, funcion ):
        self.comandos[comando] = funcion
        self.comandos_str = list (self.comandos.keys())
        
    def todos( self ):
        return self.comandos

    def maneja( self, mensaje ):
        este_comando = ''
        for c in self.comandos_str:
            if mensaje.startswith( c + " " ):
                este_comando = c
                break
        if este_comando == '':
            raise KeyError( "No se encuentra ningún comando en {}".format(mensaje) )
        
        argumentos = mensaje[ 1+len(este_comando): ]
        return self.comandos[este_comando](argumentos )



