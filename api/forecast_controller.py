import json
import requests
from flask import jsonify
from model import date_time

FORECAST_API_KEY = "aa0b96da7387272d1b44bf3384937863"
FORECAST_URL = "api.openweathermap.org/data/2.5/forecast"
KELVIN_CONSTANT = 273.15

class ForecastController:
    """ Clase que contiene los metodos de comunicacion con la 
        API de consulta de clima."""

    def __init__(self):
        """Constructor"""

    def getForecast(self, city_id):
        """ Este metodo devuelve el clima de los siguientes
            5 dias para una determinada ciudad.
        """
        # url = self._getUrl(city_id)
        url = "http://demo9410278.mockable.io/forecast"
        forecastResponse = request(url)
        jsonData = json.loads(forecastResponse)

        result = {
            "code": 0,
            "forecast": []
        }

        dayForecast = {}

        if jsonData['cod'] == 200
            weatherList = jsonData['list']
            for weatherRow in weatherList:
                rowDate = self._parseTime(weatherRow['dt_txt'])

                if rowDate.hour == 00:
                    #creo el clima a la noche
                    temp = float(rowDate['main']['temp']) - KELVIN_CONSTANT
                    weather = rowDate['weather'][0]['icon']
                    dayForecast.append("night": 
                        {
                            "temp": temp,
                            "weather": weather
                        })
                else if rowDate.hour == 12:
                    #creo el clima a la mañana
                    temp = float(rowDate['main']['temp']) - KELVIN_CONSTANT
                    weather = rowDate['weather'][0]['icon']
                    dayForecast.append("day":
                        {
                            "temp": temp,
                            "weather": weather
                        })
                    result['forecast'].append(dayForecast)
                    dayForecast = {}

            result['code'] = 200
            return jsonify(result)
        else:
            #se produjo un error
            result['code'] = 500
            return result
            

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

