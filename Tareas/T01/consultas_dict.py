# En chequeos_filter_gen se hace el chequeo por lo que el ingreso de los
# generadores ya estan "pre" filtrados

from consultas_gen import distance, load_database


def gen_tuplas(generador_pass, travels):
    lista = generador_pass
    lista2 = [i for i in travels]
    for i in lista.keys():
        for g in lista2:
            lista[i] = [g[0] for g in lista2 if i == g[1]]
            #  https://stackoverflow.com/questions/6987285/python-find-the-item
            # -with-maximum-occurrences-in-a-list#comment8338917_6987358
            # https: // stackoverflow.com / questions / 26151669 / valueerr
            # or- max - arg - is -an - empty - sequence
            lista[i] = max(lista[i], key = lista[i].count) if lista[i] else None
            yield lista


def conteo(gentuplas, flights):
    lista2 = [i for i in flights]
    lista1 = [i for i in gentuplas][0]
    for i in lista1.keys():
        lista1[i] = [i for i in filter(lambda x: x[0] == lista1[i], lista2)]
        lista1[i] = lista1[i][0][2] if lista1[i] else None
        yield lista1


def favourite_airport(passengers, flights, travels):

    dict_ = {i[0]:[] for i in passengers}
    gen_tu = gen_tuplas(dict_, travels)
    gen_con = conteo(gen_tu, flights)
    dict_ =[i for i in gen_con][0]
    return dict_

# https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3


def gen_calculo_millas(travels, flights, airports):
    data = travels
    lista2 = [i for i in flights]
    for i in data:
        millas_flight = 0
        for g in lista2:
            if i[0] == g[0]:
                millas_flight = distance(g[1], g[2], airports)

        yield i[1], millas_flight


def calculo_millas(gen_calculo, passengers):
    lista2 = [i for i in passengers]
    for i in gen_calculo:
        millas = 0
        for g in lista2:
            if i[0] == g[0]:
                millas += float(i[1])
        yield i[0], millas


def passenger_miles(passengers, airports,  flights, travels):
    gen_calc_millas = gen_calculo_millas(travels, flights, airports)
    calculo_por_id = calculo_millas(gen_calc_millas, passengers)
    # https://stackoverflow.com/questions/20489609/dictionary-comprehension-in-p
    # ython-3 diccionarios por compresion de una generador
    dict_ = {x[0]: x[1] for x in calculo_por_id}
    return dict_



def generador_suma(travels, flights):
    lista = {i[0]:[] for i in flights}
    lista2 = [i for i in travels]
    for i in lista.keys():
        for g in lista2:
            lista[i] = [g[1] for g in lista2 if i == g[0]]

            yield lista


def calculo_vuelo(generador_suma, airports):
    lista = [i for i in generador_suma][0]
    for m in lista.keys():
        passengers = 0
        for i in airports:
            if m == i[0]:
                passengers += 1
        yield i[0], passengers


def calculo_promedio(gen_promedio, airports):
    lista = [i for i in gen_promedio]
    for i in airports:
        suma_vuelo = 0
        suma_pass = 0
        promedio = 0
        for m in lista:
            if i[0] == m[0]:
                suma_vuelo += 1
                suma_pass += float(m[1])

        promedio = suma_pass/suma_vuelo
        yield i[0], promedio


def popular_airports(flights, airports, travels, topn, avg):

    # passengers, flights, y travels no son directamente load siempre
    if avg == True:
        generador_sum = generador_suma(travels, flights)
        generador_sum_tot = calculo_vuelo(generador_sum, airports)
        #https://stackoverflow.com/questions/3121979/how-to-sort-list-tu
        # ple-of-lists-tuples
        print(list(generador_sum_tot))
        generador_pop1 = sorted(generador_sum_tot, key = lambda tup: (-tup[1]))
    else:
        generador_prom = generador_suma(travels, flights)
        generador_prom_total = calculo_promedio(generador_prom, airports)
        # https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of
        # -lists-tuples
        generador_pop1 = sorted(generador_prom_total, key=lambda tup: (-tup[1]))
    generador_pop = tuple(i[0] for i in generador_pop1)
    return generador_pop[:topn]


def filter_icao_travels(flights, travels, icao):
    list_ = [i for i in flights]
    from1_ = [i for i in filter(lambda x: x[1] == icao, list_)]
    from_ = [i for i in from1_]
    to1_ = filter(lambda x: x[2] == icao, list_)
    to_ = [i for i in to1_]
    from_to = from_ + to_
    for i in travels:
        for m in from_to:
            if m[0] == i[0]:
                yield i[1]


def op_and(pass_icao1, pass_icao2):
    lista1 = [i for i in pass_icao1]
    lista2 = [i for i in pass_icao2]
    for m in lista1:
        for i in lista2:
            if m == i:
                yield m


def op_xor(pass_icao1, pass_icao2):
    lista1 = [i for i in pass_icao1]
    lista2 = [i for i in pass_icao2]
    lista3 = set(lista1 + lista2)
    for m in lista3:
        if m in lista2:
            if m in lista1:
                pass
            else:
                yield m
        else:
            yield m


def op_diff(pass_icao1, pass_icao2):
    lista1 = [i for i in pass_icao1]
    lista2 = [i for i in pass_icao2]
    for m in lista1:
        for i in lista2:
            if m != i:
                yield m


def nombres(op_result, passengers):
    data = passengers
    lista = set(op_result)
    for i in data:
        for m in lista:
            if m == i[0]:
                yield i[1]


def airport_passengers(passengers, flights, travels, icao1, icao2, op):

    pass_icao1 = filter_icao_travels(flights, travels, icao1)
    pass_icao2 = filter_icao_travels(flights, travels, icao2)
    if op == "AND":
        op_result = op_and(pass_icao1, pass_icao2)
    elif op == "OR":
        op_or = set([i for i in pass_icao1]+ [i for i in pass_icao2])
        op_result = (i for i in op_or)
    elif op == "XOR":
        op_result = op_xor(pass_icao1, pass_icao2)
    else:
        op_result = op_diff(pass_icao1, pass_icao2)
    lista_pass = nombres(op_result, passengers)

    return {i for i in lista_pass}


def search_vuelo(sort_, travels):
    data = travels
    for i in data:
        for m in sort_:
            if m[0] == i[0]:
                yield i[1], m[1]


def search_pass(sort_, passengers):
    data = passengers
    for i in data:
        for m in sort_:
            if m[0] == i[0]:
                yield i[1], m[1]


def calculo_mayor(vuelo, travels, passengers, airports):

    distance_ = ((x[0], distance(x[1], x[2], [i for i in airports])) for
                 x in vuelo)
    # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
    sort_dist = sorted(distance_, key = lambda tup: (tup[1]))
    search_id_fl = search_vuelo(sort_dist, travels)
    search_id_pass = set(search_pass([i for i in search_id_fl], passengers))
    final_ = sorted(search_id_pass, key=lambda tup: (tup[1]))
    final = [i[0] for i in final_]
    return final


def furthest_distance(passengers, airports, flights, travels, icao, n):
    vuelo = filter(lambda x: x[1] == icao, flights)
    gen_nombres = calculo_mayor(vuelo, travels, passengers, airports)
    lista1_ = [i for i in gen_nombres]
    return lista1_[:n]

