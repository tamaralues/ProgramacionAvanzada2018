import unittest

###############################################################################
"""
Tests
Acá escribe los test pedidos.
"""

class RepeatedError(Exception):
    def __init__(self, codigo):
        # Sobreescribimos el __init__ para cambiar el ingreso de los parámetros
        super().__init__("{} ya estaa siendo utilizado".format(codigo))

class InconsistencyError(Exception):
    def __init__(self):
        # Sobreescribimos el __init__ para cambiar el ingreso de los parámetros
        super().__init__("carros de compra de distintos supermercados")

# verificar nombre del producto

def add_producto(producto):
    # Hay un espacio en la sigla
    simbolos_ = ""
    for i in "-&%#@*()":
        if i in producto:
            simbolos_ += i

    if simbolos_ != "":
        raise ValueError('El código posee un caracter inválido {}'.format(i))
        # La seccion vino escrita como todas en vez del numero

# verificar descuento


def descuento(descuento):

    if not (float(descuento) >= 0 and float(descuento) <= 0.5):
        raise ValueError("descuento no est ́a entre 0% y 50%")

# verificar precio negativo


def precio_negativo(precio):

    if not int(precio) >= 0:
        raise ValueError("cantidad menor que 0")


def cantidad_pedido(pedido):

    # La seccion fue ingresada con texto en el formato "section N"
    if int(pedido)<= 0:
        raise ValueError('cantidad menor que 0')

# codigos será una lista


def existencia(producto, codigos):

    if producto not in codigos:
       raise KeyError("el producto no existe en el supermercado")


def ex_supermercado(codigo, supermercado):
    if codigo in supermercado:
        raise RepeatedError(codigo)

def suma_compras(carro1, carro2):
    if carro1 != carro2:
        raise InconsistencyError

###############################################################################

class supermercado:
    def __init__(self):
        self.
        pass


    def add_producto(self, producto):
        # Hay un espacio en la sigla
        simbolos_ = ""
        for i in "-&%#@*()":
            if i in producto:
                simbolos_ += i

        if simbolos_ != "":
            raise ValueError(
                'El código posee un caracter inválido {}'.format(i))
            # La seccion vino escrita como todas en vez del numero

    # verificar descuento

    def descuento(self, descuento):

        if not (float(descuento) >= 0 and float(descuento) <= 0.5):
            raise ValueError("descuento no est ́a entre 0% y 50%")

    # verificar precio negativo

    def precio_negativo(self, precio):

        if not int(precio) >= 0:
            raise ValueError("cantidad menor que 0")

    def cantidad_pedido(self, pedido):

        # La seccion fue ingresada con texto en el formato "section N"
        if int(pedido) <= 0:
            raise ValueError('cantidad menor que 0')

    # codigos será una lista

    def existencia(self, producto, codigos):

        if producto not in codigos:
            raise KeyError("el producto no existe en el supermercado")

    def ex_supermercado(self, codigo, supermercado):
        if codigo in supermercado:
            raise RepeatedError(codigo)

    def suma_compras(self,carro1, carro2):
        if carro1 != carro2:
            raise InconsistencyError

###############################################################################

if __name__ == '__main__':
    unittest.main()
