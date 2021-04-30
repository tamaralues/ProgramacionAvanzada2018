# En este modulo se estan las funciones que leen los archivos, estos crean
# una lista , sets, y dicts por compresion dependiendo el archivo. además de
# admin_queries, reciben los filtros y llaman a cosultas con el archivo
# abierto mas los filtros.

from ast import literal_eval

# Código de iic2233-utils

def parse(string):
    """Parse a Python literal, without raising exceptions."""
    try:
        return literal_eval(string)
    except (ValueError, SyntaxError, TypeError):
        # ValueError is raised when an illegal node is in the tree
        # SyntaxError is raised when the syntax is not correct
        # TypeError is raised when a set contains a non-hashable object
        # Create an issue if you get another exception
        return None


def read_passengers():

    with open("data/small/passengers.csv") as file:

        data = [linea.strip().split(",") for linea in file]
        data_passengers = (i for i in data)

    return data_passengers


def read_aiports():

    with open("data/small/airports.csv") as file:
        data = [linea.strip().split(",") for linea in file]
        data_airports = (i for i in data)

    return data_airports

# Vuelos es un generador por compresion, ya que tiene sus cualidades y no se
# repiten


def read_flights():

    with open("data/small/flights.csv") as file:
        data = [(linea.strip().split(",")) for linea in file]
        data_flights = (i for i in data)

    return data_flights

# Viajes es una generador por compresion.


def read_flight_pass():

    with open("data/small/flights-passengers2.csv") as file:
        data = [(linea.strip().split(",")) for linea in file]
        data_flight_pass = (i for i in data)

    return data_flight_pass


def read_consultas():

    with open("data/queries.txt") as file:
        data_queries = [parse(linea) for linea in file]
    return data_queries


def open_():
    with open("output.txt") as file:
        data = [[linea.strip("\n").strip("*")]
                for linea in file]
    data_ = filter(lambda x : x != [''], data)
    return data_

