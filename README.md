# tdp2-g3-tp0-server
Proyecto del servidor para el trabajo practico 0 de la materia Taller de desarrollo de proyectos II

## Prerequisitos
Para poder correr la aplicación, es necesario contar con:
* Python v >= 3.5

## Instalacion e inicio local
Para hacer esto hay dos opciones:

### Opcion I:

#### Para correr la app por primera vez
virtualenv venv

##### Inicio
venv/Scripts/activate
pip install -r requirements.txt
set FLASK_APP=app.py
flask run

### Opcion II:

#### Instalación
Previo a iniciar el server, es necesario correr los siguientes comandos:
* pipenv install -r requirements.txt

#### Inicio
Para iniciar el server, se debe:
* el puerto por defecto de la aplicacion va a ser 5000 (sin gunicorn)
* correr el comando **python app.py** para levantar la app con el servidor de pruebas de Flask

## Inicio Gunicorn
Para iniciar el servidor corriendo sobre Gunicorn:
* Ejecutar el comando "gunicorn app" (sin las comillas)
* La aplicacion sera levantada sobre localhost, puerto 8000 (http://localhost:8000 o 127.0.0.1:8000)

## Inicio Heroku
La aplicacion esta hosteada en Heroku, para acceder a ella:
* Ingesar a https://tdp2-tp0.herokuapp.com/
* poner luego una url correspondiente al listado de los servicios de endpoints disponibles

## Tests
Para correr los tests de la aplicación, correr el comando **pytest test/**
