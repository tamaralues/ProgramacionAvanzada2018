
class Node:

    def __init__(self, rango, superior):

        self.rango = rango
        self.items = None
        self.superior = superior
        self.superiores = None
        self.afinidad_superiores = None
        self.subordinados = None
        self.rangosubordinados = None

    def obtener_nodo(self, rango):

        if self.rango == rango:
            return self

        for sub in self.subordinados.values():
            nodo = sub.obtener_nodo(rango)

            if nodo:
                return nodo

        return None

    def _agregar_subordinado(self, rango, afinidad_superiores, superior):

        superior = self.obtener_nodo(superior)

        if superior is None:
            return

        nodo = type(self)(rango, afinidad_superiores, superior)
        superior.subordinados[rango] = nodo

        # agregar aca las condiciones de si seria un subordinado o no


class Entidades:

    def __init__(self, rango, superior):
        self.children = Node(rango, superior)

    def agregar_subordinado(self, rango, superior, afinidad):

        self.children._agregar_subordinado(rango, superior, afinidad)