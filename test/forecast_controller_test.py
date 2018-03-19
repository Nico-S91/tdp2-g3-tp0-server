import unittest
import mock
import json
from test.response_mock import ResponseMock
from api.forecast_controller import ForecastController
from mock import MagicMock
import app

FORECAST_CONTROLLER = ForecastController()

class TestForecastController(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_obtener_clima_londres_cinco_dias(self):
        """ Prueba obtener el forecast para 5 dias de londres, parseando bien la respuesta de la API"""
        response_mock = ResponseMock()
        # response_mock.set_response("http://demo4909478.mockable.io/api/v1/forecast/1")
        # response_mock.set_code(200)
        response = self.app.get('/api/v1/forecast/testUrl')
        assert_res = json.loads("""
        {
            "code": 200, 
            "forecast": [
                {
                "day": {
                    "temp": -11.7, 
                    "weather": "02d"
                }, 
                "night": {
                    "temp": -11.74, 
                    "weather": "01n"
                }
                }, 
                {
                "day": {
                    "temp": -9.42, 
                    "weather": "13d"
                }, 
                "night": {
                    "temp": -10.74, 
                    "weather": "13n"
                }
                }, 
                {
                "day": {
                    "temp": -3.23, 
                    "weather": "13d"
                }, 
                "night": {
                    "temp": -5.86, 
                    "weather": "13n"
                }
                }, 
                {
                "day": {
                    "temp": -12.56, 
                    "weather": "01d"
                }, 
                "night": {
                    "temp": -11.49, 
                    "weather": "13n"
                }
                }, 
                {
                "day": {
                    "temp": -11.24, 
                    "weather": "04d"
                }, 
                "night": {
                    "temp": -15.2, 
                    "weather": "03n"
                }
                }
            ]
        }""")
        self.assertEqual(response.status_code, 200)
        cmp_response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(assert_res, cmp_response)
