from api.forecast_controller import ForecastController
import time
import json

#Tiempo maximo es 1seg, lo uso en milisegundos
TIEMPO_MAX = 1 * 1000

#Este codigo va a indicarle al cliente que tiene que esperar para pedir nuevamente la info a la API
CODE_ESPERAR = 400
CODE_SIN_CIUDAD = 500
CODE_OK = 200

FORESCAST_API = ForecastController()

class ClimaCache:

    def __init__(self):
        """Constructor"""
        self.ultima_vez_invocado = None
        self.ciudad = None
        self.respuesta = None
    
    def obtener_info_ciudad(self, ciudad_id):
        resultado = {}
        if ciudad_id is None:
            resultado['code'] = CODE_SIN_CIUDAD
            return resultado
        if self.ultima_vez_invocado is not None:
            fecha_ahora = int(round(time.time() * 1000))
            dif_tiempo = fecha_ahora - self.ultima_vez_invocado
            if (dif_tiempo < TIEMPO_MAX):
                #No podemos pedir info a la API, hay que esperar
                if self.ciudad == ciudad_id:
                    #Tenemos la info de 
                    return self.respuesta
                else:
                    resultado['code'] = CODE_ESPERAR
                    return resultado
            else:
                #Podemos pedir nuevamente la informacion
                respuesta = self.obtener_info_api(ciudad_id)
                if respuesta.get('code') == 200:
                    self.ciudad = ciudad_id
                    self.respuesta = respuesta
                    milis = int(round(time.time() * 1000))
                    self.ultima_vez_invocado = (milis)
                return respuesta
        else:
            #Nunca se pidio, asi que vamos a pedir info
            respuesta = self.obtener_info_api(ciudad_id)
            if respuesta.get('code') == 200:
                self.ciudad = ciudad_id
                self.respuesta = respuesta
                milis = int(round(time.time() * 1000))
                self.ultima_vez_invocado = (milis)
            return respuesta

    def obtener_info_api(self, ciudad_id):
        return FORESCAST_API.getForecast(ciudad_id)        
