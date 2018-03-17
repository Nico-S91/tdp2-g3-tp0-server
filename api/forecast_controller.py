import json
import requests
from flask import jsonify
from model import date_time

FORECAST_API_KEY = "aa0b96da7387272d1b44bf3384937863"
FORECAST_URL = "api.openweathermap.org/data/2.5/forecast"

class ForecastController:
    """ Clase que contiene los metodos de comunicacion con la 
        API de consulta de clima."""

    def __init__(self):
        """Constructor"""

    def getForecast(self, city_id):
        """ Este metodo devuelve el clima de los siguientes
            5 dias para una determinada ciudad.
        """
        url = self._getUrl(city_id)
        forecastResponse = request(url)
        json_data = json.loads(forecastResponse)
        return jsonify(json_data)

    def _getUrl(self, city_id):
        """ Devuelve la url formada para pegarle a la api del clima
            @city_id id de la ciudad
        """
        return FORECAST_URL + "?id=" + str(city_id) + "&appid=" + FORECAST_API_KEY

    def _parseTime(self, dateString):
        """ Parsea el string de fecha y la devuelve en formato objeto
        """
        # Ej: 2017-01-30 18:00:00
        dateParse = dateString.split("-")
        dateTime = dateParse[2].split(" ")
        dateParse[2] = dateTime[0]
        dateTime = dateTime[1].split(":")
        #creo el objeto DateTime
        result = DateTime(int(dateParse[2]), int(dateParse[1]), int(dateParse[0]), int(dateTime[0]), int(dateTime[1]), int(dateTime[2]))
        return result

