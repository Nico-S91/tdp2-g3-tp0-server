import json
import requests
from flask import jsonify
from model.date_time import DateTime
from cache.clima_cache import ClimaCache

CLIMA_CACHE = ClimaCache()

class ClimaController:

    def __init__(self):
        """Constructor"""

    def getClimaCiudad(self, ciudad_id):
        """Obtener el clima de la ciudad"""
        respuesta = CLIMA_CACHE.obtener_info_ciudad(ciudad_id)
        response = jsonify(respuesta)
        response.status_code = respuesta.get('code')
        return response
