from Grafo import *
from copy import *
from Consultas import *


def consultas(Grafo, tamaño, sistema):
    operacion = input("Menu:\n"
                      "Energia total consumida en una comuna --> 1\n"
                      "Clientes con mayor consumo --> 2\n"
                      "Clientes con menor consumo --> 3\n"
                      "Consumo de una subestación --> 4\n")

    if operacion == "1":
        str = input("Ingrese la comuna que quiere consultar "
                    "(recuerde que debe ir en mayúsculas\n")
        print(energia_total_comuna(str, tamaño, sistema))

    elif operacion == "2":
        print(consumo_casa("mayor", Grafo))

    elif operacion == "3":
        print(consumo_casa("menor", Grafo))

    else:
        tipo = input("Indique el tipo de subestacion que quiere "
                     "consultar\n")
        id = input("Indique el id de la subestacion que quiere consultar\n")
        consumo_sub(tamaño, id, tipo, sistema)

    resp = input("¿Desea hacer otra consulta? si/no\n")

    if resp == "si":
        return consultas(Grafo, tamaño, sistema)

    else:
        return menu(Grafo, tamaño, sistema)


def modificar_red(Grafo, tamaño, sistema, estado = None, Grafo_aux = None):

    operacion = input("\nMenu:\n"
                      "Agregar nodo --> 1\n"
                      "Remover nodo --> 2\n"
                      "Agregar arista --> 3\n"
                      "Remover arista --> 4\n")

    if operacion == "1":
        id_destino = input("\nIngrese el id de origen\n")
        tipo_destino = input("\nIngrese que tipo es el origen\n")

        resp = input("\n¿Quieres conectarlo a otro nodo? si/no")

        if resp == "si":
            conexion = "si"
            id_origen = input("\nIngrese el id de destino\n")
            tipo_origen = input("\nIngrese que tipo es el destino\n")
            distancia = input("\nIngresa la distancia entre ellos")

        else:
            conexion = "no"
            id_origen = None
            tipo_origen = None
            distancia = None

        Grafo.check_nodo_add(tipo_destino, id_destino, conexion,
                             tipo_origen, id_origen, distancia)

    elif operacion == "2":
        id = input("\nIngrese el id de origen\n")
        tipo = input("\nIngrese que tipo es el origen\n")
        Grafo.check_nodo_remove(tipo, id)

    elif operacion == "3":
        id_origen = input("\nIngrese el id de origen\n")
        tipo_origen = input("\nIngrese que tipo es el origen\n")
        id_destino = input("\nIngrese el id de destino\n")
        tipo_destino = input("\nIngrese que tipo es el destino\n")
        distancia = input("\nIngresa la distancia entre ellos")
        Grafo.agregar_arista(id_origen, tipo_origen, id_destino,
                             tipo_destino, distancia)

    else:
        id_origen = input("\nIngrese el id de origen\n")
        tipo_origen = input("\nIngrese que tipo es el origen\n")
        id_destino = input("\nIngrese el id de destino\n")
        tipo_destino = input("\nIngrese que tipo es el destino\n")

        Grafo.remover_arista(id_origen, tipo_origen, id_destino,
                             tipo_destino)
    resp = input("\n¿Quieres hacer otra modificación?")

    if resp == "si":
        return modificar_red(Grafo, tamaño, sistema, estado, Grafo_aux)

    elif estado == None and resp == "no":
        return menu(Grafo, tamaño, sistema)
    else:
        return simulacion(Grafo, tamaño, sistema, Grafo_aux)


def menu_simulacion(Grafo, tamaño, sistema, Grafo_aux):
    print(".........................")
    print("Bienvenido a la versión de simulación de Electromatic")
    print(".........................\n")
    estado = "simulando"
    modificar_red(Grafo, tamaño, sistema, estado, Grafo_aux)


def simulacion(Grafo, tamaño, sistema, Grafo_aux):
    resp1 = input("¿Desea volver a la version no simulada? si/no")

    if resp1 == "si":
        resp2 = input("¿Quieres guardar esta version o volver a la "
                      "original? 1: original , 2: modificada")
        if resp2 == "1":
            return menu(Grafo_aux, tamaño, sistema)
        else:
            return menu(Grafo, tamaño, sistema)
    else:
        return menu_simulacion(Grafo, tamaño, sistema, Grafo_aux)


def menu_basico2():
    tamaño = input("Indique que el tamaño de la base de datos\n")
    print(".........................\n")
    sistema = input("Indique que sistema quiere quiere consultar\n")

    if sistema != "SING" and sistema != "SIC" and sistema != "SEA" \
            and sistema != "SEM":
        raise InvalidQuery("No existe un sistema bajo ese nombre")

    Grafo = Graph(sistema)

    return menu(Grafo, tamaño, sistema)


def menu(Grafo, tamaño, sistema):
    estado = "normal"
    operacion = input("\nMenu:\n"
                      "Modificar la red --> 1\n"
                      "Simular --> 2\n"
                      "Hacer una consulta --> 3\n"
                      "Quiere estudiar otro sistema --> 4\n")

    if operacion != "4":
        Grafo.cargar_archivo(tamaño, "centrales_elevadoras")
        Grafo.cargar_archivo(tamaño, "casas_distribucion")
        Grafo.cargar_archivo(tamaño, "distribucion_transmision")
        Grafo.cargar_archivo(tamaño, "transmision_elevadoras")
        Grafo.cargar_archivo(tamaño, "casas_casas")
        Grafo.demanda_real()
        Grafo.flujo()

    if operacion == "1":
        return modificar_red(Grafo, tamaño, sistema)
    elif operacion == "2":
        Grafo_aux = copy(Grafo)
        return menu_simulacion(Grafo, tamaño, sistema, Grafo_aux)
    elif operacion == "3":
        return consultas(Grafo, tamaño, sistema)
    else:
        return menu_basico2()


def menu_basico():
    tamaño = input("\nIndique el tamaño de la base de datos\n")
    print(".........................\n")
    sistema = input("Indique que sistema quiere quiere consultar\n")

    if sistema != "SING" and sistema != "SIC" and sistema != "SEA" \
            and sistema != "SEM":
        raise InvalidQuery("No existe un sistema bajo ese nombre")

    Grafo = Graph(sistema)
    return menu(Grafo, tamaño, sistema)


try:
    print(".........................")
    print("Bienvenido a Electromatic")
    print(".........................\n")
    menu_basico()

except ElectricalOverload as err1:
    print("ElectricalOverload " + str(err1))

except ForbiddenAction as err2:
    print("ForbiddenAction" + str(err2))

except TypeError as err3:
    print("TypeError: " + str(err3))

except ValueError as err4:
    print("ValueError: " + str(err4))

except InvalidQuery as err5:
    print("InvalidQuery: " + str(err5))

finally:
    print("\nLo sentimos :(")
    print("\nSu input ha sido invalido, será redirigido al menu inicial")
    menu_basico()





