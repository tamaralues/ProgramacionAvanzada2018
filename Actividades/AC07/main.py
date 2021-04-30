
from collections import deque

def cargar_archivo(path_archivo):
    with open(path_archivo, 'r') as file:
        for line in file:
            u, v = line.strip().split(':')
            m = v.split(",")
            l = list(u) + m

archivo =  'facil.txt'
cargar_archivo(archivo)


class Terreno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = set()

    def conectar(self, nodo):
        self.conexiones.add(nodo.nombre)

    def desconectar(self, nodo):
        self.conexiones.remove(nodo.nombre)

    def __repr__(self):
        return self.nombre


class Ciudad:

    def __init__(self, path):
        self.nodos = dict()
        with open(path, 'r') as file:
            for line in file:
                u, v = line.strip().split(':')
                m = v.strip().split(",")
                for i in m:
                    self.agregar_calle(u, i)

    def agregar_calle(self, origen, destino):

        nodo = self.nodos.get(origen)
        nodo2 = self.nodos.get(destino)

        if nodo is None:
            nodo = Terreno(origen)
            self.nodos[origen] = nodo

        if nodo2 is None:
            nodo2 = Terreno(destino)
            self.nodos[destino] = nodo

        self.nodos[origen] = nodo
        self.nodos[destino] = nodo2

        nodo.conectar(nodo2)

        return nodo

    def eliminar_calle(self, origen, destino):

        nodo = self.nodos.get(origen)
        nodo2 = self.nodos.get(destino)

        if nodo is None:
            nodo = Terreno(origen)
            self.nodos[origen] = nodo

        if nodo2 is None:
            nodo2 = Terreno(destino)
            self.nodos[destino] = nodo

        self.nodos[origen] = nodo
        self.nodos[destino] = nodo2

        nodo.desconectar(nodo2)

        return nodo

    @property
    def terrenos(self):
        return set(self.nodos.keys())


    @property
    def calles(self):
        fome = []
        for i in self.nodos.keys():
            for m in self.nodos.get(i).conexiones:
                fome.append((i,m))
        return fome


    def verificar_ruta(self, ruta,  visited=None):

        for i in range(0, len(ruta)):
            # Falta arreglar lo del valor del ultimo i + 1

            nodo_origen = self.nodos.get(ruta[i])

            if ruta[i] == ruta[i+1]:
                return True

            if visited is None:
                visited = []

            for nodo in nodo_origen.conexiones:
                if not nodo in visited:
                    visited.append(nodo)
                    if self.verificar_ruta(ruta):
                        return True

            return False


    def get_node(self, name):
        if name in self.nodos.keys():
            return self.nodos[name]
        return None


    def ruta_corta(self, origen, destino):

        if origen == destino:
            return True
        origen = self.get_node(origen)
        destino = self.get_node(destino)
        if origen is None or destino is None:
            return None
        cola = [[origen]]
        visited = list()
        while len(cola):
            current_path = cola.pop(0)
            current = current_path[-1]
            if current not in visited:
                lista_vecinos = [self.get_node(x) for x in current.conexiones]
                for vecino in lista_vecinos:
                    cola.append(list(current_path) + [vecino])
                    if vecino == destino:
                        return cola[-1]
                visited.append(current)
        return None

    def entregar_ruta(self, origen, destino):
        return self.ruta_corta(origen, destino)

    def ruta_entre_bombas(self, origen, *destinos):

        pass

    def ruta_corta_entre_bombas(self, origen, *destinos):

        pass

if __name__ == '__main__':

    facil = Ciudad("facil.txt")
    medio = Ciudad("medio.txt")
    dificil = Ciudad("dificil.txt")
    kratos = Ciudad("kratos.txt")

    ruta_facil = facil.entregar_ruta("C", "G")
    ruta_medio = medio.entregar_ruta("C", "A")
    ruta_difil = dificil.entregar_ruta("E", "L")
    ruta_kratos = kratos.entregar_ruta("M", "N")

    kratos.verificar_ruta(["A", "B"])

    print(ruta_facil)
    print(ruta_medio)
    print(ruta_difil)
    print(ruta_kratos)