import csv
from Not_things import *

# Utilize en codigo de https://docs.python.org/2/library/csv.html para
# aprender a abrir archivos.

class TransformacionArchivos:

    def __init__(self, *args):
        self.lista = NotList()
        for n in args:
            self.lista.insert(n)

    def transformado(self):
        return self.lista

class OpenFiles:
    def __init__(self, tamaño, direccion):
        self.direccion = direccion
        with open('bd/{}/{}.csv'.format(tamaño, direccion)) as csvfile:
            self.lista_archivo = NotList()
            transformacion = TransformacionArchivos(*csv.reader(csvfile))
            tamaño = transformacion.transformado().size()
            i = 0
            while i < tamaño:
                var2 = TransformacionArchivos(*transformacion.lista.obtener(i))
                self.lista_archivo.insert(var2.lista)
                i += 1

        lista_aux = NotList()

        tamaño = self.lista_archivo.size()
        i = 0
        while i < tamaño:
            if self.lista_archivo.obtener(i).size() < 3:
                lista_aux.insert(self.lista_archivo.obtener(i))
            i += 1

        tamaño = lista_aux.size()
        i = 0
        while i < tamaño:
            self.lista_archivo.remove(lista_aux.obtener(i))
            i += 1

    def data(self):

        """
        Aca hago el sort y le agrego el tipo para despues poder hacer las
        clases
        """

        lista_aux = self.lista_archivo.sort_especial(self.lista_archivo,
                                              self.direccion)
        lista_aux2 = NotList()

        tamaño = lista_aux.size()
        i = 0
        while i < tamaño:
            if lista_aux.obtener(i).obtener(2) == "distancia" or \
                    lista_aux.obtener(i).obtener(0) == "id":
                lista_aux2.insert(lista_aux.obtener(i))
            i += 1

        tamaño = lista_aux2.size()
        i = 0
        while i < tamaño:
            lista_aux.remove(lista_aux2.obtener(i))
            i += 1

        lista_aux.insert(self.direccion)

        return lista_aux

if __name__ == '__main__':
    var = OpenFiles("large","casas")

