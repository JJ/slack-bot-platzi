import os, sys, unittest
esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from SlackComandos import SlackComandos

class TestSlackComandos(unittest.TestCase):

    def setUp(self):
        self.comandos = SlackComandos()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.comandos,SlackComandos, "Objeto creado correctamente")

    def test_should_add_command(self):
        hola = lambda x: "Hola"
        self.comandos.nuevo( "Hola", hola )
        self.assertEqual( self.comandos.todos()['Hola'], hola, "Comando añadido" )

