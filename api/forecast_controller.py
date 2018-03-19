import json
import requests
from flask import jsonify
from model.date_time import DateTime

FORECAST_API_KEY = "aa0b96da7387272d1b44bf3384937863"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
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
        url = self._getUrl(city_id)
        # url de mock: "http://demo4909478.mockable.io/api/v1/forecast/1"
        forecastResponse = requests.get(url)
        jsonData = forecastResponse.json()

        currentDay = None
        iDay = 0
        iNight = 0
        acumDay = 0
        acumNight = 0
        weatherDay = ""
        weatherNight = ""

        result = {
            "code": 0,
            "forecast": []
        }

        dayForecast = {
            "day": {},
            "night": {}
        }

        if jsonData['cod'] == "200":
            weatherList = jsonData['list']
            for weatherRow in weatherList:
                rowDate = self._parseTime(weatherRow['dt_txt'])

                if currentDay == None:
                    currentDay = rowDate.day

                if rowDate.day == currentDay:
                    #mientras que nos mantengamos en el dia, agregar a las temps de dia o noche segun corresponda.
                    if (rowDate.hour == 21 or rowDate.hour == 0 or rowDate.hour == 3 or rowDate.hour == 6):
                        acumNight = acumNight + round(float(weatherRow['main']['temp']) - KELVIN_CONSTANT, 2)
                        iNight = iNight + 1
                        if weatherNight == "":
                            weatherNight = weatherRow['weather'][0]['icon'].replace("d", "n")
                    else:
                        acumDay = acumDay + round(float(weatherRow['main']['temp']) - KELVIN_CONSTANT, 2)
                        iDay = iDay + 1
                        if weatherDay == "":
                            weatherDay = weatherRow['weather'][0]['icon'].replace("n", "d")
                else:
                    #actualizo el current day
                    currentDay = rowDate.day

                    #Cambio el dia, entonces hay que subir los acumulados anteriores calculando el promedio
                    tempDay = round(float(acumDay / iDay), 2)
                    tempNight = round(float(acumNight / iNight), 2)
                    dayForecast["night"] = {
                        "temp": tempNight,
                        "weather": weatherNight
                    }
                    dayForecast["day"] = {
                        "temp": tempDay,
                        "weather": weatherDay
                    }

                    result['forecast'].append(dayForecast)
                    dayForecast = {}

                    iDay = 0
                    iNight = 0
                    acumDay = 0
                    acumNight = 0
                    weatherDay = ""
                    weatherNight = ""

                    if (rowDate.hour == 21 or rowDate.hour == 0 or rowDate.hour == 3 or rowDate.hour == 6):
                        acumNight = acumNight + round(float(weatherRow['main']['temp']) - KELVIN_CONSTANT, 2)
                        iNight = iNight + 1
                        if weatherNight == "":
                            weatherNight = weatherRow['weather'][0]['icon'].replace("d", "n")
                    else:
                        acumDay = acumDay + round(float(weatherRow['main']['temp']) - KELVIN_CONSTANT, 2)
                        iDay = iDay + 1
                        if weatherDay == "":
                            weatherDay = weatherRow['weather'][0]['icon'].replace("n", "d")

            #falta agregar el ultimo dia
            tempDay = round(float(acumDay / iDay), 2)
            tempNight = round(float(acumNight / iNight), 2)
            dayForecast["night"] = {
                "temp": tempNight,
                "weather": weatherNight
            }
            dayForecast["day"] = {
                "temp": tempDay,
                "weather": weatherDay
            }

            if len(result['forecast']) < 5:
                result['forecast'].append(dayForecast)

            result['code'] = 200
            return result
        else:
            #se produjo un error
            result['code'] = 500
            result['forecast'] = []
            return result
            

    def _getUrl(self, city_id):
        """ Devuelve la url formada para pegarle a la api del clima
            @city_id id de la ciudad
        """
        if city_id == "testUrl":
            return "http://demo4909478.mockable.io/api/v1/forecast/1"
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

