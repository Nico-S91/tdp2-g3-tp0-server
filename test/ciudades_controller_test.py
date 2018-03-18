import unittest
import mock
import json
from api.ciudades_controller import CiudadesController
from mock import MagicMock

CIUDADES_CONTROLLER = CiudadesController()

class TestCiudadesController(unittest.TestCase):

    def test_obtener_lista_ciudades_transformadas_vacia(self):
        """Prueba para transformar una lista vacia"""
        lista = []
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudades(lista)
        self.assertEqual(len(lista_transformada), len(lista))

    def test_obtener_lista_ciudades_transformadas(self):
        """Prueba transformar una lista de ciudades"""
        lista = [{"id": 707860, "name": "Hurzuf", "country": "UA", "coord": {"lon": 34.283333, "lat": 44.549999}}, {"id": 519188, "name": "Novinki", "country": "RU", "coord": {"lon": 37.666668, "lat": 55.683334}}]
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudades(lista)
        lista_esperada = [{"id": 707860, "name": "Hurzuf", "country": "UA"}, {"id": 519188, "name": "Novinki", "country": "RU"}]
        self.assertEqual(len(lista_transformada), len(lista))
        self.assertEqual(lista_esperada, lista_transformada)

    def test_obtener_lista_ciudades_transformadas_pagina_inexistente(self):
        """Prueba al pedir la lista de una pagina que no existe entonces devuelve una lista vacia"""
        lista = []
        CiudadesController.obtenerCiudadesArchivo = MagicMock(return_value=lista)
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudadesPaginado(999999)
        self.assertEqual(len(lista_transformada), len(lista))

    def test_obtener_lista_ciudades_transformadas_pagina_existente(self):
        """Prueba transformar una lista de ciudades"""
        lista = [{"id": 707860, "name": "Hurzuf", "country": "UA", "coord": {"lon": 34.283333, "lat": 44.549999}}, {"id": 519188, "name": "Novinki", "country": "RU", "coord": {"lon": 37.666668, "lat": 55.683334}}]
        CiudadesController.obtenerCiudadesArchivo = MagicMock(return_value=lista)
        lista_transformada = CIUDADES_CONTROLLER.obtenerListaCiudadesPaginado(2)
        lista_esperada = [{"id": 707860, "name": "Hurzuf", "country": "UA"}, {"id": 519188, "name": "Novinki", "country": "RU"}]
        self.assertEqual(len(lista_transformada), len(lista))
        self.assertEqual(lista_esperada, lista_transformada)
