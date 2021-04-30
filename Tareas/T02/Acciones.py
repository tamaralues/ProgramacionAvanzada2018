# Estas modifican comportamiento y ubicacion de las personas
from random import random, choice

class Acciones:

    def __init__(self):
        self.duracion_max = ""
        self.conversando = []
        self.quiere_conversar = []
        self.pozo_casino_ac = 0

    def retirarse(self):
        # finalizar estadía
        return "me retiro"

    def jugar(self):
        juegos = ["ruleta", "tragamonedas"]
        juego = choice(juegos)
        # incluir cambio de estado ??
        return juego

    def participar(self, tipo):

        if tipo == "kibitzer":
            participar = ["conversar", "hablar con tini", "fisico "
                                                          "determinista"]

        else:
            participar = ["conversar", "hablar con tini"]

        participar = choice(participar)

        # si se elije participar, se hace el llamado aleatoriamente a
        # conversar, hablar con pini o fisico determinista

        return participar

    def ir_instalacion(self):
        # elegir instalacion
        instalacion = ["restobar", "baño", "tarot"]
        instalacion = choice(instalacion)
        return instalacion

    def hablar_con_tini(self):
        return "hablo con tini"

    def fisico_determinista(self):
        return "fisico determinista"

    """
    Se tiene una lista, si la lista tiene a dos personas se sacan estas dos
    primeras, se mueven a un lugar juntas y conversan durante el tiempo
    especificado, si la lista es impar dos conversan otra espera y si no se
    agrega nadie cambia de desicion.
    """

    def conversar(self):
        length = len(self.quiere_conversar)
        if len(self.quiere_conversar) > 1:
            cliente = self.quiere_conversar.pop(length - 1)
            if self.quiere_conversar[0].quiere_ == True and \
                    self.quiere_conversar[0] != cliente:
                nuevo = self.quiere_conversar.pop()
                self.conversando.append((nuevo.nombre, cliente.nombre))
                return nuevo
        else:
            return "conversar"
