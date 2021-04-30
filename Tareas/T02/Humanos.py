from random import uniform, random
from gui.entities import Entity, Human
from Acciones import *
from names import *
from math import pi
from Juegos import *
from random import normalvariate
from Parametros import *
from random import choices

acciones = Acciones()

class Clientes(Human):

    def __init__(self, personalidad):
        super().__init__(personalidad)
        # Estas son properties ya que tienen condiciones de no ser menores a 0
        self.personalidad = personalidad
        self.destino = None
        self.dinero = 1
        self.dinero_entrada = self.dinero
        self.lucidez = 0
        self.suerte = 0
        self.sociabilidad = 0
        self.ansiedad = 0
        self.stamina = 0
        self.deshonestidad = 0
        self.tiempo = 0
        self.tiempo_espera = 0
        self.prediciendo = False
        self.nombre = random.choice([get_first_name("male"), get_first_name(
            "female")])
        self.apellido = get_last_name()
        self.edad = random.randrange(18, 90)
        self.acciones = acciones
        self.accion = None
        self.probabilidad_ganar = 0
        self.estado = False
        self.get_x = 0
        self.get_y = 0
        self.quiere_ = False
        self.a_conversado = 0
        self.pillado = False
        self.coludido = False
        self.sin_dinero = False
        self.pozo_casino = 0
        self.tick_de_llegada = 0
        self.tick_de_salida = 0

    # Dinero
    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, value):
        if value < 0:
            self._dinero = 0
        else:
            self._dinero = value

    # Lucidez
    @property
    def lucidez(self):
        return self._lucidez

    @lucidez.setter
    def lucidez(self, value):
        if value < 0:
            self._lucidez = 0
        elif value > 1:
            self._lucidez = 1
        else:
            self._lucidez = value

    # Ansiedad
    @property
    def ansiedad(self):
        return self._ansiedad

    @ansiedad.setter
    def ansiedad(self, value):

        """
        Este codigo no funciona, tengo que saber como implementarlo mejor,
        error entre el self.dinero ya que siempre da 0
        if self.dinero > self.dinero_entrada * 2 or self.dinero < \
                self.dinero_entrada / 5:
            print(self.dinero, self.dinero_entrada)
            self._ansiedad = self.ansiedad * 1.25
        else:
            self._ansiedad = value
        """

        if value < 0:
            self._ansiedad = 0

        elif value > 1:
            self._ansiedad = 1
        else:
            self._ansiedad = value

    # Suerte
    @property
    def suerte(self):
        return self._suerte

    @suerte.setter
    def suerte(self, value):
        if value < 0:
            self._suerte = 0
        elif value > 1:
            self._suerte = 1
        else:
            self._suerte = value

    # Sociabilidad
    @property
    def sociabilidad(self):
        return self._sociabilidad

    @sociabilidad.setter
    def sociabilidad(self, value):
        if value < 0:
            self._sociabilidad = 0
        elif value > 1:
            self._sociabilidad = 1
        else:
            self._sociabilidad = value

    # Stamina
    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0:
            self._stamina = 0
        elif value > 1:
            self._stamina = 1
        else:
            if self.dinero < 0:
                self._stamina = 0
            else:
                self._stamina = value

    # Deshonestidad
    @property
    def deshonestidad(self):
        return self._deshonestidad

    @deshonestidad.setter
    def deshonestidad(self, value):
        if value < 0:
            self._deshonestidad = 0
        elif value > 1:
            self._deshonestidad = 1
        else:
            self._deshonestidad = value

    @property
    def probabilidad_ganar(self):
        return self._probabilidad_ganar

    @probabilidad_ganar.setter
    def probabilidad_ganar(self, value):
        if value < 0:
            self._probabilidad_ganar = 0
        elif value > 1:
            self._probabilidad_ganar = 1
        else:
            self._probabilidad_ganar = value

    @property
    def prob_retirarse(self):
        return 1 - self.stamina

    @property
    def prob_jugar(self):
        return min(self.ansiedad, (1 - self.prob_retirarse))

    @property
    def prob_participar(self):
        return min(self.sociabilidad, (1 - self.prob_retirarse -
                                       self.prob_jugar))

    @property
    def prob_ir_insta(self):
        return 1 - (self.prob_retirarse + self.prob_participar
                                  + self.prob_jugar)

    @property
    def accion(self):
        return self.accion_

    @accion.setter
    def accion(self, value):
        if self.dinero <= 0:
            self.accion_ = "me retiro"
            self.sin_dinero = True
        else:
            self.accion_ = value
            self.sin_dinero = False

    def jugar(self):

        self.apuesta_inicial = (1 + theta + self.ansiedad) * 1

        if self.destino.estado == True and self.accion == "ruleta":
            self.destino.visitas += 1

            for i in self.destino.personal:
                if i.coludido == True and self.coludido == True:
                    self.probabilidad_ganar += self.probabilidad_ganar * \
                                               kappa  / 100

            if self.prediciendo == True:
                self.probabilidad_ganar += psi / 100

            self.destino.numero_color = random.choice(["color", "numero"])
            self.destino.color = random.choice(["verde", "negro", "rojo"])
            self.probabilidad_ganar = self.destino.probabilidad_juego_ruleta + \
                                      0.2 * self.suerte - 0.1

            if random.random() <= self.probabilidad_ganar:
                self.dinero += self.apuesta_inicial * self.destino.ganancia
                self.destino.perdida += self.apuesta_inicial * \
                                        self.destino.ganancia
            else:

                self.destino.pozo_casino += self.apuesta_inicial * \
                                            self.destino.ganancia
        else:
            if self.destino.estado == True:
                self.destino.visitas += 1
                self.probabilidad_ganar = self.destino.probabilidad_tragamoneda\
                                          + 0.2 * self.suerte - 0.1

                if random.random() <= self.probabilidad_ganar:
                    self.dinero += self.destino.pozo
                    self.destino.perdida += self.destino.pozo
                    self.destino.pozo = 0
                else:
                    self.destino.pozo += self.apuesta_inicial * 0.9
                    self.destino.pozo_casino += self.apuesta_inicial * 0.1

        if self.tiempo < int(self.tiempo_espera) and self.destino.estado == \
                True and self.prediciendo == True and self.personalidad == \
                "kibitzer":
            self.tiempo += 1
            self.estado = True
            self.accion = "ruleta"

        else:
            self.tiempo = 0
            self.estado = False

    def participar(self, personalidad):

        value = self.lucidez + self.sociabilidad - self.ansiedad
        if value >= 0.1:
            self.duracion = value * pow(pi, 2)
        else:
            self.duracion = 0.1 * pow(pi, 2)

        if self.accion == "hablar con tini":
            self.dinero -= 20
            self.stamina -= eta
            self.pozo_casino += 20
            self.tiempo = 0
            self.estado = False
            self.coludido = True

        elif self.accion == "conversar":
            self.acciones.quiere_conversar.append(self)
            # Agregar a una lista de gente conversando y chequear si se puede
            if self.nombre not in self.acciones.quiere_conversar:
                self.quiere_ = True
                nuevo = self.acciones.conversar()

                if nuevo == "conversar" or nuevo == None:
                    self.estado = True
                    self.tiempo_espera = delta

                else:
                    self.a_conversado += 1
                    nuevo.a_conversado += 1
                    self.estado = True
                    self.tiempo_espera = min(nuevo.duracion, self.duracion)

        elif self.accion == "fisico determinista":
            if self.personalidad == "kibitzer" and self.a_conversado >= 0:
                desicion = random.choice(["predigo", "no"])
                if desicion == "predigo":
                    self.estado = True
                    self.accion = "ruleta"
                    self.tiempo_espera = nu
                    self.prediciendo = True
                else:
                    self.estado = False

        # esto va pasar para cuando este esperando la conversacion o
        # conversando

        if self.tiempo < int(self.tiempo_espera) and self.estado == True and \
                self.accion != "fisico determinista":
            self.tiempo += 1
            self.estado = True

        elif self.accion != "fisico determinista":
            self.tiempo = 0
            self.ansiedad -= epsilon / 100
            self.deshonestidad += chi
            self.estado = False

    def retirarse(self):
        self.estado = True
        self.deleteLater()
        self.accion = "me retiro"

    def instalacion(self):


        if self.destino.estado == True:

            self.destino.visitas += 1

            if self.accion == "restobar":
                opciones = ["bebidas", "comida"]
                pedido = random.choice(opciones)
                self.dinero -= 2
                self.destino.pozo_casino += 0

                # defino una duracion
                self.tiempo_espera = 52 - len(self.destino.personal)

                if pedido == "bebidas":
                    self.lucidez -= 0.2
                    self.ansiedad -= 0.5
                    self.stamina += 0.3
                else:
                    self.lucidez += 0.1
                    self.ansiedad += 0.2

            elif self.accion == "baño":
                self.dinero -= 0.2
                self.destino.pozo_casino += 0.2
                self.ansiedad -= 0.1
                self.tiempo_espera = normalvariate(3 * (1 - self.lucidez), 2)

            elif self.accion == "tarot":
                self.dinero -= 10
                self.destino.pozo_casino += 10
                self.tiempo_espera = normalvariate(3, 5)

                """
                De este random elige que fué lo que le predijieron por lo 
                tanto se hace un random de que propiedad aumenta. Yo decidi 
                que cualquiera de los dos aumentara en 0.1 con igualdad de  
                probabilidad de ocurrencia
                """
                que_pasa = random.choice(["suerte", "irme"])
                if que_pasa == "suerte":
                    self.suerte += 0.1
                else:
                    self.stamina -= 0.1

        if self.tiempo < int(self.tiempo_espera) and self.destino.estado == \
                True:
            self.tiempo += 1
            self.estado = True

        else:
            self.tiempo = 0
            self.estado = False

    def tomar_desicion(self, lista_ru, lista_tra, resto, lista_ta, baño):

        """
        Obtener aleatoriamente una accion que tiene una probabilidad asignada:
        https://stackoverflow.com/questions/4265988/generate-random-numbers-with
        -a-given-numerical-distribution
        """

        acciones = [self.acciones.participar(self.personalidad),
                    self.acciones.ir_instalacion(),self.acciones.retirarse(),
                    self.acciones.jugar()]

        probabilidades = [self.prob_participar, self.prob_ir_insta,
                          self.prob_retirarse, self.prob_jugar]

        self.accion = choices(acciones, probabilidades)[0]

        return self.obtener_destino(lista_ru, lista_tra, resto, lista_ta, baño)

    def obtener_destino(self, lista_ru, lista_tra, resto, lista_ta, baño):

        if self.accion == "ruleta":
            self.destino = random.choice(lista_ru)
            self.get_x = self.destino.x
            self.get_y = self.destino.y
            return self.quihagoahora()

        elif self.accion == "tragamonedas":
            self.destino = random.choice(lista_tra)
            self.get_x = self.destino.x
            self.get_y = self.destino.y
            return self.quihagoahora()

        elif self.accion == "restobar":
            self.destino = resto
            self.get_x = self.destino.x
            self.get_y = self.destino.y
            return self.quihagoahora()

        elif self.accion == "tarot":
            self.destino = random.choice(lista_ta)
            self.get_x = self.destino.x
            self.get_y = self.destino.y
            return self.quihagoahora()

        elif self.accion == "baño":
            self.destino = baño
            self.get_x = self.destino.x
            self.get_y = self.destino.y
            return self.quihagoahora()

        elif self.accion == "me retiro" or self.pillado == True:
            return self.retirarse()

        else:
            # definir un pozo!
            if self.accion == "fisico determinista":
                self.destino = random.choice(lista_ru)
                self.get_x = self.destino.x
                self.get_y = self.destino.y
            return self.participar(self.personalidad)

    def quihagoahora(self):

        if [self.x, self.y] == [self.get_x, self.get_y] and \
                self.accion != "conversar":
            self.estado = True
            if self.accion == "ruleta":
                return self.jugar()
            elif self.accion == "tragamonedas":
                return self.jugar()
            elif self.accion == "restobar" or self.accion == "baño" or \
                    self.accion == "tarot":
                return self.instalacion()
        elif self.accion == "conversar":
            return self.participar(self.personalidad)
        elif self.accion != "me retiro":
            self.estado = "en camino"
            return self.caminar()

    def caminar(self):

        if self.x < self.get_x:
            self.x += 1
        elif self.x > self.get_x:
            self.x -= 1
        if self.y < self.get_y:
            self.y += 1
        elif self.y > self.get_y:
            self.y -= 1
        if [self.x, self.y] == [self.get_x, self.get_y]:
            self.estado = True