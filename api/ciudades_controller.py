import json
import requests
from flask import jsonify
from model.date_time import DateTime

#La agrego ahora solo para usarla de ejemplo
LISTA_EJEMPLO = [
  {
    "id": 707860,
    "name": "Hurzuf",
    "country": "UA",
    "coord": {
      "lon": 34.283333,
      "lat": 44.549999
    }
  },
  {
    "id": 519188,
    "name": "Novinki",
    "country": "RU",
    "coord": {
      "lon": 37.666668,
      "lat": 55.683334
    }
  },
  {
    "id": 1283378,
    "name": "Gorkhā",
    "country": "NP",
    "coord": {
      "lon": 84.633331,
      "lat": 28
    }
  }
]

class CiudadesController:
    """Esta clase se encarga de manejar la informacion de las ciudades"""

    def __init__(self):
        """Constructor"""

    def obtenerListaCiudadesPaginado(self, pagina):
        """Devuelve el listado de ciudades de una determinada pagina"""
        resultado = self.obtenerListaCiudades(LISTA_EJEMPLO)
        return resultado

    def obtenerListaCiudades(self, listaOriginal):
        """Armamos la lista de ciudades a devolver"""
        lista = []
        for ciudad in listaOriginal:
            infociudad = {}
            infociudad['id'] = ciudad['id']
            infociudad['name'] = ciudad['name']
            infociudad['country'] = ciudad['country']
            lista.append(infociudad)
        return lista
