import json
import requests
from flask import jsonify
from model.date_time import DateTime

class CiudadesController:
    """Esta clase se encarga de manejar la informacion de las ciudades"""

    def __init__(self):
        """Constructor"""

    def obtenerListaCiudadesPaginado(self, pagina):
        """Devuelve el listado de ciudades de una determinada pagina"""
        resultado = []
        #Aca va a ir la logica para obtener las ciudades
        resultado.append('Ciudades...')
        return resultado
