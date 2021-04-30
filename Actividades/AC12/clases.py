import json
from datetime import datetime, timedelta
from hashlib import blake2b
import pickle

RECETAS_LOCK_PATH = 'RecetasLockJSON.json'
INGREDIENTES_PATH = 'ingredientes.txt'

'''
=====================================
NO BORRAR NI CAMBIAR!
'''
SUPER_SECRET_KEY = b'IIC2233'
'''
=====================================
'''


class Receta:
    """Clase que modela una receta del 'PyKitchen' cookbook"""

    def __init__(self, nombre='', ingredientes=None, alinos=None):
        self.nombre = nombre
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []
        self.llave_segura = None

    @property
    def verificada(self):
        """Property que nos indica si una receta fue limpiada o no."""
        return hasattr(self, 'llave_segura') and self.llave_segura == self.encriptar()

    def encriptar(self):
        """Funcion que encripta el valor a partir de una llave secreta"""
        encriptador = blake2b(key=SUPER_SECRET_KEY, digest_size=16)
        encriptador.update(self.nombre.encode())

        return encriptador.hexdigest()

    @staticmethod
    def abrir_ingredientes():
        """Genera las líneas del archivo ingredientes.txt"""
        with open(INGREDIENTES_PATH, encoding='utf-8') as fp:
            yield from map(lambda x: x.strip(), fp)

    def abrir_recetas_lock(self):
        """
        Funcion para abrir el archivo que indica los atributos
        de las recetas

        Implementa la funci ́on def abrir_recetas_lock(self), que deber ́a
        leer el archivoRecetasLockJSON.json y retornar un set de los atributos permitidos en las recetas
        """
        with open("RecetasLockJSON.json", encoding="utf-8") as file:
            data = set(json.load(file))

        return data

    def __setstate__(self, state):
        """
        Deserializa
        Elimina los atributos incorrectos y los ingredientes inválidos.
        """
        state = {i : state[i] for i in state if i in self.abrir_recetas_lock()}
        lista_aux = []
        for n in state["ingredientes"]:
            if n in self.abrir_ingredientes():
                lista_aux.append(n)
        state["ingredientes"] = lista_aux
        return state

    def __getstate__(self):
        """
        Serializa
        Recuerda colocar el atributo llave_segura.
        """

        self.llave_segura = self.__dict__
        self.llave_segura.update({"llave_segura" : self.encriptar()})


class Comida:
    def __init__(self,
                 nombre='',
                 nivel_preparacion=0.0,
                 ingredientes=None,
                 alinos=None,
                 fecha_ingreso=None):
        self.nombre = nombre
        self.nivel_preparacion = nivel_preparacion
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []

        if fecha_ingreso != None:
            delta  = timedelta(datetime.now(), self.str_a_date(
                fecha_ingreso))
            self.nivel_preparacion = self.nivel_preparacion + delta

        ''' Recuerda cambiar aqui el nivel de preparacion de acuerdo a la fecha
        de ingreso!'''

    @property
    def quemado(self):
        return self.nivel_preparacion > 100

    @property
    def preparado(self):
        return self.nivel_preparacion >= 100

    @staticmethod
    def date_a_str(fecha):
        return fecha.strftime('%Y-%m-%d-%H-%M-%S')

    @staticmethod
    def str_a_date(fecha_str):
        return datetime.strptime(fecha_str, '%Y-%m-%d-%H-%M-%S')

    @classmethod
    def de_receta(cls, receta):
        return cls(receta.nombre, 0.0, receta.ingredientes, receta.alinos)


class ComidaEncoder(json.JSONEncoder):
    """Utiliza esta clase para codificar en json"""

    def default(self, p):
        if isinstance(p, Comida):
           return {"nombre": p.nombre,
                    "nivel_preparacion": p.nivel_preparacion,
                    "ingredientes": p.ingredientes, "aliños": p.alinos,
                    "fecha_ingreso" : p.date_a_str(datetime.now())}

        return super().default(p)