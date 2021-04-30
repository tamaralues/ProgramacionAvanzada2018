from lectura_csv import read_passengers, read_aiports, read_flights, \
    read_flight_pass
from math import sin, asin, cos, sqrt, pow
from datetime import datetime

# Hago los chequeos y eso llama a estas funciones


def load_database(file):

    if file == "Passengers":
        return read_passengers()

    elif file == "Airports":
        return read_aiports()

    elif file == "Flights":
        return read_flights()

    elif file == "Travels":
        return read_flight_pass()


# utilize este codigo para anidar dos
# generadoreshttps://stackoverflow.com/questions/9708902/in-practice-what-are-t
# he-main-uses-for-the-new-yield-from-syntax-in-python-3

def wrapper_flights(lista):
    # Manually iterate over data produced by reader
    lista_= lista
    for g in lista_:
        lista1_= load_database("Travels")
        for i in lista1_:
            if i[0] == g[0]:
                # si los id son iguales, retoro el id de los pasajeros
                yield i[1]
            else:
                pass


def wrapper_passengers(lista1):
    # Manually iterate over data produced by reader
    lista_= lista1
    #id de usuarios
    for g in lista_:
        # id de usuario y nombre
        lista1_= load_database("Passengers")
        for i in lista1_:
            if i[0] == g:
                # si los id son iguales, retoro el id de los pasajeros
                yield i
            else:
                pass


def filter_passengers(passengers, flights, travels, icao, start, end):

    gen_destino = filter(lambda x: x[2] == icao, load_database("Flights"))
    gen_filter_up = filter(lambda x: compare_dates(x[4], end, ">") == True,
                           gen_destino)
    gen_filter_low = filter(lambda x: compare_dates(x[4], start, "<") == True,
                             gen_filter_up)
    filter_flight_id = wrapper_flights(gen_filter_low)
    passenger_flight = wrapper_passengers(filter_flight_id)
    return passenger_flight


def filter_passengers_by_age(passengers, age, lower):

    passengers_ = filter(lambda x: x[0]!= "id", passengers)
    if lower == True:
        passengers_ = filter(lambda x: float(x[3]) < age, passengers_)
    else:
        passengers_ = filter(lambda x: float(x[3]) > age, passengers_)
    return passengers_


def filter_airports_by_country(airports, iso):

    gen_airports = filter(lambda x: x[4] == iso, airports)
    return gen_airports


# Saque este codigo para calcular la
# formula de Haversine https://stackoverflow.com/questions/4913349/haversine-
# formula-in-python-bearing-and-distance-between-two-gps-points


def formula(x1, y1, x2, y2):

    dlat = y1 - x1
    dlon = y2 - x2
    a = sin(dlat / 2) ** 2 + cos(x1) * cos(y1) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3440
    formula_ = c * r
    return formula_


def filter_airports_by_distance(airports_, icao, distance, lower):

    gen_airport_id = filter(lambda x: x[0] == icao, load_database("Airports"))
    airports = filter(lambda x: x[2] != "lat", airports_)
    d_icao = list(gen_airport_id)

    if lower == True:
        gen_filter_distance = filter(lambda x: formula(float(d_icao[0][2]),
                              float(x[2]), float(d_icao[0][3]), float(x[3])) <
                             distance, airports)
    else:
        gen_filter_distance = filter(lambda x: formula(float(d_icao[0][2]),
                              float(x[2]), float(d_icao[0][3]), float(x[3])) >
                            distance, airports)
    return gen_filter_distance


def compare_dates(val_x, value, consulta):

    date1 = datetime.strptime(val_x, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    if consulta == ">":
        if date1 >= date2:
            return True
    elif consulta == "==":
        if date1 == date2:
            return True
    elif consulta == "!=":
        if date1 != date2:
            return True
    else:
        if date1 <= date2:
            return True


def filter_flights_date(data_checked, airports, attr, symbol, value):

    if symbol == ">":
        gen_filter_time = filter(lambda x: compare_dates(x[3], value,
                                  symbol) == True, data_checked)
    elif symbol == "==":
        gen_filter_time = filter(lambda x: compare_dates(x[3], value,
                                  symbol) == True, data_checked)
    elif symbol == "!=":
        gen_filter_time = filter(lambda x: compare_dates(x[3], value,
                                  symbol) == True, data_checked)
    else:
        gen_filter_time = filter(lambda x: compare_dates(x[3], value,
                                  symbol) == True, data_checked)
    return gen_filter_time


def distance(start, finish, airports):

    lista_air = airports
    data_aeropuerto1 = filter(lambda x: x[0] == start , lista_air)
    data_aeropuerto2 = filter(lambda x: finish == x[0], lista_air)
    valor_aeropuerto1 = list(data_aeropuerto1)
    valor_aeropuerto2 = list(data_aeropuerto2)
    if valor_aeropuerto1 == [] or valor_aeropuerto2 == []:
        return 0
    return formula(float(valor_aeropuerto1[0][2]), float(valor_aeropuerto2[0][
                                                            2]),
                   float(valor_aeropuerto1[0][3]), float(valor_aeropuerto2[0][
                                                 3]))


def filter_flights_dist(flights, airports, attr, symbol, value):

    if symbol == ">":
        gen_filter_distance = filter(lambda x: distance(x[1], x[2],
                                     [i for i in airports]) > value, flights)
    elif symbol == "==":
        gen_filter_distance = filter(lambda x: distance(x[1], x[2],
                                    [i for i in airports]) == value, flights)
    elif symbol == "!=":
        gen_filter_distance = filter(lambda x: distance(x[1], x[2],[i for i in
                                            airports]) != value, flights)
    else:
        gen_filter_distance = filter(lambda x: distance(x[1], x[2],[i for i in
                                                airports]) < value, flights)
    return gen_filter_distance


def filter_flights(flights_, airports, attr, symbol, value):

    if attr == "distance":
        flights = filter(lambda x: x[0] != "id", flights_)
        gen_filter_dist = filter_flights_dist(flights, airports, attr, symbol,
                                              value)
        return gen_filter_dist
    else:
        data_checked = filter(lambda x: x[3] != "date", flights_)
        gen_filter_time = filter_flights_date(data_checked, airports, attr,
                                              symbol,value)
        return gen_filter_time

