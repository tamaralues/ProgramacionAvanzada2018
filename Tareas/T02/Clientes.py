from Humanos import *

# Ludopata

class Ludopata(Clientes):

    def __init__(self):
        super().__init__("ludopata")
        self.tipo = "ludopata"
        # Estas son properties ya que tienen condiciones de no ser menores a 0
        self.dinero = uniform(0.30, 0.70) * 200
        self.dinero_entrada = self.dinero
        self.lucidez = uniform(0.30, 0.70)
        self.ansiedad = uniform(0.70, 1.00)
        self.suerte = uniform(0.30, 0.70)
        self.sociabilidad = uniform(0.30, 0.70)
        self.stamina = uniform(0.70, 1.00)
        self.deshonestidad = uniform(0.30, 0.70)
        self.x = 0
        self.y = 0
        self.angle = 0

# Kibitzer


class Kibitzer(Clientes):

    def __init__(self):
        super().__init__("kibitzer")
        self.tipo = "kibitzer"
        # Estas son properties ya que tienen condiciones de no ser menores a 0
        self.dinero = uniform(0.00, 0.30) * 200
        self.lucidez = uniform(0.30, 0.70)
        self.dinero_entrada = self.dinero
        self.ansiedad = uniform(0.00, 0.30)
        self.suerte = uniform(0.30, 0.70)
        self.sociabilidad = uniform(0.70, 1.00)
        self.stamina = uniform(0.00, 0.30)
        self.deshonestidad = uniform(0.30, 0.70)
        self.x = 0
        self.y = 0
        self.angle = 0
        # Es del tipo booleano, si es True entonces esta prediciendo
        self.prediciendo = False

        # importar de opciones externas de que hacer con cierta probabilidad
        # cada un

    """
    @property
    def prediciendo(self):
        return self.prediciendo_

    @prediciendo.setter
    def prediciendo(self, value):
        if value == self.acciones.fisico_determinista():
            self.prediciendo_ = True
        else:
            self.prediciendo_ = False
    """


# Diciochero


class Dieciochero(Clientes):

    def __init__(self):
        super().__init__("dieciochero")
        self.tipo = "dieciochero"

        # Estas son properties ya que tienen condiciones de no ser menores a 0

        self.dinero = uniform(0.30, 0.70) * 200
        self.dinero_entrada = self.dinero
        self.lucidez = uniform(0.00, 0.30)
        self.ansiedad = uniform(0.70, 1.00)
        self.suerte = uniform(0.30, 0.70)
        self.sociabilidad = uniform(0.70, 1.00)
        self.stamina = uniform(0.30, 0.70)
        self.deshonestidad = uniform(0.00, 0.30)
        self.x = 0
        self.y = 0
        self.angle = 0

# El ganador


class Ganador(Clientes):

    def __init__(self):
        super().__init__("ganador")
        self.tipo = "ganador"

        # Estas son properties ya que tienen condiciones de no ser menores a 0
        self.dinero = uniform(0.30, 0.70) * 200
        self.dinero_entrada = self.dinero
        self.lucidez = uniform(0.30, 0.70)
        self.ansiedad = uniform(0.30, 0.70)
        self.suerte = uniform(0.70, 1.00)
        self.sociabilidad = uniform(0.70, 1.00)
        self.stamina = uniform(0.70, 1.00)
        self.deshonestidad = uniform(0.70, 1.00)
        self.x = 0
        self.y = 0
        self.angle = 0

    # Acciones es un objeto que posee todas las opciones que el ususario
    # puede elegir

# Millonario


class Millonario(Clientes):

    def __init__(self):
        super().__init__("millonario")
        self.tipo = "millonario"

        # Estas son properties ya que tienen condiciones de no ser menores a 0

        self.dinero = uniform(0.30, 0.70) * 200
        self.dinero_entrada = self.dinero
        self.lucidez = uniform(0.00, 0.30)
        self.ansiedad = uniform(0.70, 1.00)
        self.suerte = uniform(0.30, 0.70)
        self.sociabilidad = uniform(0.70, 1.00)
        self.stamina = uniform(0.30, 0.70)
        self.deshonestidad = uniform(0.00, 0.30)
        self.x = 0
        self.y = 0
        self.angle = 0

        # importar de opciones externas de que hacer con cierta probabilidad
        # cada un
