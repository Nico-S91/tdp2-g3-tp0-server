from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/v1/forecast/<string:city_id>', methods=['GET'])
def get_forecast(city_id):
    """ Endpoint que devuelve el pronostico del clima
        de una determinada ciudad."""
    response = FORECAST_CONTROLLER.getForecast(city_id)