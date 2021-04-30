from Grafo import *
from Exceptions import *


def energia_total_comuna(str, tamaño, sistema, Grafo1):

    if sistema != "SING" and sistema != "SIC" and sistema != "SEA" and sistema\
            != "SEM":
        raise InvalidQuery("No existe un sistema bajo ese nombre")
    """
    Grafo1 = Graph(sistema)
    Grafo1.cargar_archivo(tamaño, "centrales_elevadoras")
    Grafo1.cargar_archivo(tamaño, "casas_distribucion")
    Grafo1.cargar_archivo(tamaño, "distribucion_transmision")
    Grafo1.cargar_archivo(tamaño, "transmision_elevadoras")
    Grafo1.cargar_archivo(tamaño, "casas_casas")
    Grafo1.demanda_real()
    Grafo1.flujo()
    """

    suma_demanda = 0
    suma_red = 0

    tamaño = Grafo1.nodos.keys().size()
    i = 0
    while i < tamaño:
        if Grafo1.nodos.keys().obtener(i).elemento.comuna == str:
            if Grafo1.nodos.keys().obtener(i).tipo != "elevadoras" and \
                    Grafo1.nodos.keys().obtener(i).tipo != "centrales" and \
                    Grafo1.nodos.keys().obtener(i).tipo != "transmision":
                suma_demanda += Grafo1.nodos.keys().obtener(i).potencia_recibida

        elif Grafo1.nodos.keys().obtener(i).tipo != "centrales":
             suma_red += Grafo1.nodos.keys().obtener(i).potencia_recibida
        i += 1

    if suma_red > 0:
        promedio = (suma_demanda/ suma_red )* 100

    else:
        promedio = 0

    return "El consumo total de la demanda en la comuna {} fue: {}\n Y el " \
           "porcentaje es {} %".format(str, suma_demanda, promedio)


def consumo_casa(tipo, Grafo1):

    if tipo != "mayor" and  tipo != "menor":
        raise InvalidQuery("La consulta no soporta un tipo de consulta "
                           "distinto a 'mayor' o 'menor'")

    valor_cmp_max = 0
    valor_cmp_min = 0
    id_max = ""
    nombre_max = ""
    provincia_max = ""
    comuna_max = ""

    id_min = ""
    nombre_min = ""
    provincia_min = ""
    comuna_min = ""

    tamaño = Grafo1.nodos.keys().size()
    i = 0
    while i < tamaño:
        primero = 0
        if Grafo1.nodos.keys().obtener(i).tipo == "casas":
            valor = Grafo1.nodos.keys().obtener(i).potencia_recibida
            if valor >= valor_cmp_max:
                valor_cmp_max = valor
                id_max = Grafo1.nodos.keys().obtener(i).elemento.id_
                nombre_max = Grafo1.nodos.keys().obtener(i).elemento.nivel
                provincia_max = Grafo1.nodos.keys().obtener(
                    i).elemento.provincia
                comuna_max = Grafo1.nodos.keys().obtener(i).elemento.comuna

            if primero == 0:
                valor_cmp_min = valor
                id_min = Grafo1.nodos.keys().obtener(i).elemento.id_
                nombre_min = Grafo1.nodos.keys().obtener(i).elemento.nivel
                provincia_min = Grafo1.nodos.keys().obtener(
                    i).elemento.provincia
                comuna_min = Grafo1.nodos.keys().obtener(i).elemento.comuna
                primero += 1

            if valor <= valor_cmp_min:
                valor_cmp_min = valor
                id_min = Grafo1.nodos.keys().obtener(i).elemento.id_
                nombre_min = Grafo1.nodos.keys().obtener(i).elemento.nivel
                provincia_min = Grafo1.nodos.keys().obtener(
                    i).elemento.provincia
                comuna_min = Grafo1.nodos.keys().obtener(i).elemento.comuna
        i += 1

    if tipo == "mayor":
        return "El cliente de {} con id {} es el con mayor consumo eléctrico " \
               "ubicado en {} , {}".format(nombre_max, id_max, provincia_max,
                                           comuna_max)
    else:
        return "El cliente de {} con id {} es el con menor consumo eléctrico " \
               "ubicado en {} , {}".format(nombre_min, id_min, provincia_min,
                                           comuna_min)


def potencia_perdida(id, tamaño):
    pass


def consumo_sub(tamaño, id, tipo, sistema):

    if tipo != "distribucion" and tipo != "transmision":
        raise InvalidQuery("No es del tipo de una subestacion")

    if sistema != "SING" and sistema != "SIC" and sistema != "SEA" and sistema\
            != "SEM":
        raise InvalidQuery("No existe un sistema bajo ese nombre")

    Grafo1 = Graph(sistema)
    Grafo1.cargar_archivo(tamaño, "centrales_elevadoras")
    Grafo1.cargar_archivo(tamaño, "casas_distribucion")
    Grafo1.cargar_archivo(tamaño, "distribucion_transmision")
    Grafo1.cargar_archivo(tamaño, "transmision_elevadoras")
    Grafo1.cargar_archivo(tamaño, "casas_casas")
    Grafo1.demanda_real()
    Grafo1.flujo()

    consumo = 0
    existe = False

    tamaño = Grafo1.nodos.keys().size()
    i = 0
    while i < tamaño:
        if Grafo1.nodos.keys().obtener(i).elemento.id_ == id and \
                Grafo1.nodos.keys().obtener(i).tipo == tipo:
            consumo = Grafo1.nodos.keys().obtener(i).potencia_recibida
            existe = True
        i += 1

    if existe == False:
        raise InvalidQuery(tipo, id, "no existe")
        # raise algo

    return "El consumo de la subestación {} con id {} fue de {}".format(tipo,
                                                                 id, consumo)

if __name__ == '__main__':

    Grafo1 = Graph("SING")
    Grafo1.cargar_archivo("small", "centrales_elevadoras")
    Grafo1.cargar_archivo("small", "casas_distribucion")
    Grafo1.cargar_archivo("small", "distribucion_transmision")
    Grafo1.cargar_archivo("small", "transmision_elevadoras")
    Grafo1.cargar_archivo("small", "casas_casas")
    Grafo1.demanda_real()
    Grafo1.flujo()
    print(consumo_casa("mayor", Grafo1))
    print(energia_total_comuna("MARIA ELENA", "small", "SING"))




