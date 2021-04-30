from os import path, remove
from random import sample

# ------ Encriptación ------




def codificador(string):
    arquetipos =["a", "r", "q", "u", "e", "t", "i", "p","o","s"]
    lista = ["0", "1", "2","3", "4", "5", "6", "7", "9", "9"]
    dictzip= dict(zip(arquetipos, lista))
    for i in dictzip:
        for k in i:
            for m in string:
                if m == k:
                    string = string.replace(m, dictzip[k])
                    pass

                elif m == dictzip[k]:
                    string = string.replace(m, k)

    return string


    """
    Debe retornar el string codificado por la clave arquetipos.

    Usa funcional al programar esta función.
    """



# ------ Decoradores -------


"""

@pasaprogra: Este decorador debe verificar si la palabra ingresada como respuesta 
por el jugador en la funci ́on jugar es igual a “pasaprogra”. De ser as ́ı, debe retornar 
la respuesta y cero puntos. En cualquier otro caso, debe retornar lo que retorna
 la funci ́on decorada.


"""

def pasaprogra(funcion):
    def funcion_chequeadora(*args):
        respuesta, respuestacorrecta = func(*args)
        if  respuesta== "pasaprogra":
            restador = 0
            orden = "1"
        else:
            restador = 1
            orden = "2"

        return restador, orden
    return funcion_chequeadora


def esconder_palabra(funcion):
    """
    Decorador que se encarga de esconder la palabra en la oración.

    La función 'camuflar', definida más abajo, te puede ser útil.
    """
    linea = funcion(*args, **kwargs)
    lista =linea.split(",")
    palabra_camuflada = camuflar(lista[0])

    lista2 = lista[1].split(" ")
    for i in range(len(lista2)):

        if lista2[i] == "palabra":
            lista2[i] == palabra_camuflada

    string=""

    for i in lista2:
        string += i + " "


    return string



def desencriptar(funcion_decodificadora):
    """
    Decorador que permite desencriptar las palabras.

    La desencriptación requiere de una función decodificadora.
    """
    funcion_codificadora()  # mi codificdor también decodifica
    def nueva_funcion(func):
        linea = func(*args)
        return funcion_decodificadora(linea)




def encriptar(funcion_codificadora):
    funcion_codificadora()

    """
    Decorador para encriptar las respuestas de los jugadores y guardarlas.

    La encriptación requiere de una función codificadora.
    Las palabras encriptadas deben ser guardadas en 'resultados_encr.txt'.
    """
    return


# ------------------------------------------------------------

# --------- NO MODIFICAR LAS FUNCIONES, SOLO DECORAR ---------

# ------------------------------------------------------------


def camuflar(palabra):
    """
    Devuelve una palabra con la mitad de sus letras,
    escogidas al azar, camufladas con guiones bajos.

    Utilízala en tus decoradores!

    Ejemplos:
    ========
    - 'hola': --> '_ol_'
    - 'mundo': ---> '_un__'
    - 'palabra': ---> '_a__br_'
    """

    muestra = sample(palabra, round(len(palabra) / 2))
    for letra in muestra:
        palabra = palabra.replace(letra, '_', 1)
    return palabra


@desencriptar(codificador)
def leer_archivo(ruta_archivo):
    """
    Esta función recibe una ruta (path) y retorna un generador con los datos.

    Nota que es cada línea se divide sólo con la primera coma, por lo que
    siempre hace yield de dos elementos.

    Decorar para:
    =============
    - Entregar los datos desencriptados.
    """

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # ¿Por qué usar split con maxsplit=1?
            # Porque solo queremos dividir el string con la primera coma
            yield linea.strip().split(',', maxsplit=1)


@esconder_palabra
def juego_ahorcado(ruta_archivo_ahoracado):

    """
    Esta función generadora entrega las oraciones del juego ahorcado.

    Decorar para:
    =============
    - Esconder la palabra a adivinar dentro de la oración.
    """

    print('Juego: AHORCADO')
    print('En este juego se te dará una oración con una palabra',
          'incompleta que debes adivinar')
    yield from leer_archivo(ruta_archivo_ahoracado)
    print('-' * 80)


def juego_rosca(ruta_archivo_rosca):

    """
    Esta funcion genera las definiciones del juego rosca.

    Es una función generadora.
    """

    print('Juego: ROSCA')
    print('En este juego se te dará una definición y',
          'deberá adivinar la palabra asociada')
    yield from leer_archivo(ruta_archivo_rosca)
    print('-' * 80)


@pasaprogra
def jugar(respuesta, palabra_correcta):
    """
    Esta función verifica si la respuesta es igual a la palabra correcta.

    Si la respuesta es correcta, entrega 1 punto. En caso contrario, -1.

    Decorar para:
    =============
    - Poder pasar y dar 0 puntos en ese caso.
    - Encriptar la respuesta.
    """

    if respuesta.lower() == palabra_correcta.lower():
        print(f"{respuesta}: Correcto! has ganado 1 punto :)")
        return respuesta, 1
    print(f"{respuesta}: Incorrecto! la respuesta era {palabra_correcta},",
          "has perdido 1 punto :(")
    return respuesta, -1


if __name__ == '__main__':
    # Limpia el archivo de resultados encriptados
    if path.exists('resultados_encr.txt'):
        remove('resultados_encr.txt')
    # Sigue con la ejecución
    RUTA_JUEGO_AHORCADO = 'ahorcado_encriptada.txt'
    RUTA_JUEGO_ROSCA = 'rosca_encriptada.txt'
    puntaje = 0
    nombre = input('Ingresa tu nombre: ')
    print(f'BIENVENIDO A PASAPROGRA {nombre}')

    for palabra_correcta, oracion in juego_ahorcado(RUTA_JUEGO_AHORCADO):
        print(f'Tienes {puntaje} puntos!')
        print(oracion)
        respuesta_jugador = input('Ingrese su respuesta: ')
        _, puntos_ganados = jugar(respuesta_jugador, palabra_correcta)
        puntaje += puntos_ganados

    for palabra_correcta, definicion in juego_rosca(RUTA_JUEGO_ROSCA):
        print(f'Tienes {puntaje} puntos!')
        print(definicion)
        respuesta_jugador = input('Ingrese su respuesta: ')
        _, puntos_ganados = jugar(respuesta_jugador, palabra_correcta)
        puntaje += puntos_ganados

    print(f"Terminaste con {puntaje} puntos")

jugar()