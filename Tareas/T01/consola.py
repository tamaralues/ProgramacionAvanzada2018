from check_filter import *
from lectura_csv import read_consultas, parse, open_
import pprint


def foreach(function, iterable):
    """Apply a function to the elements of an iterable, without returning."""
    for x in iterable:
        function(x)


def inicio():
    res = input("Menu:\n1. Hacer consulta nueva\n2. Hacer consulta (o "
                "consultas) antigua\n3. Ver consultas o eliminar\n")
    if res == "1":
        resp = str(input("Ingresa tu consulta\n"))
        pr = input("¿Quieres guardar esta consulta?  si(1) / no(2)\n")
        return hacer_consulta(resp, pr)
    elif res == "2":
        queries = list(enumerate(open_() , 1))
        queries.insert(0, queries)
        pprint.pprint(queries)
        num = input("¿Quieres hacer consultas anidadas? si(1) / no(2)\n")
        return hacer_consulta_v(num)
    elif res == "3":
        return ver_consultas()
    return inicio()


def gen_output(consulta, resultado):

    resultado1 = type(resultado)
    resultado2 = [i for i in resultado]
    var = ("*-------    Consulta   ------- " + str(consulta) + " " + str(
        resultado1) + str(resultado2)+ "\n")
    return var


def hacer_consulta(resp, pr):
    if pr == "1":
        if type(parse(resp)) == list:
            var = [check_consulta(parse(i)) for i in resp]
        else :
            var = check_consulta(parse(resp))
        with open("output.txt", "a") as txt:
            txt.write(str(gen_output(resp, var)) + "\n")
        with open("data/queries.txt", "a") as txt2:
            txt2.write("\n" + str(resp))
        num = len([i for i in open_()])
        print([i for i in open_()][num - 1:num])
    else:
        var = check_consulta(parse(resp))
        print([i for i in var])
    return inicio()


def ver_consultas():
    queries = list(enumerate(open_(), 1))
    queries.insert(0, queries)
    pprint.pprint(queries)
    res = input("Menu:\n1.Eliminar consulta\n2.Ver consulta en "
                "específico\n3.Volver a inicio\n")
    if res == "1":
        num = int(input("Ingrese el número de consulta que quieres eliminar\n"))
        return delete_consulta(num)
    elif res == "2":
        num = int(input("Ingrese el número de consulta que quieres ver\n"))
        return dar_consulta(num)
    else:
        return inicio()


def dar_consulta(num):
    consulta_to_see = [i for i in open_()]
    print(consulta_to_see[num-1])
    return inicio()


def delete_consulta(num):
    consulta_to_see = [i for i in open_()]
    consulta_to_see.pop(num-1)
    with open("output.txt", "w") as txt:
        txt.write(str(consulta_to_see))
    return inicio()


def hacer_consulta_v(num):
    consulta_to_see = [i for i in open_()]
    pr = input("¿Quieres guardar esta consulta?  si(1) / no(2)\n")
    if num == "1":
        lista = input("Ingrese separado por comas los id de las consultas "
                       "que quieres realizar\n")
        lista = lista.split(",")
        consultas = hacer_consulta([consulta_to_see[int(i)-1] for i in
                     lista] , "1")
    else:
        in_ = input("Ingrese el número de la consulta que quiere hacer\n")
        consultas = hacer_consulta(consulta_to_see[int(in_)-1], pr)
    return inicio()
