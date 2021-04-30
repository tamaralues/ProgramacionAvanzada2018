from random import random, randrange, choice, triangular, normalvariate
from names import *
from Parametros import w
from math import ceil


class Trabajadores:

    def __init__(self):

        self.juego_asignado = None
        self.nombre = random.choice([get_first_name("male"), get_first_name(
            "female")])
        self.apellido = get_last_name()
        self.edad = random.randrange(21, 90)
        self.t_descanso = normalvariate(14, 5)
        self.t_descansado = 0
        self.t_trabajo = 0
        self.t_trabajado = 0
        self.trabajando = False
        self.h_prox_turno = 0
        self.tipo = ""
        self.descansado = 0

    # definimos que el tiempo de trabajo no puede ser mayor a 8
    @property
    def t_trabajo(self):
        return self.t_trabajo_

    @t_trabajo.setter
    def t_trabajo(self, value):
        if value >= 8 * 60:
            self.t_trabajo_ = 8 * 60
        elif value <= 6 * 60:
            self.t_trabajo_ = 6 * 60
        else:
            self.t_trabajo_ = value

    @property
    def t_descanso(self):
        return self.t_descanso_

    @t_descanso.setter
    def t_descanso(self, value):
        if value > 20 * 60:
            self.t_descanso_ = 20 * 60
        elif value > 8 * 60:
            self.t_descanso_ = 8 * 60
        else:
            self.t_descanso_ = value


class Dealer(Trabajadores):

    def __init__(self):
        super().__init__()
        self.juego_asignado = "id"
        self.t_trabajo = triangular(360, 540, 490)
        self.coludido = True
        self.tipo = "dealer"

    def pillar(self, lista_personas):
        for i in lista_personas:
            if i.destino != None:
                if i.destino.id == self.juego_asignado.id and \
                        i.accion != "me retiro":
                    if i.coludido == True or i.prediciendo == True:
                        if random.random() <= w:
                            i.pillado = True

    def tomar_desicion(self, lista):
        return self.trabajar(lista)

    def trabajar(self, lista):
        self.t_trabajado += 1
        self.trabajando = True
        self.pillar(lista)

    def descansar(self):
        self.t_descansado += 1
        self.trabajando = False

    def cuando_vuelvo(self):
        """
        Ya que el programa está en minutos, los divido por 60, saco las
        horas de la suma entre las horas de descanso y la trabajadas y las
        redondeo a el entero más grande, y despues las vuelvo a transformar en
        minutos
        """

        self.h_prox_turno = (ceil((self.t_descanso + self.t_trabajado) /
                                 60)) * 60
        self.t_descanso = normalvariate(14, 5) * 60
        self.t_trabajo = triangular(360, 540, 490)


class Bartender(Trabajadores):

    def __init__(self):
        super().__init__()
        self.tipo = "restobar"
        self.t_trabajo = triangular(360, 540, 540)

        # if's que asocien un juego en una posicion especifica, saquen el
        # no_juego de los availables para trabajar si es necesario y lo agrege a
        # los habilitados para su utilizacion para los clientes.

        # importar de opciones externas de que hacer con cierta probabilidad
        # cada un

    def trabajar(self):
        self.t_trabajado += 1
        self.trabajando = True

    def descansar(self):
        self.t_descansado += 1
        self.trabajando = False

    def cuando_vuelvo(self):
        """
        Ya que el programa está en minutos, los divido por 60, saco las
        horas de la suma entre las horas de descanso y la trabajadas y las
        redondeo a el entero más chico, y despues las vuelvo a transformar en
        minutos
        """
        self.h_prox_turno = (int((self.t_descanso + self.t_trabajado) /
                                 60)) * 60
        self.t_descanso = normalvariate(14, 5) * 60
        self.t_trabajo = triangular(360, 540, 540)


class Mr_T(Trabajadores):
    def __init__(self):
        super().__init__()
        self.t_trabajo = triangular(360, 500, 420)
        self.tipo = "mr.t"
        # importar de opciones externas de que hacer con cierta probabilidad
        # cada un

    def trabajar(self):
        self.t_trabajado += 1
        self.trabajando = True

    def descansar(self):
        self.t_descansado += 1
        self.trabajando = False

    def cuando_vuelvo(self):

        """
        Ya que el programa está en minutos, los divido por 60, saco las
        horas de la suma entre las horas de descanso y la trabajadas y las
        redondeo a el entero más chico, y despues las vuelvo a transformar en
        minutos
        """
        self.h_prox_turno = (int((self.t_descanso + self.t_trabajado) /
                                 60)) * 60
        self.t_descanso = normalvariate(14, 5) * 60
        self.t_trabajo = triangular(360, 500, 420)


