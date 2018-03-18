from flask import Flask
from api.forecast_controller import ForecastController
from api.ciudades_controller import CiudadesController
from flask import jsonify

app = Flask(__name__)

FORECAST_CONTROLLER = ForecastController()
CIUDADES_CONTROLLER = CiudadesController()

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/v1/forecast/<string:city_id>', methods=['GET'])
def get_forecast(city_id):
    """ Endpoint que devuelve el pronostico del clima
        de una determinada ciudad."""
    response = FORECAST_CONTROLLER.getForecast(city_id)
    return response

@app.route('/api/v1/cities/<int:page_id>', methods=['GET'])
def get_ciudades(page_id):
	#Endpoint que devuelve las ciudades de una pagina
	if page_id >= 1:
		ciudades = CIUDADES_CONTROLLER.obtenerListaCiudadesPaginado(page_id)
		resultado = jsonify(ciudades)
		return resultado
	else:
		resultado = jsonify('La pagina debe ser un valor numerico mayor igual a 1')
		resultado.status_code = 400
		return resultado

if __name__ == '__main__':
    app.run(host='0.0.0.0')