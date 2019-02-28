import os, sys, unittest
esto = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, esto + '/../')

from PlatziAgenda import PlatziAgenda

class TestPlatziAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = PlatziAgenda()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.agenda,PlatziAgenda, "Objeto creado correctamente")

    def test_should_return_first_course(self):
        curso = self.agenda.siguiente()
        self.assertIsInstance( curso, dict, "Extraido primer curso" )
        self.assertNotEqual( curso['titulo'], "", "Titulo existe" )
