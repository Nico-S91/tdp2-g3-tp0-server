import unittest
import mock
import json
from api.ciudades_controller import CiudadesController
from mock import MagicMock

CIUDADES_CONTROLLER = CiudadesController()

class TestCiudadesController(unittest.TestCase):

    def test_obtener_lista_ciudades_transformadas_vieja(self):
        """Prueba al pedir la lista de una pagina que no existe entonces devuelve una lista vacia"""
        lista = []
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudades(lista)
        self.assertEqual(len(lista_transformada), len(lista))

    def test_obtener_lista_ciudades_transformadas(self):
        """Prueba al pedir la lista de una pagina que no existe entonces devuelve una lista vacia"""
        lista = [{"id": 707860, "name": "Hurzuf", "country": "UA", "coord": {"lon": 34.283333, "lat": 44.549999}}, {"id": 519188, "name": "Novinki", "country": "RU", "coord": {"lon": 37.666668, "lat": 55.683334}}]
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudades(lista)
        lista_esperada = [{"id": 707860, "name": "Hurzuf", "country": "UA"}, {"id": 519188, "name": "Novinki", "country": "RU"}]
        self.assertEqual(len(lista_transformada), len(lista))
        self.assertEqual(lista_esperada, lista_transformada)
