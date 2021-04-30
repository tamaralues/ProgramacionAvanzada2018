from gui.entities import Building, Game
from Ubicaciones_fijas import *
from random import getrandbits
from Parametros import *

class Juego(Game):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = ""
        self.personal = []
        self.capacidad = 0
        self.pozo = 0
        self.probabilidad_juego_ruleta = 0
        self.probabilidad_juego_tragamonedas = 0
        self.tipo_apuesta = ""
        self.numero_color = ""
        self.color = ""
        self.pozo_casino = 0
        self.ganancia = 0
        self.visitas = 0
        self.perdida = 0


class NoJuegos(Building):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.personal = 0
        self.pozo_casino = 0
        self.visitas = 0
        self.no_funcionando = 0

class Tragamonedas(Juego):
    def __init__(self):
        super().__init__("tragamonedas")
        self.nombre = "tragamonedas"
        self.id = "{}{}".format(self.nombre, getrandbits(28))
        self.estado = False
        self.capacidad = 1
        self.probabilidad_tragamoneda = alfa

        if len(lista_ub_tragamonedas) > 0:
            self.ubicacion = lista_ub_tragamonedas.pop()
            self.x = self.ubicacion[0]
            self.y = self.ubicacion[1]

        else:
            return

    def estado_(self):
        c = 0
        for i in self.personal:
            if i.trabajando == True:
                c += 1

        if c < 1:
            self.estado = False
        else:
            self.estado = True


class Ruleta(Juego):
    def __init__(self):
        super().__init__("ruleta")
        self.nombre = "ruleta"
        self.id = "{}{}".format(self.nombre, getrandbits(28))
        self.estado = False
        if len(lista_ub_ruleta) > 0:
            self.ubicacion = lista_ub_ruleta.pop()
            self.x = self.ubicacion[0]
            self.y = self.ubicacion[1]
        else:
            return

        if self.tipo_apuesta == "color":
            if self.color == "Verde":
                self.ganancia = 5
                self.probabilidad_juego_ruleta = 1 / (gamma + 1)

            elif self.color == "Negro":
                self.ganancia = 1.5
                self.probabilidad_juego_ruleta = gamma / (2 * (gamma + 1))

            elif self.color == "Rojo":
                self.ganancia = 1.5
                self.probabilidad_juego_ruleta = gamma / (2 * (gamma + 1))

        else:
            self.ganancia = 5
            self.probabilidad_juego_ruleta = 1 / (gamma + 1)

    def estado_(self):
        c = 0
        for i in self.personal:
            if i.trabajando == True:
                c += 1
        if c < 1:
            self.estado = False
        else:
            self.estado = True


class Tarot(NoJuegos):
    def __init__(self):
        super().__init__("tarot")
        self.nombre = "tarot"
        self.id = "{}{}".format(self.nombre, getrandbits(28))
        self.costo = 10
        self.personal = []
        self.estado = False
        self.capacidad = 1

        if len(lista_ub_tarot) > 0:
            self.ubicacion = lista_ub_tarot.pop()
            self.x = self.ubicacion[0]
            self.y = self.ubicacion[1]
        else:
            return

    def estado_(self):
        c = 0
        for i in self.personal:
            if i.trabajando == True:
                c += 1
        if c == 1:
            self.estado = True
        else:
            self.estado = False

class Restobar(NoJuegos):
    def __init__(self):
        super().__init__("restobar")
        self.nombre = "restobar"
        self.id = "{}{}".format(self.nombre, getrandbits(28))
        self.x = 420
        self.y = 230
        self.estado = False
        self.capacidad = 20
        self.personal = []

    def estado_(self):
        c = 0
        for i in self.personal:
            if i.trabajando == True:
                c += 1
        if c < 2:
            self.estado = False

        else:
            self.estado = True


class Restroom(NoJuegos):
    # Puse solo 1 baño, que es el que tienen para usar todos
    def __init__(self):
        super().__init__("baños")
        self.nombre = "baño"
        self.id = "{}{}".format(self.nombre, getrandbits(28))
        self.x = 650
        self.y = 350
        self.estado = True