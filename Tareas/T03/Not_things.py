
"""
Las siguientes clases son un poco "Frankestein". Tienen funciones obtenidas de:

1. https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
   -python/ y https://dbader.org/blog/python-linked-list
2. https://dbader.org/blog/python-linked-list
3. complementado por el material de clases
4. otras implementadas por mi
"""

# Material de Ayudantía


class Node:

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_previous(self, new_previous):
        self.previous_node = new_previous


class NotList:
    def __init__(self, head=None):
        self.head = head
        self.cola = None

    def insert(self, data):
        """
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
        -python/ y https://dbader.org/blog/python-linked-list
        """

        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def obtener(self, posicion):
        """
        Material de Ayudantia
        """

        nodo_actual = self.head

        tamaño = posicion
        i = 0
        while i < tamaño:
            if nodo_actual:
                nodo_actual = nodo_actual.next_node
            i += 1

        if not nodo_actual:
            return "Posición no encontrada"

        return nodo_actual.data

    def encontrar(self, nombre):
        nodo_actual = self.head
        posicion = 0

        tamaño = self.size()
        i = 0
        while i < tamaño:
            if nodo_actual.data != nombre:
                nodo_actual = nodo_actual.next_node
                posicion = i + 1
            i += 1

        if nodo_actual == None:
            posicion = 100000

        return posicion

    def size(self):
        """
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
        -python/ y https://dbader.org/blog/python-linked-list
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def insertar(self, valor, posicion):
        """
        Material de Ayudantia
        """

        nodo_nuevo = Node(valor)
        nodo_actual = self.head

        if posicion == 0:
            nodo_nuevo.next_node = self.head
            self.head = nodo_nuevo

            if nodo_nuevo.next_node is None:
                self.cola = nodo_nuevo

            return

        tamaño = posicion - 1
        i = 0
        while i < tamaño:
            if nodo_actual:
                nodo_actual = nodo_actual.next_node
            i += 1

        if nodo_actual is not None:
            nodo_nuevo.next_node = nodo_actual.next_node
            nodo_actual.next_node = nodo_nuevo

            if nodo_nuevo.next_node is None:
                self.cola = nodo_nuevo

    def remove(self, key):
        """
        https://dbader.org/blog/python-linked-list
        """

        curr = self.head
        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.get_next()

        if prev is None:
            self.head = curr.get_next()

        elif curr:
            prev.next_node = curr.get_next()
            curr.next_node = None

    def sort_especial(self, lista_mala, tipo):

        """
        Esta funcion recibe un arreglo que es una "lista" NotList el cual es el
        estado actual de la lista y la ordena para que quede en el formato
        que necesito para poder utilizarla y ser consistente con todo_ mi código
        """

        lista_aux = NotList()
        orden_actual = lista_mala.obtener(0)
        orden = "incorrecto"

        while orden != "correcto":
            if tipo == 'casas_casas' or tipo == "casas_distribucion" or tipo \
                    == "centrales_elevadoras" or tipo == \
                    "distribucion_transmision" or tipo == \
                    "transmision_elevadoras":

                if tipo == 'casas_casas':
                    dato0 = 'id_desde'
                    dato1 = 'id_hasta'
                    dato2 = 'distancia'

                elif tipo == "casas_distribucion":
                    dato0 = 'id_distribucion'
                    dato1 = 'id_casa'
                    dato2 = 'distancia'

                elif tipo == "centrales_elevadoras":
                    dato0 = 'id_central'
                    dato1 = 'id_elevadora'
                    dato2 = 'distancia'

                elif tipo == "distribucion_transmision":
                    dato0 = 'id_transmision'
                    dato1 = 'id_distribucion'
                    dato2 = 'distancia'

                else:
                    dato0 = 'id_elevadora'
                    dato1 = 'id_transmision'
                    dato2 = 'distancia'

                tamaño = lista_mala.size()
                i = 0
                while i < tamaño:
                    lista_aux2 = NotList()
                    lugar_id_desde = orden_actual.encontrar(dato0)
                    lugar_id_hasta = orden_actual.encontrar(dato1)
                    lugar_dist = orden_actual.encontrar(dato2)
                    lista_aux2.insertar(lista_mala.obtener(i).obtener(
                        lugar_id_desde), 0)
                    lista_aux2.insertar(lista_mala.obtener(i).obtener(
                        lugar_id_hasta), 1)
                    lista_aux2.insertar(
                        lista_mala.obtener(i).obtener(lugar_dist), 2)
                    lista_aux.insert(lista_aux2)
                    i += 1

            else:

                if tipo == 'casas':
                    dato0 = 'id'
                    dato1 = 'sistema_electrico'
                    dato2 = 'provincia'
                    dato3 = 'comuna'
                    dato4 = 'consumo_kw'

                    i = 0
                    tamaño2 = lista_mala.size()
                    while i < tamaño2:
                        lista_aux2 = NotList()
                        lugar_id = orden_actual.encontrar(dato0)
                        lugar_sist = orden_actual.encontrar(dato1)
                        lugar_prov = orden_actual.encontrar(dato2)
                        lugar_comuna = orden_actual.encontrar(dato3)
                        lugar_consumo = orden_actual.encontrar(dato4)

                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_id), 0)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_sist), 1)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_prov), 2)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_comuna), 3)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_consumo), 4)

                        lista_aux.insert(lista_aux2)
                        i += 1

                elif tipo == "centrales":
                    dato0 = 'id'
                    dato1 = 'nombre'
                    dato2 = 'sistema_electrico'
                    dato3 = 'provincia'
                    dato4 = 'comuna'
                    dato5 = 'tipo'
                    dato6 = 'potencia'

                    i = 0
                    tamaño3 = lista_mala.size()
                    while i < tamaño3:

                        lista_aux2 = NotList()
                        lugar_id = orden_actual.encontrar(dato0)
                        lugar_nombre = orden_actual.encontrar(dato1)
                        lugar_sist = orden_actual.encontrar(dato2)
                        lugar_prov = orden_actual.encontrar(dato3)
                        lugar_comuna = orden_actual.encontrar(dato4)
                        lugar_tipo = orden_actual.encontrar(dato5)
                        lugar_consumo = orden_actual.encontrar(dato6)

                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_id), 0)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_nombre), 1)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_sist), 2)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_prov), 3)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_comuna), 4)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_tipo), 5)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_consumo), 6)

                        lista_aux.insert(lista_aux2)
                        i += 1

                elif tipo == "distribucion" or tipo == "elevadoras" or tipo \
                        == "transmision":

                    dato0 = 'id'
                    dato1 = 'nombre'
                    dato2 = 'sistema_electrico'
                    dato3 = 'provincia'
                    dato4 = 'comuna'
                    dato5 = 'consumo_mw'

                    i = 0
                    tamaño4 = lista_mala.size()
                    while i < tamaño4:
                        lista_aux2 = NotList()
                        lugar_id = orden_actual.encontrar(dato0)
                        lugar_nombre = orden_actual.encontrar(dato1)
                        lugar_sist = orden_actual.encontrar(dato2)
                        lugar_prov = orden_actual.encontrar(dato3)
                        lugar_comuna = orden_actual.encontrar(dato4)
                        lugar_consumo = orden_actual.encontrar(dato5)

                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_id), 0)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_nombre), 1)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_sist), 2)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_prov), 3)
                        lista_aux2.insertar(
                            lista_mala.obtener(i).obtener(lugar_comuna), 4)
                        lista_aux2.insertar(lista_mala.obtener(i).obtener(
                            lugar_consumo), 5)

                        lista_aux.insert(lista_aux2)
                        i += 1

            orden = "correcto"

        return lista_aux

    def __repr__(self):
        string = ""

        tamaño = self.size()
        i = 0
        while i < tamaño:
            string += str(self.obtener(i)) + ", "
            i += 1

        return "[ " + string[:len(string) - 2] + " ]"


class NodeDict:

    def __init__(self, key = None, value = None, next_node = None):
        self.data = key
        self.next_node = next_node
        self.value = value

    def get_data(self):
        return

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_previous(self, new_previous):
        self.previous_node = new_previous

    def __repr__(self):
        return str(self.data) + " : " + str(self.value)


class NotDict:

    """
    Mi NotDict tambien lo puedo usar como set de cosas que no uso
    """

    def __init__(self):
        self.head = None
        self.cola = Node

    def set_value(self, key, value = None):

        tamaño = self.size()
        i = 0
        while i < tamaño:
            if self.obtener(i).data == key:
                self.obtener(i).value = value
            i += 1

    def get_value(self, key):

        tamaño = self.size()
        i = 0
        while i < tamaño:
            if self.obtener(i).data == key:
                return self.obtener(i).value
            i += 1

            # else:
                # return self.agregar(key, None)

    def agregar(self, other_key = None,  other_value = None):
        """
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
        -python/ y https://dbader.org/blog/python-linked-list
        """

        chequeador = 0

        tamaño = self.size()
        i = 0
        while i < tamaño:
            if self.obtener(i).data == other_key:
                chequeador += 1
                self.obtener(i).value = other_value
            i += 1

        if chequeador == 0:
            new_node = NodeDict(other_key, other_value)
            new_node.set_next(self.head)
            self.head = new_node

    def size(self):

        """
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in
        -python/ y https://dbader.org/blog/python-linked-list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def obtener(self, posicion):
        """
        Ayudantia
        """
        nodo_actual = self.head

        tamaño = posicion
        i = 0
        while i < tamaño:
            if nodo_actual:
                nodo_actual = nodo_actual.next_node

            i += 1

        if not nodo_actual:
            return "Posición no encontrada"

        return nodo_actual

    def remove(self, key):
        """
        https://dbader.org/blog/python-linked-list
        """
        curr = self.head
        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.get_next()

        if prev is None:
            self.head = curr.get_next()

        elif curr:
            prev.next_node = curr.get_next()
            curr.next_node = None

    def keys(self):
        lista_keys = NotList()
        tamaño = self.size()
        i = 0
        while i < tamaño:
            lista_keys.insert(self.obtener(i).data)
            i += 1

        return lista_keys

    def __repr__(self):
        string = ""

        tamaño = self.size()
        i = 0
        while i < tamaño:
            string += str(self.obtener(i)) + ", "
            i += 1

        return "{ " + string[:len(string) - 2] + " }"


