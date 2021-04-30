from Lectura_archivos import *

# valor cambiado fue 60.869527749543934 por 10000 en centrales

class AsignarTipo:

    """
    Con clase lo que hago es agregar a el nodo el elemento (Casa, Central,...).
    este recibe un id y el tipo
    """
    def __init__(self, id_, tipo, tamaño, sistema_electrico):
        self.objeto = None
        self.sistema = sistema_electrico
        self.potencia = 20
        if tipo == "centrales":
            archivo = OpenFiles(tamaño, "centrales")
            datos = archivo.data()
            size = datos.size()
            i = 0
            while i < size:
                if datos.obtener(i) == "centrales":
                    pass

                elif datos.obtener(i).obtener(0) == id_:
                    id_ = datos.obtener(i).obtener(0)
                    nombre = datos.obtener(i).obtener(1)
                    sistema_electrico = datos.obtener(i).obtener(2)
                    provincia = datos.obtener(i).obtener(3)
                    comuna = datos.obtener(i).obtener(4)
                    tipo = datos.obtener(i).obtener(5)
                    potencia = datos.obtener(i).obtener(6)

                    self.objeto = Central(id_, nombre, sistema_electrico,
                                            provincia, comuna, tipo, potencia)
                i += 1

        elif tipo == "elevadoras" or tipo == "distribucion" or tipo == \
                "transmision":
            archivo = OpenFiles(tamaño, tipo)
            datos = archivo.data()
            size = datos.size()
            i = 0
            while i < size:
                if datos.obtener(i) == "elevadoras" or datos.obtener(i) == \
                        "transmision" or datos.obtener(i) == "distribucion":
                    pass

                elif datos.obtener(i).obtener(0) == id_:
                    id_ = datos.obtener(i).obtener(0)
                    nombre = datos.obtener(i).obtener(1)
                    sistema_electrico = datos.obtener(i).obtener(2)
                    provincia = datos.obtener(i).obtener(3)
                    comuna = datos.obtener(i).obtener(4)
                    consumo_mw = datos.obtener(i).obtener(5)

                    if tipo == "elevadoras":
                        self.objeto = Elevadoras(id_, nombre, sistema_electrico,
                                            provincia, comuna, consumo_mw)

                    elif tipo == "distribucion":
                        self.objeto = Distribucion(id_, nombre,
                                                   sistema_electrico,
                                                provincia, comuna, consumo_mw)

                    elif tipo == "transmision":
                        self.objeto = Transmision(id_, nombre,
                                                  sistema_electrico,
                                                  provincia, comuna, consumo_mw)
                i += 1

        elif tipo == "casas":
            archivo = OpenFiles(tamaño, "casas")
            datos = archivo.data()
            size = datos.size()
            i = 0
            while i < size:
                if datos.obtener(i) == "casas":
                    pass
                elif datos.obtener(i).obtener(0) == id_:
                    id_ = datos.obtener(i).obtener(0)
                    sistema_electrico = datos.obtener(i).obtener(1)
                    provincia = datos.obtener(i).obtener(2)
                    comuna = datos.obtener(i).obtener(3)
                    consumo_kw = datos.obtener(i).obtener(4)
                    self.objeto = Casas(id_, sistema_electrico,provincia,
                                        comuna, consumo_kw)
                i += 1

        if self.objeto == None :
            """
            Si se agrega un nodo que no existe, entonces le solitito los 
            datos para poder crear el objeto
            """
            id_ = id_
            sistema_electrico = input("Ingresa el sistema electrico \n")
            provincia = input("Ingresa la provincia\n")
            comuna = input("Ingresa la comuna\n")

            if tipo == "casas":
                consumo_kw = input("Ingresa el consumo en kW\n")
                self.objeto = Casas(id_, sistema_electrico, provincia,
                                        comuna, consumo_kw)

            elif tipo == "transmision":
                consumo_mw = input("Ingresa el consumo en MW")
                nombre = input("Ingresa el nombre de la transmisora\n")
                self.objeto = Transmision(id_, nombre,
                                          sistema_electrico,
                                          provincia, comuna, consumo_mw)
            elif tipo == "distribucion":
                consumo_mw = input("Ingresa el consumo en MW")
                nombre = input("Ingresa el nombre de la distribudora\n")
                self.objeto = Distribucion(id_, nombre,sistema_electrico,
                                           provincia, comuna, consumo_mw)
            elif tipo == "elevadoras":
                consumo_mw = input("Ingresa el consumo en MW")
                nombre = input("Ingresa el nombre de la elevadora\n")
                self.objeto = Elevadoras(id_, nombre, sistema_electrico,
                                         provincia, comuna, consumo_mw)
            elif tipo == "centrales":
                consumo_mw = input("Ingresa el consumo en MW")
                nombre = input("Ingresa el nombre de la central\n")

                if potencia == None:
                    self.potencia = input("Indique cuanta potencia va a "
                                          "aportar\n")
                else:
                    self.potencia = float(potencia)
                self.objeto = Central(id_, nombre, sistema_electrico,
                                      provincia, comuna, tipo, potencia)

    @property
    def potencia(self):
        return self.potencia_

    @potencia.setter
    def potencia(self, value):
        if value < 20:
            self.potencia_ = 20
        elif value > 200:
            self.potencia_ = 200
        else:
            self.potencia_ = value

    def data(self):
        if self.objeto.sistema != self.sistema:
            self.objeto = None

        return self.objeto


class Casas:
    def __init__(self, id_,sistema_electrico,provincia,comuna,consumo_kw):
        self.id_ = id_
        self.sistema = sistema_electrico
        self.provincia = provincia
        self.comuna = comuna
        self.consumo = float(consumo_kw)/1000
        self.nivel = "casas"


class Centrales:
    def __init__(self,id_,nombre,sistema_electrico,provincia,comuna):
        self.id_ = id_
        self.nombre = nombre
        self.nivel = "centrales"
        self.sistema = sistema_electrico
        self.provincia = provincia
        self.comuna = comuna


class Transmision(Centrales):
    def __init__(self,id_,nombre,sistema_electrico,provincia,comuna,
                 consumo_mw):
        super().__init__(id_,nombre,sistema_electrico,provincia,comuna)
        self.consumo = float(consumo_mw)
        self.nivel = "transmision"


class Distribucion(Centrales):
    def __init__(self,id_,nombre,sistema_electrico,provincia,comuna,consumo_mw):
        super().__init__(id_, nombre, sistema_electrico, provincia, comuna)
        self.consumo = float(consumo_mw)
        self.nivel = "distribucion"


class Central(Centrales):
    def __init__(self,id_,nombre,sistema_electrico,provincia,comuna,tipo,
                 potencia):
        super().__init__(id_, nombre, sistema_electrico, provincia, comuna)
        self.tipo = tipo
        self.consumo = float(potencia)
        self.nivel = "centrales"
        self.potencia = float(potencia)


class Elevadoras(Centrales):
    def __init__(self, id_, nombre, sistema_electrico, provincia, comuna,
                 consumo_mw):
        super().__init__(id_, nombre, sistema_electrico, provincia, comuna)
        self.consumo = float(consumo_mw)
        self.nivel = "elevadoras"


class Compact:
    def __init__(self, lista1, lista2, lista3, lista4):
        self.lista = NotList()

        tamaño = lista1.size()
        i = 0
        while i < tamaño:
            self.lista.insert(lista1.obtener(i))
            i += 1

        tamaño = lista2.size()
        i = 0
        while i < tamaño:
            self.lista.insert(lista2.obtener(i))
            i += 1

        tamaño = lista3.size()
        i = 0
        while i < tamaño:
            self.lista.insert(lista3.obtener(i))
            i += 1

        tamaño = lista4.size()
        i = 0
        while i < tamaño:
            self.lista.insert(lista4.obtener(i))
            i += 1

    def retornar(self):
        return self.lista


