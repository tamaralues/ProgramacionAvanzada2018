import unittest
from Consultas import *


class MostrarAsserts(unittest.TestCase):
    def setUp(self):
        self.sistema = "SING"
        self.tamaño = "small"
        self.Grafo = Graph(self.sistema)
        self.Grafo.cargar_archivo(self.tamaño, "centrales_elevadoras")
        self.Grafo.cargar_archivo(self.tamaño, "casas_distribucion")
        self.Grafo.cargar_archivo(self.tamaño, "distribucion_transmision")
        self.Grafo.cargar_archivo(self.tamaño, "transmision_elevadoras")
        self.Grafo.cargar_archivo(self.tamaño, "casas_casas")
        self.Grafo.demanda_real()
        self.Grafo.flujo()

    def test_consumo_sub(self):

        # El consumo de la substación distribucion con id 220 fue de
        # 11.90359449380347

        self.tipo = "distribucion"
        self.id = "220"
        self.consumo = "11.90359449380347"

        res = "El consumo de la subestación {} con id {} fue de {}".format(
            self.tipo, self.id, self.consumo)

        self.assertEqual(consumo_sub("small", "220", "distribucion", "SING"),
                         res)

    def test_casa_mayor(self):
        self.formato = "mayor"
        self.id = "1497"
        self.nombre = "casas"
        self.provincia = "TOCOPILLA"
        self.comuna = "MARIA ELENA"

        res = "El cliente de {} con id {} es el con mayor consumo eléctrico " \
              "ubicado en {} , {}".format(self.nombre, self.id, self.provincia,
                                          self.comuna)

        self.assertEqual(consumo_casa(self.formato, self.Grafo), res)

    def test_casa_menor(self):

        self.formato = "menor"
        self.id = "1497"
        self.nombre = "casas"
        self.provincia = "TOCOPILLA"
        self.comuna = "MARIA ELENA"

        res = "El cliente de {} con id {} es el con menor consumo eléctrico " \
               "ubicado en {} , {}".format(self.nombre, self.id, self.provincia,
                                           self.comuna)

        self.assertEqual(consumo_casa(self.formato, self.Grafo), res)

    def consumo_comuna(self):
        self.str = ""
        self.suma_demanda = ""
        self.promedio = ""

        res = "El consumo total de la demanda en la comuna {} fue: {}\n Y el " \
           "porcentaje es {} %".format(self.str, self.suma_demanda,
                                       self.promedio)

        self.assertEqual(energia_total_comuna(str, self.tamaño, self.sistema),
                         res)

suite = unittest.TestLoader().loadTestsFromTestCase(MostrarAsserts)
unittest.TextTestRunner().run(suite)


"""
class MostrarExceptions(unittest.TestCase):
    def setUp(self):
        Grafo = Graph("SING")
        Grafo.cargar_archivo("small", "centrales_elevadoras")
        Grafo.cargar_archivo("small", "casas_distribucion")
        Grafo.cargar_archivo("small", "distribucion_transmision")
        Grafo.cargar_archivo("small", "transmision_elevadoras")
        Grafo.cargar_archivo("small", "casas_casas")
        Grafo.demanda_real()
        Grafo.flujo()

    def test_c(self):
        pass
"""


