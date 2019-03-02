


def PlatziSlackComando( comandero, comando, func ):
    def new_function( *args, **kwargs ):
        agenda = PlatziAgenda()
        func(agenda, *args)
        return new_function
    comandero.nuevo( comando, new_function)

        


