"""Esta clase se encarga de crear los archivos con los listados de ciudades"""

import json
import codecs

#Ruta para los archivos de las ciudades
RUTA = 'data/ciudades/ciudades'
#Ruta para los archivos de las ciudades
DIR_CIUDADES = 'data/ciudades/ciudades.json'

CANT_CIUDADES_MAX = 2

def crear_listados():
    lista = json.load(codecs.open(DIR_CIUDADES, 'r', 'utf-8'))
    #Recorremos la lista y creamos los nuevos archivos
    pagina = 1
    cant_ciudades = 0
    ruta = RUTA + str(pagina) + ".json"
    lista_ciudades = []
    for ciudad in lista:
        if cant_ciudades < CANT_CIUDADES_MAX:
            cant_ciudades = cant_ciudades + 1
            lista_ciudades.append(ciudad)
        else:
            pagina = pagina + 1
            cant_ciudades = 1
            guardar_ciudades(lista_ciudades, ruta)
            ruta = RUTA + str(pagina) + ".json"
            lista_ciudades = []
            lista_ciudades.append(ciudad)
    if len(lista_ciudades) > 0:
        guardar_ciudades(lista_ciudades, ruta) 

def guardar_ciudades(lista_ciudades, ruta):
    print(ruta)
    with open(ruta, 'w') as f:
        json.dump(lista_ciudades, f)

print("Se crearan las listas de ciudades")
crear_listados()
