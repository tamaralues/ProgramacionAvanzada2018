# Acá va lo relacionado con el procesamiento de datos
from PyQt5.QtCore import QObject, pyqtSignal, QRect
from PyQt5.Qt import QTest
from os import urandom
import hashlib
from csv import DictReader


class CheckInput(QObject):

    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal1 = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__()

        # Se conecta la señal check_signal con la función open_window del
        # parent (MainWindow).

        self.check_signal1.connect(parent.open_window)

    def check(self, name):
        # self.check_signal.emit(True)

        """
        Función que chequea que la cuenta tenga bien el formato del nombre en
        el caso de superarlo, envia una señal
        True al frontend.
        """

        if name == "Registrarse":
            self.check_signal1.emit(1)

        elif name == "Ingresar":
            self.check_signal1.emit(0)


class CheckReg(QObject):

    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal1 = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()

        # Se conecta la señal check_signal con la función open_window del
        # parent (MainWindow).
        self.parent = parent

        self.check_signal1.connect(parent.open_window)

    def check(self, dir):

        """
        Función que chequea que la cuenta tenga bien el formato del nombre en
        el caso de superarlo, envia una señal
        True al frontend.
        """

        lista = ["yellow", "blue", "pink", "red", "purple"]
        if type(dir) != list:
            dir = dir.split(",")

        print(dir)

        if dir[0] == "Volver":
            self.check_signal1.emit([0])

        elif type(dir) == list and len(dir) > 1 and dir[1] not in lista:
            """
            Aca tengo que poner los chequeos
            """

            """
            Chequeamos que el nombre de usuario no exista
            """

            mensaje = {"status": "nuevo_usuario", "nombre_usuario": str(dir[0]),
                       "clave": str(dir[1]), "la_salt" : str(dir[2])}

        if dir[0] == "no existe":
            self.check_signal1.emit([1, dir[1]])

        elif dir[0] == "existe":
            self.check_signal1.emit([3])

        elif dir[0] == "iniciar":
            print("hola")
            self.check_signal1.emit([4])


class CheckIng(QObject):

    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal1 = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()
        self.check_signal1.connect(parent.open_window)

    def check(self, dir):

        """
        Función que chequea que la cuenta tenga bien el formato del nombre en
        el caso de superarlo, envia una señal
        True al frontend.


        dir = dir.split(",")
        password = ""

        with open("usuarios.csv", "r") as file:
            file_ = DictReader(file)
            for i in file_:
                if list(i.values())[0] == dir[0]:
                    count = 1
                    password = list(i.values())[1]
                    la_salt = list(i.values())[2]
        """

        if dir[0] == "Volver":
            self.check_signal1.emit([0])

        elif dir[0] == "acceso":
            self.check_signal1.emit([1, dir[1]])

        elif dir[0] == "sin acceso":
            self.check_signal1.emit([3])

class CheckChat(QObject):
    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal1 = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()
        self.check_signal1.connect(parent.open_window)

    def check(self, dir):
        if isinstance(dir, dict):
            pass
        elif dir[0] == "iniciar":
            self.check_signal1.emit([4])


class Character(QObject):

    update_position_signal = pyqtSignal(dict)

    def __init__(self,  parent, x, y):
        super().__init__()
        self.jumping = False
        self.direction = 'R'
        self._x = x
        self._y = y
        self.pos = []
        self.enemies = []

        # Se conecta la señal update_position con el metodo del parent (MainGame.update_position)
        self.update_position_signal.connect(parent.update_position)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """
        Envía la señal update_position al cambiar la coordenada y.
        :param value: int
        :return: none
        """
        if 3 < value < 523:
            self._y = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})
        else:
            if value <= 3:
                self._y = 3
                self.update_position_signal.emit({'x': self.x, 'y': self.y})
            else:
                self._y = 523
                self.update_position_signal.emit({'x': self.x, 'y': self.y})

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):

        """
        Chequea que la coordenada x se encuentre dentro de los parámetros y envía la señal
        update_position con las nuevas coordenadas.
        :param value: int
        :return: none
        """

        if 160 < value < 770:
            self._x = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})
        else:
            if value <= 160:
                self._x = 160
                self.update_position_signal.emit({'x': self.x, 'y': self.y})
            else:
                self._x = 770
                self.update_position_signal.emit({'x': self.x, 'y': self.y})


    def move(self, event):
        """
        Función que maneja los eventos de movimiento (L, R, U, D)
        """
        if event == 'U':
            self.y -= 7
            self.direction = 'U'

        if event == 'L':
            self.x -= 7
            self.direction = 'L'

        if event == 'R':
            self.x += 7
            self.direction = 'R'

        if event == 'D':
            self.y += 7
            self.direction = 'D'


    def Check_posicion(self, lista):
        """
        Función que chequea colicion.
        :return: none
        """
        for i in lista:
            if i.x == self.x and i.y == self.y:
                i.deleteLater()


class CheckGame(QObject):

    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal1 = pyqtSignal(int)
    check_signal2 = pyqtSignal(dict)


    def __init__(self, parent):
        super().__init__()

        # Se conecta la señal check_signal con la función open_window del
        # parent (MainWindow).
        self.padre = parent

        self.check_signal1.connect(parent.open_window)
        self.check_signal2.connect(parent.open_window)

    def check(self, dir):
        # self.check_signal.emit(True)

        """
        Función que chequea que la cuenta tenga bien el formato del nombre en
        el caso de superarlo, envia una señal
        True al frontend.
        """

        print(type(dir))

        if isinstance(dir, dict):
            if dir["status"] == "draw":
                print("entre")
                self.check_signal2.emit(dir)

        elif dir == "Nueva Partida":
            self.check_signal1.emit(1)

        elif dir == "Salir":
            self.check_signal1.emit(0)
        else:
            self.check_signal1.emit(3)
