from lectura_csv import parse
from consultas_gen import *
from consultas_dict import *

# https://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-
# variable-directly-in-python-not-by-searching-fr obtener el key (lo uso en m

def check_load(lista):
    if len(list(lista.values())[0]) == 1 :
        if list(lista.values())[0][0] == "Airports" or list(lista.values())[
            0][0] == "Flights" or list(lista.values())[0][0] == "Travels" or \
                list(lista.values())[0][0] == "Passengers":

            return load_database(list(lista.values())[0][0])
    else:
         return ["No es válida la consulta"]


def check_filter_flights(lista):

    if len(list(lista.values())[0]) == 5:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            data1 = check_load(list(lista.values())[0][0])
            if list(list(lista.values())[0][1].keys())[0] == "load_database":
                data2 = check_load(list(lista.values())[0][1])
                if list(lista.values())[0][2] == "distance" or list(
                        lista.values(
                    ))[0][2] == "date":
                    data3 = list(lista.values())[0][2]
                    if list(lista.values())[0][3] == "<" or list(
                            lista.values())[0][3] == ">"  or list(lista.values()
                            )[0][3] == "=="or list(lista.values())[0][3] == \
                            "!=" :
                        data4 = list(lista.values())[0][3]
                        data5 = list(lista.values())[0][4]
                        print(data1, data2, data3, data4, data5)
                        return filter_flights(data1, data2, data3, data4, data5)

    return ["No es válida la consulta"]


def check_filter_pass(lista):

    if len(list(lista.values())[0]) == 6:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            if list(list(lista.values())[0][1].keys())[0] == "load_database":
                d2 = check_load(list(lista.values())[0][1])
                if list(list(lista.values())[0][2].keys())[0] == \
                        "load_database":
                    d3 = check_load(list(lista.values())[0][2])
                    if type(list(lista.values())[0][3]) == str and type(list(
                            lista.values())[0][4]) == str and type(list(
                        lista.values())[0][5]) == str:
                        d4 = list(lista.values())[0][3]
                        d5 = list(lista.values())[0][4]
                        d6 = list(lista.values())[0][5]
                        return filter_passengers(d1, d2, d3, d4, d5, d6)
    return ["No es válida la consulta"]


def check_pass_by_age(lista):

    if len(list(lista.values())[0]) == 3 :
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            d2 = int(list(lista.values())[0][1])
            d3 = list(lista.values())[0][2]
            return filter_passengers_by_age(d1, d2, d3)

    elif len(list(lista.values())[0]) == 2:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            d2 = int(list(lista.values())[0][1])
            d3 = False
            return filter_passengers_by_age(d1, d2, d3)

    return ["No es válida la consulta"]


def check_filter_air(lista):
    if len(list(lista.values())[0]) == 2:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            d2 = list(lista.values())[0][1]
            return filter_airports_by_country(d1, d2)
    return ["No es válida la consulta"]


def check_filter_air_by_dist(lista):

    if len(list(lista.values())[0]) == 4:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            d2 = list(lista.values())[0][1]
            d3 = list(lista.values())[0][2]
            d4 = list(lista.values())[0][3]
            return filter_airports_by_distance(d1, d2, d3, d4)
    elif len(list(lista.values())[0]) == 3:
        if list(list(lista.values())[0][0].keys())[0] == "load_database":
            d1 = check_load(list(lista.values())[0][0])
            d2 = list(lista.values())[0][1]
            d3 = list(lista.values())[0][2]
            d4 = False
            return filter_airports_by_distance(d1, d2, d3, d4)

    return ["No es válida la consulta"]



def check_data(lista):

    if list(lista.keys())[0] == "load_database":
        d = check_load(lista)
    else:
        d = check_consulta(lista)
    return d


def check_fav_air(lista):
    lista_ = (i for i in range(0, 1))
    if len(list(lista.values())[0]) == 3:
        d1 = check_data(list(lista.values())[0][0])
        d2 = check_data(list(lista.values())[0][1])
        d3 = check_data(list(lista.values())[0][2])
        if type(d3) == type(lista_) and type(d2) == type(lista_) and type(d1)\
                == type(lista_):
            return favourite_airport(d1, d2, d3)
    return ["No es válida la consulta"]


def check_pass_miles(lista):
    lista_ = (i for i in range(0, 1))
    if len(list(lista.values())[0]) == 3:
        d1 = check_data(list(lista.values())[0][0])
        d2 = check_data(list(lista.values())[0][1])
        d3 = check_data(list(lista.values())[0][2])
        d4 = check_data(list(lista.values())[0][3])
        if type(d3) == type(lista_) and type(d2) == type(lista_) and type(d1) \
                == type(lista_) and type(d4) == type(lista_):
            return passenger_miles(d1, d2, d3, d4)
    return ["No es válida la consulta"]


def check_pop_airport(lista):
    lista_ = (i for i in range(0, 1))
    if len(list(lista.values())[0]) == 5 or len(list(lista.values())[0]) == 4:
        d1 = check_data(list(lista.values())[0][0])
        d2 = check_data(list(lista.values())[0][1])
        d3 = check_data(list(lista.values())[0][2])
        if type(d3) == type(lista_) and type(d2) == type(lista_) and type(d1) \
                == type(lista_) and len(list(lista.values())[0]) == 5:
            d4 = list(lista.values())[0][3]
            d5 = list(lista.values())[0][3]
        elif type(d3) == type(lista_) and type(d2) == type(lista_) and type(
                d1) == type(lista_) and len(list(lista.values())[0]) == 4:
            d4 = list(lista.values())[0][3]
            d5 = False
        return popular_airports(d1, d2, d3, d4, d5)
    return ["No es válida la consulta"]


def check_air_pass(lista):
    lista_ = (i for i in range(0, 1))
    if len(list(lista.values())[0]) == 6:
        d1 = check_data(list(lista.values())[0][0])
        d2 = check_data(list(lista.values())[0][1])
        d3 = check_data(list(lista.values())[0][2])
        if type(d3) == type(lista_) and type(d2) == type(lista_) and type(d1) \
                == type(lista_):
            d4 = list(lista.values())[0][3]
            d5 = list(lista.values())[0][4]
            d6 = list(lista.values())[0][5]
            return airport_passengers(d1, d2, d3, d4, d5, d6)
    return ["No es válida la consulta"]


def check_further(lista):
    lista_ = (i for i in range(0, 1))
    if len(list(lista.values())[0]) == 6 or len(list(lista.values())[0]) == 5 :
        d1 = check_data(list(lista.values())[0][0])
        d2 = check_data(list(lista.values())[0][1])
        d3 = check_data(list(lista.values())[0][2])
        d4 = check_data(list(lista.values())[0][3])
        if type(d3) == type(lista_) and type(d2) == type(lista_) and type(d1) \
                == type(lista_):
            d5 = list(lista.values())[0][4]
            if len(list(lista.values())[0]) == 6:
                d6 = list(lista.values())[0][5]
            else:
                d6 = 3
            return furthest_distance(d1, d2, d3, d4, d5, d6)
    return ["No es válida la consulta"]


def call_checker_gen(var):
    if list(var.keys())[0] == "load_database":
        return check_load(var)
    elif list(var.keys())[0] == "filter_flights":
        return check_filter_flights(var)
    elif list(var.keys())[0] == "filter_passengers":
        return check_filter_pass(var)
    elif list(var.keys())[0] == "filter_passengers_by_age":
        return check_pass_by_age(var)
    elif list(var.keys())[0] == "filter_airports_by_country":
        return check_filter_air(var)
    elif list(var.keys())[0] == "filter_airports_by_distance":
        return check_filter_air_by_dist(var)
    else:
        return call_checker_dict(var)


def call_checker_dict(var):

    if list(var.keys())[0] == "favourite_airport":
        return check_fav_air(var)
    elif list(var.keys())[0] == "passenger_miles":
        return check_pass_miles(var)
    elif list(var.keys())[0] == "popular_airports":
        return check_pop_airport(var)
    elif list(var.keys())[0] == "airport_passengers":
        return check_air_pass(var)
    elif list(var.keys())[0] == "furthest_distance":
        return check_further(var)
    else:
        return ["No es válida la consulta"]


def check_1(consulta):
    if type(consulta) == dict:
        return call_checker_gen(consulta)

    else:
        return ["No es valida la consulta "]


def check_consulta(consulta1):

    if type(consulta1) == dict:
        return check_1(consulta1)
    elif type(consulta1) == list:
        descomp_ = (check_1(i) for i in consulta1)
        return descomp_
    else:
        return ["No es válida la consulta"]



