import json
import requests
import codecs
from flask import jsonify
from model.date_time import DateTime

#Ruta para los archivos de las ciudades
RUTA = 'data/ciudades/ciudades'

#La agrego ahora solo para usarla de ejemplo
class CiudadesController:
    """Esta clase se encarga de manejar la informacion de las ciudades"""

    def __init__(self):
        """Constructor"""

    def obtenerListaCiudadesPaginado(self, pagina):
        """Devuelve el listado de ciudades de una determinada pagina"""
        ruta = RUTA + str(pagina) + ".json"
        lista = json.load(codecs.open(ruta, 'r', 'utf-8'))
        #Procesamos la info para devolver lo que se necesita
        return self.obtenerListaCiudades(lista)

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
