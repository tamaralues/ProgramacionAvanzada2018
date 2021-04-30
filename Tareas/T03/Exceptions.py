
class ForbiddenAction(Exception):
    def __init__(self, tipo_destino, tipo_origen = None):
        # Sobreescribimos el __init__ para cambiar el ingreso de los parámetros

        if tipo_origen != None:
            mensaje = "Acción agregar_arista no está permitida entre {} y {}".\
                format(tipo_origen, tipo_destino)

        elif tipo_destino == "no existe":
            mensaje = "Acción agregar_arista no puede unir dos elementos en " \
                      "donde 1 o mas no existen"

        elif tipo_destino == "no estan en la misma comuna":
            mensaje = "Acción agregar_arista no puede unir elementos que " \
                      "estan en diferentes comunas"

        elif tipo_destino == "Ya tiene una elevadora":
            mensaje = "Acción agregar_arista ya que la subestacion ya tiene " \
                      "una elevadora"

        elif tipo_destino == "ya tiene una subestacion transmisora":
            mensaje = "Acción agregar_arista ya que la subestacion ya tiene " \
                      "una transmisora"

        else:
            mensaje = "Acción agregar_arista no esta permitida ya que " \
                      "formaría un ciclo"

        super().__init__(mensaje)


class ElectricalOverload(Exception):
    def __init__(self, cantidad, funcion):
        super().__init__("La acción {} sobre carga la red a {} kW".format(
            funcion, (cantidad - 30000)))


class InvalidQuery(Exception):
    def __init__(self,tipo, id = None,  elemento = None):
        # Sobreescribimos el __init__ para cambiar el ingreso de los parámetros

        if tipo == "No es del tipo de una subestacion":
            mensaje = tipo

        elif elemento == "no existe":
            mensaje = "La instalacion de tipo {} y id {} no existe".format(
                tipo, id)

        elif tipo == "La consulta no soporta un tipo de consulta distinto a " \
                     "'mayor' o 'menor'":
            mensaje = tipo

        elif tipo == "No existe un sistema bajo ese nombre":
            mensaje = tipo

        super().__init__(mensaje)


