from random import uniform, random
from Clientes import Millonario, Ganador, Ludopata, Dieciochero, Kibitzer
from Juegos import *
from Trabajadores import *
import os
import gui
from random import random, choice
from Parametros import p
from math import ceil

_PATH = os.path.dirname(os.path.abspath(__file__))

gui.init()
gui.set_size(773, 485)

class Main:
    """
    Para hacer esta clase me base en el material complementario
    """

    def __init__(self):
        self.ticks = 0
        self.list_personajes = []
        self.list_inst = []
        self.list_tragamonedas = []
        self.list_ruletas = []
        self.restobar = ""
        self.baño = None
        self.lista_tarot = []
        self.dealers = []
        self.mr_t = []
        self.bartender = []
        self.ticks = 0
        self.dias_simulacion = 0

        self.suma_pozo_casino = 0
        self.suma_kibitzer = 0
        self.suma_ganador = 0
        self.suma_dieciochero = 0
        self.suma_ludopata = 0
        self.suma_millonario = 0

        self.suma_dinero_kibitzer = 0
        self.suma_dinero_ganador = 0
        self.suma_dinero_dieciochero = 0
        self.suma_dinero_ludopata = 0
        self.suma_dinero_millonario = 0

        self.suma_estadia_kibitzer = 0
        self.suma_estadia_ganador = 0
        self.suma_estadia_dieciochero = 0
        self.suma_estadia_ludopata = 0
        self.suma_estadia_millonario = 0

        self.suma_fisic = 0

        self.suma_retiro_pillado = 0
        self.suma_retiro_normal = 0
        self.suma_retiro_plata = 0

        self.lista_personasxjuego = []
        self.lista_tiempoxinstalacion = []

    def agrego_trabajador(self, tipo):

        if tipo == "bartender":
            trabajador = Bartender()
            trabajador.juego_asignado = self.restobar
            self.bartender.append(trabajador)
            self.restobar.personal += [trabajador]
            self.restobar.estado_()

        elif tipo == "mr_t":
            trabajador = Mr_T()
            for i in self.lista_tarot:
                if len(i.personal) < 1:
                    trabajador.juego_asignado = i
                    i.personal += [trabajador]
                    i.estado_()
                    self.mr_t.append(trabajador)
                    break

        else:
            trabajador = Dealer()
            for i in self.list_tragamonedas + self.list_ruletas:
                if len(i.personal) < 16 and i.nombre == "tragamonedas":
                    trabajador.juego_asignado = i
                    i.personal += [trabajador]
                    i.estado_()
                    self.dealers.append(trabajador)
                    break

                elif len(i.personal) < 1:
                    trabajador.juego_asignado = i
                    i.personal += [trabajador]
                    i.estado_()
                    self.dealers.append(trabajador)
                    break

    def agrego_cliente(self):
        if random() <= p:
            lista_elegir = [Millonario(), Kibitzer(), Ganador(),
                            Dieciochero(), Ludopata()]
            personaje = choice(lista_elegir)
            personaje.tick_de_llegada = self.ticks
            self.list_personajes.append(personaje)
            gui.add_entity(personaje)

    def qui_hacen(self):

        for i in self.list_personajes:
            if i.estado == False:
                i.tomar_desicion(self.list_ruletas, self.list_tragamonedas,
                                 restobar, self.lista_tarot, baño)
            elif i.estado == "en camino" and i.accion != "me retiro":
                i.caminar()

            elif i.estado == True:
                i.quihagoahora()

            if i.accion == "me retiro":
                i.tick_de_salida = self.ticks

            if i.accion != "me retiro":
                if i.dinero > 2 * i.dinero_entrada or i.dinero < \
                        i.dinero_entrada / 5:
                    i.stamina = i.stamina * 1.25

    def qui_hacen_trabajadores(self):

        """
        A qui veo que es lo que van a hacer los trabajadores si no van a
        trabajar tengo que llamar a la funcion que actualice el estado de la
        instalacion/juego para se verifique si sigue o no abierta
        """

        for i in self.mr_t:
            if i.trabajando == True and i.t_trabajo > i.t_trabajado:
                i.trabajar()

            elif i.trabajando == True and i.t_trabajo <= i.t_trabajado:
                i.cuando_vuelvo()
                i.descansar()

            elif i.trabajando == False and i.t_descanso > i.t_descansado:
                i.descansar()

            elif i.trabajando == False and i.h_prox_turno <= (
                    i.t_trabajado + i.t_descansado):
                i.t_trabajado = 0
                i.t_descansado = 0
                i.trabajar()

            else:
                i.descansar()

        for i in self.dealers:
            if i.trabajando == True and i.t_trabajo > i.t_trabajado:
                i.trabajar(self.list_personajes)

            elif i.trabajando == True and i.t_trabajo <= i.t_trabajado:
                i.cuando_vuelvo()
                i.descansar()

            elif i.trabajando == False and i.t_descanso > i.t_descansado:
                i.descansar()

            elif i.trabajando == False and i.h_prox_turno <= (
                    i.t_trabajado + i.t_descansado):
                i.t_trabajado = 0
                i.t_descansado = 0
                i.trabajar(self.list_personajes)

            else:
                i.descansar()

        for i in self.bartender:

            if i.trabajando == True and i.t_trabajo > i.t_trabajado:
                i.trabajar()

            elif i.trabajando == True and i.t_trabajo <= i.t_trabajado:
                i.cuando_vuelvo()
                i.descansar()

            elif i.trabajando == False and i.t_descanso > i.t_descansado:
                i.descansar()

            elif i.trabajando == False and i.h_prox_turno <= (
                    i.t_trabajado + i.t_descansado):
                i.t_trabajado = 0
                i.t_descansado = 0
                i.trabajar()
            else:
                i.descansar()

    def actualizar_estado(self):

        for i in self.list_ruletas:
            i.estado_()
        for i in self.list_tragamonedas:
            i.estado_()
        for i in self.lista_tarot:
            i.estado_()

        self.restobar.estado_()

        for i in self.lista_tarot + [self.restobar] + [self.baño]:
            if i.estado == False:
                i.no_funcionando += 1

    def suma_ticks(self):
        self.ticks += 1

    def imprimir(self):

        if self.suma_kibitzer > 0:
            promedio_k = self.suma_dinero_kibitzer / self.suma_kibitzer
            t_promedio_k = self.suma_estadia_kibitzer / self.suma_kibitzer

        else:
            promedio_k = 0
            t_promedio_k = 0

        if self.suma_ganador > 0:
            promedio_g = self.suma_dinero_ganador / self.suma_ganador
            t_promedio_g = self.suma_estadia_ganador / self.suma_ganador
        else:
            promedio_g = 0
            t_promedio_g = 0

        if self.suma_dieciochero > 0:
            promedio_d = self.suma_dinero_dieciochero / self.suma_dieciochero
            t_promedio_d = self.suma_estadia_dieciochero / self.suma_dieciochero
        else:
            promedio_d = 0
            t_promedio_d = 0

        if self.suma_ludopata > 0:
            promedio_l = self.suma_dinero_ludopata / self.suma_ludopata
            t_promedio_l = self.suma_estadia_ludopata / self.suma_ludopata
        else:
            promedio_l = 0
            t_promedio_l = 0

        if self.suma_millonario > 0:
            promedio_m = self.suma_dinero_millonario / self.suma_millonario
            t_promedio_m = self.suma_estadia_millonario / self.suma_millonario
        else:
            promedio_m = 0
            t_promedio_m = 0

        promedio_f = (promedio_k + promedio_g + promedio_d + promedio_l +
                      promedio_m) / 5
        t_promedio_f = (t_promedio_k + t_promedio_g + t_promedio_d +
                        t_promedio_l + t_promedio_m) / 5

        ganancia_promedio = self.suma_pozo_casino / ceil(main.ticks / (60 * 24))
        porcentaje_fis = 100 * (self.suma_fisic / (self.suma_kibitzer +
                                                   self.suma_ganador +
                                                   self.suma_dieciochero +
                                                   self.suma_ludopata +
                                                   self.suma_millonario))

        print("--------------------------------------------------------------\n"
              "                  Resumen Estadíticas                   \n"
              "--------------------------------------------------------------\n"
              "\n"
              "   i)  Dinero promedio final -->  " + str(promedio_f) + "\n\n"
                                                                       "  ii)  Dinero promedio final por cliente -->\n\n"
                                                                       "       Kibitzer    --> " + str(
            promedio_k) + "   \n"
                          "       Ganador     --> " + str(promedio_g) + "  \n"
                                                                        "       Dieciochero --> " + str(
            promedio_d) + "  \n"
                          "       Ludopata    --> " + str(promedio_l) + "  \n"
                                                                        "       Millonario  --> " + str(
            promedio_m) + "  \n\n"

                          " iii)  Tiempo promedio de estadía --> " + str(
            t_promedio_f) +
              "\n\n"
              "  iv)  Tiempo promedio de estadía por cliente -->\n\n"
              "       Kibitzer    --> " + str(t_promedio_k) + "   \n"
                                                              "       Ganador     --> " + str(
            t_promedio_g) + "  \n"
                            "       Dieciochero --> " + str(
            t_promedio_d) + "  \n"
                            "       Ludopata    --> " + str(
            t_promedio_l) + "  \n"
                            "       Millonario  --> " + str(
            t_promedio_m) + "  \n\n"
                            "   v)  Ganancia en promedio del casino por día --> " +
              str(ganancia_promedio) + "\n\n"
                                       "  vi)  Juego que generó mas ganancias --> " +
              str(self.juego_menor_perdida) + "\n\n"
                                              " vii)  Porcentaje de personas que 'Contaron cartas' --> " +
              str(porcentaje_fis) + "%\n\n"
                                    "viii)  Razones de retirada (+ Porcentaje) --> \n\n"
                                    "       Sin dinero      --> " + str(
            self.suma_retiro_plata) +
              "\n"
              "       Hechado         --> " + str(self.suma_retiro_pillado) +
              "\n"
              "       Desición propia --> " + str(self.suma_retiro_normal) +
              "\n\n"
              "  ix)  Tiempo sin funcionar de cada instalacion -->\n")

        for i in self.lista_tiempoxinstalacion:
            print("       La intalación {} no funcionó durante {} minutos "
                  "durante la simulación".format(i[0], i[1]))

        print(
            "\n   x)  Número de personas que visitó cada juego por día -->\n")

        for i in self.lista_personasxjuego:
            print("       {} personas visitaron el juego {}".format(i[1], i[0]))

    def estadisticas(self):

        """
        Aqui calculo las estadísticas de un día
        """

        for i in self.list_personajes:
            if i.estado != "me retiro" and i.tipo == "kibitzer":
                self.suma_kibitzer += 1
                self.suma_dinero_kibitzer += i.dinero

                if i.tick_de_salida != 0:
                    self.suma_estadia_kibitzer += (i.tick_de_salida -
                                                   i.tick_de_llegada)
                if i.prediciendo == True:
                    self.suma_fisic += 1

            elif i.estado != "me retiro" and i.tipo == "ganador":
                self.suma_ganador += 1
                self.suma_dinero_ganador += i.dinero

                if i.tick_de_salida != 0:
                    self.suma_estadia_ganador += (i.tick_de_salida -
                                                  i.tick_de_llegada)

            elif i.estado != "me retiro" and i.tipo == "dieciochero":
                self.suma_dieciochero += 1
                self.suma_dinero_dieciochero += i.dinero

                if i.tick_de_salida != 0:
                    self.suma_estadia_dieciochero += (i.tick_de_salida -
                                                      i.tick_de_llegada)

            elif i.estado != "me retiro" and i.tipo == "ludopata":
                self.suma_ludopata += 1
                self.suma_dinero_ludopata += i.dinero
                if i.tick_de_salida != 0:
                    self.suma_estadia_ludopata += (i.tick_de_salida -
                                                   i.tick_de_llegada)

            elif i.estado != "me retiro" and i.tipo == "millonario":
                self.suma_millonario += 1
                self.suma_dinero_millonario += i.dinero

                if i.tick_de_salida != 0:
                    self.suma_estadia_millonario += (i.tick_de_salida -
                                                     i.tick_de_llegada)
            if i.pillado == True:
                self.suma_retiro_pillado += 1

            elif i.sin_dinero == True:
                self.suma_retiro_plata += 1

            elif i.accion == "me retiro":
                self.suma_retiro_normal += 1

            """
            Sumo el pozo de las ganancias de as instalaciones 
            """
            self.suma_pozo_casino += i.pozo_casino

        for i in self.lista_tarot + self.list_ruletas + \
                 self.list_tragamonedas + [self.baño] + [self.restobar]:
            self.suma_pozo_casino += i.pozo_casino

        """
        Sumo lo que quedo en el pozo
        """

        for i in self.list_tragamonedas:
            self.suma_pozo_casino += i.pozo

        for i in self.list_tragamonedas + self.list_ruletas:
            self.lista_personasxjuego.append((i.id, i.visitas))

        for i in self.lista_tarot + [self.restobar] + [self.baño]:
            self.lista_tiempoxinstalacion.append((i.id, i.no_funcionando))

        for i in self.list_tragamonedas + self.list_ruletas:
            for m in self.list_tragamonedas + self.list_ruletas:
                if (i.pozo - i.perdida) >= (m.pozo - m.perdida) \
                        and (i.pozo - i.perdida) != 0:
                    self.juego_menor_perdida = i.id
                else:
                    self.juego_menor_perdida = None


main = Main()

baño = Restroom()
restobar = Restobar()

lista_ruletas = []
lista_tragamonedas = []
lista_tarot = []

for i in range(1, 5):
    var6 = Ruleta()
    main.list_ruletas.append(var6)
    lista_ruletas.append(var6)

for i in range(1, 4):
    var7 = Tragamonedas()
    main.list_tragamonedas.append(var7)
    lista_tragamonedas.append(var7)

for i in range(1, 4):
    var8 = Tarot()
    main.lista_tarot.append(var8)
    lista_tarot.append(var8)

for i in lista_ruletas:
    gui.add_entity(i)
    i.estado = False

for i in lista_tragamonedas:
    gui.add_entity(i)
    i.estado = False

for i in lista_tarot:
    gui.add_entity(i)
    i.estado = False

main.baño = baño
main.restobar = restobar
gui.add_entity(baño)
gui.add_entity(restobar)

main.dias_simulacion = float(input("Cuanto tiempo en DIAS quiere simular:\n"))


def tick():
    """
    Esta es la función Tick(), primero en las primeras jornadas voy poniendo
    a mi personal pero al mismo tiempo llamo para ver si estan en turno o no
    """
    main.suma_ticks()

    if len(main.dealers) < 62:
        main.agrego_trabajador("dealer")

    if len(main.mr_t) < 3:
        main.agrego_trabajador("mr_t")

    if len(main.bartender) < 55:
        main.agrego_trabajador("bartender")

    main.qui_hacen_trabajadores()
    main.agrego_cliente()
    main.qui_hacen()
    main.actualizar_estado()

    if main.ticks >= main.dias_simulacion * 60 * 24:
        main.estadisticas()
        main.imprimir()
        exit()


gui.run(tick, 50)