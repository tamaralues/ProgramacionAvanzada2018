# Acá va lo relacionado con la GUI.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QRect
from backend import Check_Name, Character
from random import random, randint
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMessageBox, QFrame)

window_name5, base_class5 = uic.loadUiType("untitled.ui")

class MainWindow(window_name5, base_class5):

    """
    Esta es mi ventana principal
    """

    check_count_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.contador_label = QLabel('', self)


        self.contador = "AEl nombre no es válido"

        # El boton es capaz de ingresar algo que se chequea en check name
        self.pushButton.clicked.connect(self.check_count)

        # Se Instancia el CountChecker.
        self.spell_checker = Check_Name(self)
        self.check_count_signal.connect(self.spell_checker.check)


    def check_count(self):

        """
        Función que incrementa el contador y envía una señal al CheckCount con
         la cuenta.
        También actualiza el label del contador.
        :return: none
        """

        self.check_count_signal.emit(self.lineEdit.text())

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del
        juego.
        :param state: bool
        :return: none
        """

        if state:
            self.hide()
            self.maingame = MainGame()
            self.maingame.show()
        else:
            self.contador_label.setText(self.contador)


class MainGame(QWidget):

    move_character_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 560, 615)

        self._frame = 1

        # Se setea la imagen de fondo.
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('sprites/map.png'))

        # Se instancia el personaje del backend y se conecta move_character
        # _signal con la función move de Character.
        self.backend_character = Character(self, 50, 485)
        self.move_character_signal.connect(self.backend_character.move)

        # Se crea el personaje en el frontend.
        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprites/pacman_D_1.png'))
        self.front_character.move(50, 485)
        self.lista = []
        self.chosen_left = "L"
        self.chosen_right = "R"


    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value > 3:
            self._frame = 1
        else:
            self._frame = value

    def keyPressEvent(self, e):

        """
        Dada la presión de una tecla se llama a esta función. Al apretarse una
        tecla chequeamos si esta dentro de las teclas del control del juego y de
        ser así, se envía una señal al backend con la acción además de
        actualizar el sprite.
        :param e: QKeyEvent
        """

        self.frame += 1
        self.backend_character.Check_posicion(self.lista)
        if e.key() == Qt.Key_Down:
            self.front_character.setPixmap(QPixmap(f'sprites/pacman_D_'
                                                   f'{self.frame}.png'))

            self.move_character_signal.emit("D")


        if e.key() == Qt.Key_Left:

            self.front_character.setPixmap(QPixmap(f'sprites/pacman_L'
                                                   f'_{self.frame}.png'))
            self.move_character_signal.emit(self.chosen_left)


        if e.key() == Qt.Key_Up:
            self.front_character.setPixmap(QPixmap(f'sprites/pacman_U_'
                                                   f'{self.frame}.png'))

            self.move_character_signal.emit('U')


        if e.key() == Qt.Key_Right:
            self.front_character.setPixmap(QPixmap(f'sprites/pacman_R_'
                                                   f'{self.frame}.png'))

            self.move_character_signal.emit(self.chosen_right)


        if e.key() == Qt.Key_Space:

            self.lista.append(QLabel(self))

            largo = len(self.lista)

            self.lista[largo - 1].setPixmap(QPixmap('sprites/cherry.png'))
            x = randint(20, 500)
            y = randint(10, 550)
            self.lista[largo - 1].move(x, y)
            self.move_character_signal.emit('A')
            self.lista[largo - 1].show()


    def keyReleaseEvent(self, e):

        """
        Dado que se deje de presionar una tecla se llama a esta función. Al
        apretarse una tecla chequeamos si esta dentro de las teclas del
        control del juego y de ser así, se actualiza el sprite.
        :param e: QKeyEvent
        :return:
        """

        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(QPixmap(f'sprite/Super '
                             f'Mario{self.backend_character.direction}.png'))


    def update_position(self, event):
        """
        Función que recibe un diccionario con las cordenadas del personaje y
         las actualiza en el frontend.
        :param event: dict
        :return: none
        """
        self.front_character.move(event['x'], event['y'])


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())