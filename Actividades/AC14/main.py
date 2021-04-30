import json
import re
from time import sleep

import requests
from credenciales import API_KEY


API_URL = "https://api.nasa.gov/planetary/apod"
DIR_IMAGENES = 'imagenes'
PATH_RESULTADOS = 'resultados.txt'


def limpiar_fecha(linea):
    '''
    Esta función se encarga de limpiar el texto introducido a las fechas

    :param linea: str
    :return: str
    '''

    new_linea = re.sub("<[a-zA-Z][0-9]>", "", linea)
    new_linea = re.sub("<[a-zA-Z]*>", "", new_linea)
    new_linea = re.sub("</[a-zA-Z]*[0-9]*>", "", new_linea)
    new_linea = re.sub("<>", "", new_linea)

    return new_linea


def chequear_fecha(fecha):
    '''
    Esta función debe chequear si la fecha cumple el formato especificado

    :param fecha: str
    :return: bool
    '''
    pattern = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    boolean = re.fullmatch(pattern, fecha)

    return boolean


def obtener_fechas(path):
    '''
    Esta función procesa las fechas para devolver aquellas que son útiles
    para realizar las consultas a la API

    :param path: str
    :return: iterable
    '''

    lista_valida = []
    with open(path, "r") as file:
        for i in file:
            i = i.strip()
            limpiado = limpiar_fecha(i)
            boolean = chequear_fecha(limpiado)
            if boolean:
                lista_valida.append(limpiado)
    return lista_valida


def obtener_info(fecha):
    '''
    Recibe una fecha y retorna un diccionario
    con el título, la fecha y el url de la imagen
    :param fecha: str
    :return: dict
    '''
    url = API_URL
    response = requests.get(API_URL)
    ip = response.text

    nasa = requests.get(f'{url}', params={'api_key': API_KEY,
                                               "date":fecha, "hd":False})
    response = nasa.json()

    datos_send = {"titulo":response["title"], "fecha":response["date"],
                  "url":response["url"]}

    return datos_send


def escribir_respuesta(datos):
    '''
    Esta función debe escribir las respuestas de la API en el archivo
    resultados.txt
    :param datos_respuesta: dict
    '''

    with open("resultados.txt", "a") as file:
        file.write("{}-->{}:{}\n".format(datos["fecha"],datos["titulo"],
                                       datos["url"]))

    nombre = datos["url"].split("/")
    length = len(nombre)
    nombre = nombre[length - 1]

    descargar_imagen(datos["url"], "imagenes/{}".format(nombre))


def descargar_imagen(url, path):
    '''
    Recibe la url de una imagen y guarda los datos en un archivo en path

    :param url: str
    :param path: str
    '''
    respuesta = requests.get(url, stream=True)
    if respuesta.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in respuesta:
                f.write(chunk)


if __name__ == "__main__":
    PATH_FECHAS = 'fechas_secretas.txt'

    for fecha in obtener_fechas(PATH_FECHAS):
        respuesta = obtener_info(fecha)
        escribir_respuesta(respuesta)
        

