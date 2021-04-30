from Elementos_grafo import *
from Exceptions import *

rho = float(0.0172)  # esta medida es (mm^2)(Amperes)/km,

"""
Estas dos funciones son basadas en las de la ayudantía 7, la cual adapte a 
mis funciones creadas 60.869527749543934
"""

class GraphNode:
    def __init__(self, id, tipo, tamaño, sistema_electrico):
        """
        Usamos NotDict agregandole keys, los cuales tendran siempre como value
        None
        """
        var = AsignarTipo(id, tipo, tamaño, sistema_electrico)
        self.elemento = var.data()
        self.en_funcion = None
        self.nombre = id
        self.conexiones = NotDict()
        self.tipo = tipo
        self.sistema = sistema_electrico
        self.padres = 0
        self.lista = NotDict()
        if self.elemento != None:
            self.demanda_real = float(self.elemento.consumo)
            self.demanda = self.elemento.consumo
        else:
            self.demanda_real = 0
            self.demanda = 0
        self.potencia_demandada = 0
        self.potencia_recibida = 0

    def conectar(self, nodo, distancia):
        if nodo != None and nodo.elemento.sistema == self.sistema:
            """
            Aca tengo que hacer el calculo y el valor será el resultado
            """
            nodo.padres += 1
            if nodo.tipo == "casas" and self.tipo == "casas":
                area = 85
            elif nodo.tipo == "casas" and self.tipo == "distribucion":
                area = 85
            elif nodo.tipo == "distribucion" and self.tipo == "transmision":
                area = 152
            elif nodo.tipo == "transmision" and self.tipo == "elevadoras":
                area = 202.7
            else: # centrales y elevadoras
                area = 253
            nodo.lista = NotDict()
            nodo.lista.agregar("demanda", float(nodo.demanda_real))
            nodo.lista.agregar("padres", int(nodo.padres))
            nodo.lista.agregar("area", area)
            nodo.lista.agregar("distancia", float(distancia))
            self.conexiones.agregar(nodo)
        else: # no conecto
            pass

    def desconectar(self, nodo):
        self.conexiones.remove(nodo)

class Graph:

    def __init__(self, sistema_electrico):
        """
        En este diccionario el key es el objeto que esta asignado y el value
        va ser tambien el objeto
        """
        self.nodos = NotDict()
        self.sistema = sistema_electrico
        self.overload = False
        """
        le asigne por default el small, para evitarme posibles problemas
        """
        self.tamaño = "small"

    def _crear_nodo(self, tipo, id):
        """
        Aqui el nombre va a ser el id de la casa, central,.. etc y el tipo a
        qu infraestructura corresponde
        """
        chequeador = 0
        tamaño = self.nodos.keys().size()
        i = 0
        while i < tamaño:
            """
            self.nodos.keys().size() tiene objetos o de la clase Casa,
            Distribucion ...
            """
            if self.nodos.keys().obtener(i).nombre == id and self.nodos.keys(
            ).obtener(i).tipo == tipo:
                chequeador += 1
                nodo = self.nodos.keys().obtener(i)
            i += 1
        if chequeador == 0:
            nodo = GraphNode(id, tipo, self.tamaño, self.sistema)

            """
            Agrego a mi diccionario de nodos el nodo creado pero con value None
            """
            if nodo.elemento != None:
                self.nodos.agregar(nodo)
                return nodo
            else:
                # No es del sistema
                return
        else:
            return nodo

    def agregar_conexion(self, tipo_conexion, id_origen, id_destino, distancia):

        if tipo_conexion == 'centrales_elevadoras':
            tipo_origen = 'centrales'
            tipo_destino = 'elevadoras'
        elif tipo_conexion == 'transmision_elevadoras':
            tipo_origen = 'elevadoras'
            tipo_destino = 'transmision'
        elif tipo_conexion == 'distribucion_transmision':
            tipo_origen = 'transmision'
            tipo_destino = 'distribucion'
        elif tipo_conexion == 'casas_distribucion':
            tipo_origen = 'distribucion'
            tipo_destino = 'casas'
        else: # tipo_conexion == 'casas_casas':
            tipo_origen = 'casas'
            tipo_destino = 'casas'
        nodo_origen = self._crear_nodo(tipo_origen, id_origen)
        nodo_destino = self._crear_nodo(tipo_destino, id_destino)

        """
        Le agrego a la conexion el nodo de destino que es un objeto de la clase 
        GraphNode
        """
        if nodo_origen != None:
            nodo_origen.conectar(nodo_destino, distancia)

    def quitar_conexion(self, origen, destino):
        nodo_origen = self.nodos.keys().encontrar(origen)
        nodo_destino = self.nodos.keys().encontrar(destino)
        nodo_origen.desconectar(nodo_destino)

    def cargar_archivo(self, tamaño, direccion):
        archivo = OpenFiles(tamaño, direccion)
        self.tamaño = tamaño
        self.direccion = direccion
        datos = archivo.data()
        tamaño = datos.size()
        i = 0
        while i < tamaño:
            if datos.obtener(i) == "casas_casas" or \
                    datos.obtener(i) == "casas_distribucion" or \
                    datos.obtener(i) == "centrales_elevadoras" or \
                    datos.obtener(i) == "distribucion_transmision" or \
                    datos.obtener(i) == "transmision_elevadoras" :
                tipo = datos.obtener(i)
            else:
                self.agregar_conexion(tipo, datos.obtener(i).obtener(0),
                                      datos.obtener(i).obtener(1),
                                      datos.obtener(i).obtener(2))
            i += 1

    def demanda_real(self):
        archivo1 = OpenFiles(self.tamaño, "casas_casas")
        datos1 = archivo1.data()
        archivo2 = OpenFiles(self.tamaño, "casas_distribucion")
        datos2 = archivo2.data()
        archivo3 = OpenFiles(self.tamaño, "distribucion_transmision")
        datos3 = archivo3.data()
        archivo4 = OpenFiles(self.tamaño, "transmision_elevadoras")
        datos4 = archivo4.data()
        archivo = Compact(datos4, datos3, datos2, datos1)
        datos = archivo.retornar()

        tamaño = datos.size()
        i = 0
        while i < tamaño:
            if datos.obtener(i) == "casas_casas" or \
                    datos.obtener(i) == "casas_distribucion" or \
                    datos.obtener(i) == "centrales_elevadoras" or \
                    datos.obtener(i) == "distribucion_transmision" or \
                    datos.obtener(i) == "transmision_elevadoras":
                i_origen = None
                i_destino = None
            else:
                i_origen = datos.obtener(i).obtener(0)
                i_destino = datos.obtener(i).obtener(1)

            tamaño2 = self.nodos.keys().size()
            l = 0
            while l < tamaño2:
                if self.nodos.keys().obtener(l) == \
                        "Posición no encontrada":
                    pass

                elif self.nodos.keys().obtener(l).elemento.id_ == i_origen \
                        and self.nodos.keys().obtener(l).elemento.nivel != \
                        "centrales":

                    distancia_conexion = datos.obtener(i).obtener(2)

                    tamaño3 = self.nodos.keys().obtener(l).conexiones.size()
                    m = 0
                    while m < tamaño3:
                        if self.nodos.keys().obtener(l).conexiones.keys().\
                                obtener(m).elemento.id_ == i_destino:

                            distancia = float(distancia_conexion)
                            demanda_nodo = self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).demanda_real
                            area = self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).lista.get_value("area")
                            n_padres_nodo =self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).lista.get_value("padres")

                            formula = (demanda_nodo/ n_padres_nodo) / (1 - (
                                    rho * distancia) / area)

                            self.nodos.keys().obtener(l).demanda_real\
                                += formula
                        m += 1
                l += 1
            i += 1

    def valor_centrales(self):
        archivo1 = OpenFiles(self.tamaño, "centrales_elevadoras")
        datos = archivo1.data()

        tamaño = datos.size()
        i = 0
        while i < tamaño:
            if datos.obtener(i) == "centrales_elevadoras":
                i_origen = None
                i_destino = None
            else:
                i_origen = datos.obtener(i).obtener(0)
                i_destino = datos.obtener(i).obtener(1)

            tamaño2 = self.nodos.keys().size()
            l = 0
            while l < tamaño2:
                if self.nodos.keys().obtener(l) == \
                        "Posición no encontrada":
                    pass

                elif self.nodos.keys().obtener(l).elemento.id_ == i_origen:
                    tamaño3 = self.nodos.keys().obtener(l).conexiones.size()
                    m = 0

                    while m < tamaño3:
                        if self.nodos.keys().obtener(l).conexiones.keys().\
                                obtener(m).elemento.id_ == i_destino:
                            demanda_nodo = self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).demanda_real
                            n_padres_nodo =self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).lista.get_value("padres")

                            self.nodos.keys().obtener(l).potencia_demandada += \
                                (demanda_nodo / n_padres_nodo)
                        m += 1
                l += 1
            i += 1

    def flujo(self):
        self.falta = "no"

        tamaño = self.nodos.keys().size()
        l = 0
        while l < tamaño:
            if self.nodos.keys().obtener(l) == \
                    "Posición no encontrada":
                pass

            else:
                if self.nodos.keys().obtener(l).tipo == "centrales":
                    suma = 0
                    tamaño2 = self.nodos.keys().obtener(l).conexiones.size()
                    m = 0
                    while m < tamaño2:

                        area = self.nodos.keys().obtener(
                            l).conexiones.keys().obtener(
                            m).lista.get_value("area")

                        distancia = self.nodos.keys().obtener(
                            l).conexiones.keys().obtener(
                            m).lista.get_value("distancia")

                        M = (self.nodos.keys().obtener(l).conexiones.keys(
                        ).obtener(m).demanda_real) / (1 - rho * distancia /area)

                        suma += M
                        m += 1

                    tamaño2 = self.nodos.keys().obtener(l).conexiones.size()
                    m = 0
                    while m < tamaño2:

                        M = (self.nodos.keys().obtener(l).conexiones.keys(
                        ).obtener(m).demanda_real)/(1 - rho * distancia / area)
                        proporcion = M / suma
                        potencia = self.nodos.keys().obtener(
                            l).elemento.potencia * proporcion
                        formula = (rho * distancia / area) * potencia
                        potencia -= formula
                        self.nodos.keys().obtener(
                            l).conexiones.keys().obtener(
                            m).potencia_recibida \
                            += potencia
                        m += 1
            l += 1

        list_aux = NotList()
        list_aux.insert("casas")
        list_aux.insert("distribucion")
        list_aux.insert("transmision")
        list_aux.insert("elevadoras")

        tamaño = 5
        i = 0
        while i < tamaño:
            tamaño2 = self.nodos.keys().size()
            l = 0
            while l < tamaño2:
                if self.nodos.keys().obtener(l) == \
                        "Posición no encontrada":
                    pass

                else:
                    if self.nodos.keys().obtener(l).tipo == list_aux.obtener(i):
                        suma = 0
                        tamaño3 = self.nodos.keys().obtener(l).conexiones.size()
                        m = 0
                        while m < tamaño3:
                            area = self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).lista.get_value("area")

                            distancia = self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).lista.get_value("distancia")

                            M = (self.nodos.keys().obtener(l).conexiones.keys(
                            ).obtener(m).demanda_real) / (1 - rho * distancia
                                                          / area)
                            suma += M
                            m += 1

                        tamaño4 = self.nodos.keys().obtener(l).conexiones.size()
                        m = 0
                        while m < tamaño4:
                            M = (self.nodos.keys().obtener(l).conexiones.keys(
                            ).obtener(m).demanda_real) / (
                                            1 - rho * distancia / area)

                            proporcion = M / suma
                            potencia = (self.nodos.keys().obtener(
                                l).potencia_recibida - self.nodos.keys(
                            ).obtener(l).elemento.consumo) * proporcion
                            formula = (rho * distancia / area) * potencia
                            potencia -= formula

                            self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).potencia_recibida \
                                += potencia

                            if self.nodos.keys().obtener(
                                l).conexiones.keys().obtener(
                                m).potencia_recibida < 0:

                                self.nodos.keys().obtener(
                                    l).conexiones.keys().obtener(
                                    m).potencia_recibida = 0
                                self.falta = "si"

                            if self.nodos.keys().obtener(l).tipo == "casas":
                                if self.nodos.keys().obtener(
                                        l).conexiones.keys().obtener(
                                        m).potencia_recibida > 30000:
                                    self.overload = True
                                    self.exceso = self.nodos.keys().obtener(
                                    l).conexiones.keys().obtener(
                                    m).potencia_recibida
                                    raise ElectricalOverload("Hay overload")
                            m += 1
                l += 1
            i += 1

    def agregar_arista(self, id_origen, tipo_origen, id_destino,
                       tipo_destino, distancia):
        """
        Recibo el id de una casa y evalúo si se puede agregar la conexion
        """
        c_origen = ""
        c_destino = "."
        nodo_destino = None

        tamaño = self.nodos.keys().size()
        i = 0
        while i < tamaño:
            if self.nodos.keys().obtener(i).tipo == tipo_origen:
                if self.nodos.keys().obtener(i).elemento.id_ == id_origen:
                    c_origen = self.nodos.keys().obtener(i).elemento.comuna
                    nodo_origen = self.nodos.keys().obtener(i)

            if self.nodos.keys().obtener(i).tipo == tipo_destino:
                if self.nodos.keys().obtener(i).elemento.id_ == id_destino:
                    c_destino = self.nodos.keys().obtener(i).elemento.comuna
                    nodo_destino = self.nodos.keys().obtener(i)
            i += 1

        if nodo_destino == None:
            self._crear_nodo(tipo_destino, id_destino)
            tamaño = self.nodos.keys().size()
            i = 0
            while i < tamaño:
                if self.nodos.keys().obtener(i).tipo == tipo_destino:
                    if self.nodos.keys().obtener(i).elemento.id_ == \
                          id_destino:
                        c_destino = self.nodos.keys().obtener(
                             i).elemento.comuna
                        nodo_destino = self.nodos.keys().obtener(i)
                i += 1

        if tipo_origen == "elevadoras" or tipo_origen == "centrales" or \
                tipo_destino == "elevadoras" or tipo_destino == "centrales" \
                or tipo_destino == "transmision" or tipo_origen == \
                "transmision":
            if tipo_origen == "casas" or tipo_destino == "casas":
                raise ForbiddenAction(tipo_destino, tipo_origen)

        if tipo_destino == "transmision" and tipo_origen == "elevadoras":
            tamaño = self.nodos.keys().size()
            i = 0
            while i < tamaño:
                if self.nodos.keys().obtener(i).tipo == tipo_origen:
                    tamaño2 = self.nodos.keys().obtener(i).conexiones.size()
                    m = 0
                    while m < tamaño2:
                        if self.nodos.keys().obtener(i).conexiones.keys(
                        ).obtener(m).elemento.id_ == id_destino:
                            raise ForbiddenAction("Ya tiene una elevadora")
                        m += 1
                i += 0

        if tipo_destino == "distribucion" and tipo_origen == "transmision":
            tamaño3 = self.nodos.keys().size()
            i = 0
            while i < tamaño3:
                if self.nodos.keys().obtener(i).tipo == tipo_origen:
                    tamaño4 = self.nodos.keys().obtener(i).conexiones.size()
                    m = 0
                    while m < tamaño4:
                        if self.nodos.keys().obtener(i).conexiones.keys(
                        ).obtener(m).elemento.id_ == id_destino:
                            raise ForbiddenAction("ya tiene una "
                                                  "subestacion "
                                                  "transmisora")
                        m += 1
                i += 1

        if nodo_destino == None:
            raise ForbiddenAction("no")

        tamaño5 = nodo_destino.conexiones.size()
        i = 0
        while i < tamaño5:
            if nodo_destino.conexiones.keys().obtener(
                    i).elemento.id_ == id_origen:
                raise ForbiddenAction("ciclo")
            i += 1

        if tipo_destino == "centrales" and tipo_origen == "elevadora":
            self.agregar_conexion("centrales_elevadoras", id_origen,
                                  id_destino, distancia)

        elif c_destino == c_origen and tipo_origen == "casas" and \
              tipo_destino\
                =="casas":
            self.agregar_conexion("{}_{}".format(tipo_destino, tipo_origen),
                                  id_origen, id_destino, distancia)

        elif c_destino != c_origen and tipo_origen == "casas" and \
              tipo_destino\
                =="casas":
            raise ForbiddenAction("no estan en la misma comuna")
        else:
            self.agregar_conexion("{}_{}".format(tipo_destino, tipo_origen),
                                  id_origen, id_destino, distancia)
        self.flujo()
        if self.overload == True:
             raise ElectricalOverload(self.exceso, "agregar_nodo")

    def remover_arista(self, id_origen, tipo_origen, id_destino, tipo_destino):
        tamaño = self.nodos.keys().size()
        i = 0
        while i < tamaño:
            if self.nodo.keys().obtener(i).elemento.id_ == id_origen and \
                    self.nodo.keys().obtener(i).tipo == tipo_origen:
                tamaño2 = self.nodos.keys().obtener(i).conexiones.keys().size()
                m = 0
                while m < tamaño2:
                    if self.nodos.keys().obtener(i).conexiones.keys(
                ).obtener(m).elemento.id_ == id_destino and self.nodos.keys(
                    ).obtener(i).conexiones.keys().obtener(m).tipo == \
                            tipo_destino:
                        self.nodos.keys().obtener(i).desconectar(
                            self.nodos.keys().obtener(i).conexiones.keys(
                            ).obtener(m))
                    m += 1
            i += 1

    def check_nodo_add(self, tipo_destino, id_destino, conexion, tipo_origen
                       = None,id_origen = None, distancia = None):
        """
        En esta funcion recibo los parametros para simplemente agregar un
        nodo o tambien agregarlo a mi red, ya que si no se une no afecta la
        red. El chequeo de la validez se hace en agregar arista. Y la de
        Electrical overload se hace cuando se recalcula el flujo por nodo en
        flujo()
        """
        self.en_funcion = "nodo_radd"

        if conexion == "si":
            nodo_destino = self._crear_nodo(tipo_destino, id_destino)
            nodo_origen = self._crear_nodo(tipo_origen, id_origen)
            self.flujo()
            var = self.falta
            if var == "si":
                self.agregar_arista(id_origen, tipo_origen, id_destino,
                                    tipo_destino, distancia)
        else:
            """
            No nesesariamente se va a querer unir el nodo a la red
            """
            self._crear_nodo(tipo_destino, id_destino)

    def check_nodo_remove(self, tipo, id):
        """
        busco el id y el tipo
        """
        self.en_funcion = "nodo_remove"
        tamaño = self.nodos.keys().size()
        i = 0
        while i < tamaño:
            if self.nodos.keys().obtener(i).elemento.id_ == id and \
                    self.nodos.keys().obtener(i).tipo == tipo:
                conexiones = self.nodos.keys().obtener(i).conexiones.size()
                while conexiones > 0:
                    tamaño2 = self.nodos.keys().obtener(i).conexiones.size()
                    m = 0
                    while m < tamaño2:
                        self.nodos.keys().obtener(i).desconectar(
                            self.nodos.keys().obtener(i).conexiones.keys(
                            ).obtener(m))
                        m += 1
                    conexiones -= 1
            i += 1
        desconectado_completamente = False
        while desconectado_completamente == False:
            tamaño = self.nodos.keys().size()
            i = 0
            while i < tamaño:
                tamaño2 = self.nodos.keys().obtener(i).conexiones.size()
                m = 0
                while m < tamaño2:
                    if self.nodos.keys().obtener(i).conexiones.keys(
                       ).obtener(m).elemento.id_ == id and self.nodos.keys(
                       ).obtener(i).conexiones.keys().obtener(m).tipo == tipo:
                        self.nodos.keys().obtener(i).desconectar(
                            self.nodos.keys().obtener(i).conexiones.keys(
                            ).obtener(m))
                    m += 1
                i += 1
            desconectado_completamente = True
        tamaño  = self.nodos.keys().size()
        i = 0
        while i < tamaño:
            if self.nodos.keys().obtener(i).elemento.id_ == id and \
                    self.nodos.keys().obtener(i).tipo == tipo:
                self.nodos.remove(self.nodos.keys().obtener(i))
                break
            i += 1
        self.flujo()
        if self.overload == True:
            raise ElectricalOverload(self.exceso, "remover_nodo")


if __name__ == '__main__':

    Grafo = Graph("SING")
    Grafo.cargar_archivo("small", "centrales_elevadoras")
    Grafo.cargar_archivo("small", "casas_distribucion")
    Grafo.cargar_archivo("small", "distribucion_transmision")
    Grafo.cargar_archivo("small", "transmision_elevadoras")
    Grafo.cargar_archivo("small", "casas_casas")
    Grafo.demanda_real()
    Grafo.flujo()
