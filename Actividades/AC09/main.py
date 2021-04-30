import threading as thr
import time
from itertools import chain
from random import randint , random
from itertools import count


def desencriptar(nombre_archivo):
    """
    Esta simple (pero útil) función te permite descifrar un archivo encriptado.
    Dado el path de un archivo, devuelve un string del contenido desencriptado.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        murcielago, numeros = "murcielago", "0123456789"
        dic = dict(chain(zip(murcielago, numeros), zip(numeros, murcielago)))
        return "".join(
            dic.get(char, char) for linea in archivo for char in linea.lower())


class Hacker(thr.Thread):

    id_gen = count()  # Generamos ID unico para cada Hacker
    id_nombre = (i for i in ["Slytherin", "Griffindor", "Ravenclaw",
                             "Huslehuff"])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hacker_id = next(self.id_gen)
        self.nombre_eq = next(self.id_nombre)
        self.daemon = True
        self.fired_signal = thr.Event()
        self.desencriptado_ = False

    def run(self):
        time.sleep(randint(4, 12))
        desencriptar("pista.txt")
        print("En el equipo {} ya termino de desencriptar".format(
            self.id_nombre))
        self.desencriptado_ = True
        self.fired_signal.set()


NebiLongbottom = thr.Lock()


class Cracker(thr.Thread):

    def __init__(self, hacker: Hacker, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hacker = hacker
        self.daemon = True
        self.fired_signal = thr.Event()  # señal para avisar al estratega
        self.id_gen = count()
        self.lineas_escritas = 0
        self.nombre_eq = hacker.nombre_eq

    def Atack(self):
        with NebiLongbottom:
            NebiLongbottom.acquire()
            print("NebiLongbottom esta ayudando a el equipo {}".format(
                self.hacker.id_nombre))
            time.sleep(random.randint(1, 3))
            print("NebiLongbottom termino de ayudar  a el equipo {}".format(
                self.hacker.id_nombre))
            NebiLongbottom.release()

    def run(self):
        while self.lineas_escritas < 50:
            time.sleep(1)
            self.lineas_escritas += int(randint(5, 15))
            if random() <= 0.2:
                self.Atack()

        # cuando termina de hacer esto manda la señal
        self.fired_signal.set()


class Equipo(thr.Thread):
    def __init__(self, cracker: Cracker, hacker: Hacker, signal1: thr.Event,
                 signal2 : thr.Event, señal_mision: thr.Event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cracker = cracker
        self.hacker = hacker
        self.daemon = True
        self.fired_signal1 = signal1
        self.fired_signal2 = signal2
        self.señal_mision = señal_mision
        self.terminamos = False
        self.nombre_eq = cracker.nombre_eq
        self.lineas = cracker.lineas_escritas
        self.desencriptado = hacker.desencriptado_

    def run(self):
        self.cracker.start()
        self.hacker.start()
        self.fired_signal1.wait()  # espera la señal del pilo
        self.fired_signal2.wait()
        self.terminamos = True
        self.señal_mision.set()


class Mision(thr.Thread):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equipos = []
        self.hackers = []
        self.crackers = []
        self.señal_mision = thr.Event()
        self.equipo_ganador = ""

        for _ in range(4):
            self.hacker = Hacker()
            self.hackers.append(self.hacker)
            self.cracker = Cracker(self.hacker)
            self.crackers.append(self.cracker)
            self.equipo = Equipo(self.cracker, self.hacker,
                                      self.hacker.fired_signal,
                                self.cracker.fired_signal, self.señal_mision)
            self.equipos.append(self.equipo)
            self.equipo.start()


    def run(self):
        self.señal_mision.wait()

        """
        Reviso que equipo terminó de escribir las lineas
        """

        for i in self.equipos:
            if i.terminamos == True:
                print("El equipo ganador fue {}".format(i.nombre_eq))
                if i.desencriptado == True:
                    print("El hacker logró desncriptar")
                else:
                    print("El hacker no logró desncriptar")

                print("El cracker logró escibir {} lineas de código".format(i.lineas ))

            else:
                print("En el equipo {}".format(i.nombre_eq))

                if i.desencriptado == True:
                    print("El hacker logró desncriptar")
                else:
                    print("El hacker no logró desncriptar")

                print("El cracker logró escibir {} lineas de código".format(
                    i.lineas))


mision = Mision()

mision.start()
