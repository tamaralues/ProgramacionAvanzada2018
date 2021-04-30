import json
import os
import os.path as path
import pickle

from clases import Comida, ComidaEncoder

BOOK_PATH = 'recetas.book'

class PyKitchen:
    def __init__(self):
        self.recetas = []
        self.comidas = []
        self.despachadas = []


    def cargar_recetas(self):
        '''Esta función se encarga de cargar el archivo recetas.book'''
        with open(BOOK_PATH, encoding="utf-8") as file:
            data = pickle.load(file)
        self.recetas = data

    def guardar_recetas(self):
        with open(BOOK_PATH, "w", encoding="utf-8") as file:
            for i in self.recetas:
                file.write(i)
            
    def cocinar(self):
        '''Esta funcion debe:
        - filtrar recetas verificadas
        - crear comidas a partir de estas recetas
        - guardar las comidas en la carpeta horno
        '''
        pass

    def despachar_y_botar(self):
        ''' Esta funcion debe:
        - Cargar las comidas que están en la carpeta horno.
            Pro tip: string.endswith('.json') retorna true si un string
            termina con .json
        - Crear instancias de Comida a partir de estas.
        - Guardar en despachadas las que están preparadas
        - Imprimir las comidas que están quemadas
        - Guardar en comidas las no preparadas ni quemadas
        '''
        pass
