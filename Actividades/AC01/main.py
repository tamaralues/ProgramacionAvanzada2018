from collections import namedtuple, defaultdict, deque

"""
Aquí están las estructuras de datos para guardar la información respectiva.

NO MODIFICAR.
"""

# Como se vio en la ayudantía, hay varias formas de declarar una namedtuple :)
Entrenador = namedtuple('Entrenador', 'nombre apellido')
Pokemon = namedtuple('Pokemon', ['nombre', 'tipo', 'max_solicitudes'])
Solicitud = namedtuple('Solicitud', ['id_entrenador', 'id_pokemon'])

################################################################################
"""
En esta sección debe completar las funciones para cargar los archivos al sistema.

Puedes crear funcionas auxiliar si tú quieres, ¡pero estas funciones DEBEN
retornar lo pedido en el enunciado!
"""

def cargar_entrenadores(ruta_archivo):
    data_entrenadores=dict()
    with open(ruta_archivo) as file:
        for linea in file:
            linea=linea.split(";")
            id= str(linea[0])
            nombre=str(linea[1].strip("\n"))
            apellido = str(linea[2].strip("\n"))
            data_entrenadores[id]=Entrenador(nombre, apellido)

    return data_entrenadores


def cargar_pokemones(ruta_archivo):
    data_pokemones = dict()
    with open(ruta_archivo) as file:
        for linea in file:
            linea=linea.split(";")
            linea[3]=linea[3].strip("\n")
            id = str(linea[0])
            nombre = str(linea[1])
            tipo= str(linea[2])
            max_solicitudes= linea[3]
            data_pokemones[id] = Pokemon(nombre, tipo, max_solicitudes)
    return data_pokemones



def cargar_solicitudes(ruta_archivo):
    data_solicitudes = dict()
    lugar=0
    with open(ruta_archivo) as file:
        for linea in file:
            linea = linea.split(";")
            id_entrenador= linea[0]
            linea[1] = linea[1].strip("\n")
            id_pokemones= linea[1]
            data_solicitudes[lugar] = \
                Solicitud(id_entrenador,id_pokemones)

            lugar=lugar+1
    print(data_solicitudes)

    return data_solicitudes

################################################################################

"""
Lógica del Sistema.
Debes completar esta función como se dice en el enunciado.
"""

def sistema(modo, entrenadores, pokemones, solicitudes):
    solicitudes=cargar_solicitudes("solicitudes.txt")
    entrenadores=cargar_entrenadores("entrenadores.txt")
    pokemones=cargar_pokemones("pokemones.txt")
    c=0
    deque_modo1= deque()
    deque_modo2= deque()
    for i in entrenadores.keys():
        if i==c:
            c=c+1
            deque_modo1=deque_modo1.append(entrenadores.values())
            deque_modo2= deque_modo1.appendleft(entrenadores.values())


    if modo=="1":
        return deque_modo1

    else:
        return deque_modo2



################################################################################
"""
Funciones de consultas, deben rellenarlos como dice en el enunciado :D.
"""

def pokemones_por_entrenador(id_entrenador, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con el
    id entregado.

    Recuerda que esta función debe retornar una lista.
    """
    pass

def mismos_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó tanto el entrenador
    con el id_entrenador1 como el entrenador con el id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    pass

def diferentes_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):

    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con
    id_entrenador1 y que no ganó el entrenador con id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    pass


if __name__ == '__main__':

    ############################################################################
    """
    Poblando el sistema.
    Ya se hacen los llamados a las funciones, puedes imprimirlos para ver si se
    cargaron bien.
    """

    entrenadores = cargar_entrenadores('entrenadores.txt')
    pokemones = cargar_pokemones('pokemones.txt')
    solicitudes = cargar_solicitudes('solicitudes.txt')

    # print(entrenadores)
    # print(pokemones)
    # print(solicitudes)

    ################################   MENU   ##################################
    """
    Menú.
    ¡No debes cambiar nada! Simplemente nota que es un menú que pide input del
    usuario, y en el caso en que este responda con "1" ó "2", entonces se hace
    el llamado a la función. En otro caso, el programa termina.
    """

    eleccion = input('Ingrese el modo de lectura de solicitudes:\n'
                 '1: Orden de llegada\n'
                 '2: Orden Inverso de llegada\n'
                 '>\t')

    if eleccion in {"1", "2"}:
        resultados_simulacion = sistema(eleccion, entrenadores,
                                        pokemones, solicitudes)
    else:
        exit()

    ##############################   Pruebas   #################################
    """
    Casos de uso.

    Aquí pueden probar si sus consultas funcionan correctamente.
    """
