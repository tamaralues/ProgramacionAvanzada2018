# Acá va lo relacionado con el procesamiento de datos
from PyQt5.QtCore import QObject, pyqtSignal, QRect
from PyQt5.Qt import QTest


class Check_Name(QObject):
    """
    Clase que se encargara de chequear la cuenta del contador.
    """
    check_signal = pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__()

        # Se conecta la señal check_signal con la función open_window del
        # parent (MainWindow).

        self.check_signal.connect(parent.open_window)

    def check(self, name):

        """
        Función que chequea que la cuenta tenga bien el formato del nombre en
        el caso de superarlo, envia una señal
        True al frontend.
        """

        with open("Hola.txt", "w") as file:
            file.write(name)

        if name.isalpha() and len(name) >= 6:
            self.check_signal.emit(True)

        else:
            self.check_signal.emit(False)


class Character(QObject):

    update_position_signal = pyqtSignal(dict)

    def __init__(self,  parent, x, y):
        super().__init__()
        self.jumping = False
        self.direction = 'R'
        self._x = x
        self._y = y

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
        if 8 < value < 580:
            self._y = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})
        else:
            if value <= 8:
                self._y = 8
                self.update_position_signal.emit({'x': self.x, 'y': self.y})
            else:
                self._y = 580
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
        if 13 < value < 525:
            self._x = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})

        else:
            if value <= 13:
                self._x = 13
                self.update_position_signal.emit({'x': self.x, 'y': self.y})
            else:
                self._x = 525
                self.update_position_signal.emit({'x': self.x, 'y': self.y})

    def move(self, event):
        """
        Función que maneja los eventos de movimiento (L, R, U, D)
        """
        if event == 'U':
            self.y -= 10
            self.direction = 'U'

        if event == 'L':
            self.x -= 10
            self.direction = 'L'

        if event == 'R':
            self.x += 10
            self.direction = 'R'

        if event == 'D':
            self.y += 10
            self.direction = 'D'

    def Check_posicion(self, lista):
        """
        Función que chequea colicion.
        :return: none
        """
        for i in lista:
            if i.x == self.x and i.y == self.y:
                i.deleteLater()

