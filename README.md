# tdp2-g3-tp0-server
Proyecto del servidor para el trabajo practico 0 de TDPII.

# Para correr la app por primera vez
pip install -r requirements.txt

#Creamos un virtual env
virtualenv venv

#PARA CORRER LA APP: estos 3 pasos los hacemos siempre cuando prendemos todo
#corremos virtualenv
venv/Scripts/activate

#seteamos el punto de entrada de flask
set FLASK_APP=app.py

#Ya solo queda correr el run
flask run