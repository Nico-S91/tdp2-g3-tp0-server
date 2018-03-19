from api.forecast_controller import ForecastController
import time
import json

#Tiempo maximo es 10 min, lo uso en milisegundos
TIEMPO_MAX = 10 * 60 * 1000

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
            resultado['code'] = CODE_ESPERAR
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
        res = {"code":200,"forecast":[{"day":{"temp":24.72495993583186,"weather":"02d"},"night":{"temp":20.397672523433844,"weather":"02n"}},{"day":{"temp":19.126333049992787,"weather":"04d"},"night":{"temp":15.672498729341998,"weather":"01n"}},{"day":{"temp":21.351756099054843,"weather":"02d"},"night":{"temp":23.658643624538698,"weather":"03n"}},{"day":{"temp":27.064653499927406,"weather":"03d"},"night":{"temp":18.112496966329527,"weather":"01n"}},{"day":{"temp":15.20555024637092,"weather":"02d"},"night":{"temp":17.892319110983326,"weather":"02n"}}]}
        return res
        # return FORESCAST_API.getForecast(ciudad_id)        
