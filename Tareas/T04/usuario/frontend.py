# Utilize como base la Actividad 10
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QRect
from backend import CheckInput, Character, CheckReg, CheckIng, CheckGame, CheckChat
from random import random, randint
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import (QApplication, QMessageBox, QFrame)
from time import  time
from os import urandom
import hashlib
from random import randrange
from csv import DictReader

window_name, base_class = uic.loadUiType("Ventana1.ui")
window_name2, base_class2 = uic.loadUiType("Ingresar.ui")
window_name3, base_class3 = uic.loadUiType("Registrarse.ui")
window_name4, base_class4 = uic.loadUiType("chatroom.ui")
window_name5, base_class5 = uic.loadUiType("main.ui")
window_name6, base_class6 = uic.loadUiType("chatroom_master.ui")


class MainWindow(window_name, base_class):

    check_count_signal = pyqtSignal(str)
    servidor_signal = pyqtSignal(dict)
    terminar_conexion_signal = pyqtSignal(dict)

    def __init__(self, cliente, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cliente = cliente
        self.contador_label = QLabel('', self)

        # Conexion de Señales
        self.servidor_signal.connect(cliente.send)
        self.terminar_conexion_signal.connect(cliente.terminar_conexion)

        self.game = MainGame(self.cliente, self.servidor_signal,
                             self.terminar_conexion_signal)
        self.game.pause()

        # El boton es capaz de ingresar algo que se chequea en check name
        self.pushButton_3.clicked.connect(self.boton_callback)
        self.pushButton_4.clicked.connect(self.boton_callback)

        self.spell_checker = CheckInput(self)
        self.check_count_signal.connect(self.spell_checker.check)

    def boton_callback(self):
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label3.
        sender = self.sender()
        # Se Instancia el CountChecker.
        self.check_count_signal.emit(sender.text())

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del
        juego.
        :param state: bool
        :return: none
        """

        if state == 1:
            self.hide()
            self.maingame = Registrarse(self.game,self.cliente,
                                        self.servidor_signal,
                                        self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()

        elif state == 0:
            self.hide()
            self.maingame = Ingresar(self.game, self.cliente,
                                     self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()


class Registrarse(window_name3,base_class3):

    check_count_signal = pyqtSignal(str)

    def __init__(self,Game, cliente, servidor_signal, terminar_conexion_signal,
                 *args,**kwargs):
        super().__init__(*args, **kwargs)
        # Señales
        self.setupUi(self)
        self.cliente = cliente
        self.game = Game

        """
        # Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal
        """
        self.setupUi(self)

        # Conexion de Señales
        # Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal

        self.contador_label = QLabel('', self)

        # El boton es capaz de ingresar algo que se chequea en check name
        self.pushButton_3.clicked.connect(self.boton_callback)
        self.pushButton_4.clicked.connect(self.boton_callback)

        self.spell_checker = CheckReg(self)
        self.check_count_signal.connect(self.spell_checker.check)

        self.contador = "Este usuario ya esta existe"


    def boton_callback(self):
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label3.
        sender = self.sender()

        # Se Instancia el CountChecker.

        if sender.text() == "Registrarse":

            hashing = hashlib.sha256()

            mi_salt = urandom(8)
            clave = bytes(self.password.text() , 'utf-8')
            hashing.update((str(clave) + str(mi_salt)).encode(
                "utf-8"))

            mensaje = {"status": "nuevo_usuario", "nombre_usuario":self.name.text(),
                       "clave": str(hashing.hexdigest()), "la_salt":
                           str(mi_salt)}

            self.cliente.send(mensaje)

        else:
            self.check_count_signal.emit(sender.text())

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del
        juego.
        :param state: bool
        :return: none
        """

        if self.cliente.master and state[0] == 1:
            self.hide()
            self.maingame = MainChatMaster(self.game,self.cliente,
                                           self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()

        elif state[0] == 1:
            self.hide()
            self.maingame = MainChat(self.game, self.cliente ,
                                     self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()

        elif state[0] == 4:
            self.hide()
            self.game.color = self.cliente.color
            self.game.show()
            self.game.start()

        elif state[0] == 0:
            """
            Si desea volver hacia atras
            """
            self.hide()
            self.maingame = MainWindow(self.cliente)
            self.cliente.frontend = self.maingame
            self.cliente.frontend.show()

        else:
            self.label_3.setText(self.contador)
            self.label_3.setStyleSheet("QLabel {color: yellow}")


class Ingresar(window_name2, base_class2):

    check_count_signal = pyqtSignal(str)

    def __init__(self, Game,cliente,servidor_signal, terminar_conexion_signal,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        # Señales
        self.setupUi(self)
        self.cliente = cliente
        self.game = Game

        # Conexion Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal

        self.setupUi(self)

        # El boton es capaz de ingresar algo que se chequea en check name
        self.pushButton_3.clicked.connect(self.boton_callback)
        self.pushButton_4.clicked.connect(self.boton_callback)
        self.contador = "Clave inválida"
        self.spell_checker = CheckIng(self)
        self.check_count_signal.connect(self.spell_checker.check)
        self.maingame1 = Game
        self.nombre = ""

    def boton_callback(self):
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label3.
        sender = self.sender()

        # Se Instancia el CountChecker.
        self.check_count_signal.connect(self.spell_checker.check)

        if sender.text() == "Ingresar":
            self.check_count_signal.emit(str(self.name.text() + "," +
                                             self.password.text()))
            mensaje = {"status": "usuario_antiguo", "nombre":
                self.name.text(), "clave":self.password.text()}

            self.cliente.send(mensaje)
        else:
            self.check_count_signal.emit(sender.text())

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del
        juego.
        :param state: bool
        :return: none
        """
        if self.cliente.master and state[0] == 1:
            self.hide()
            self.maingame = MainChatMaster(self.game,self.cliente,
                                           self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()

        elif state[0] == 1:
            self.hide()
            self.maingame = MainChat(self.game, self.cliente ,
                                     self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.cliente.frontend = self.maingame
            self.maingame.show()

        elif state[0] == 0:
            """
            Si desea volver hacia atras
            """
            self.hide()
            self.maingame = MainWindow(self.cliente)
            self.maingame.show()

        elif state[0] == 2:
            self.contador = "Usuario no existe"
            self.label_3.setText(self.contador)
            self.label_3.setStyleSheet("QLabel {color: yellow}")

        elif state[0] == 4:
            self.hide()
            self.game.color = self.cliente.color
            self.game.show()
            self.game.start()

        else:
            self.label_3.setText(self.contador)
            self.label_3.setStyleSheet("QLabel {color: yellow}")

class MainChat(window_name4, base_class4):
    check_count_signal = pyqtSignal(str)

    def __init__(self, Game,cliente, servidor_signal, terminar_conexion_signal,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.game = Game

        # Log
        self.chat_log = ""

        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal
        self.cliente = cliente
        self.pushButton.clicked.connect(self.manejo_boton)

        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(12)
        self.chat_log_label.setFont(chat_log_label_font)
        self.chat_log_label.setStyleSheet("color: darkblue")
        self.scrollArea.setWidget(self.chat_log_label)

        self.spell_checker = CheckChat(self)
        self.check_count_signal.connect(self.spell_checker.check)

    def manejo_boton(self):
        mensaje = {"status": "mensaje", "data": {"usuario": self.cliente.name,
                                "contenido": self.lineEdit.text()}}

        self.cliente.send(mensaje)
        self.lineEdit.setText("")

    def actualizar_chat(self, contenido):
        print(contenido)
        self.chat_log += f"{contenido}\n"
        self.chat_log_label.setText(self.chat_log)

    def open_window(self, state):
        if state[0] == 4:
            self.hide()
            self.game.show()
            self.game.start()


class MainChatMaster(window_name6, base_class6):
    check_count_signal = pyqtSignal(str)

    def __init__(self, Game,cliente, servidor_signal, terminar_conexion_signal,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.game = Game

        # Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal

        self.spell_checker = CheckChat(self)
        self.check_count_signal.connect(self.spell_checker.check)

        # Log
        self.chat_log = ""

        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(12)
        self.chat_log_label.setFont(chat_log_label_font)
        self.chat_log_label.setStyleSheet("color: darkblue")
        self.scrollArea.setWidget(self.chat_log_label)

        self.cliente = cliente
        self.pushButton.clicked.connect(self.manejo_boton)
        self.pushButton_2.clicked.connect(self.boton_master)

    def manejo_boton(self):
        mensaje = {"status": "mensaje", "data": {"usuario":
            self.cliente.name,"contenido": self.lineEdit.text()}}
        self.cliente.send(mensaje)
        self.lineEdit.setText("")

    def actualizar_chat(self, contenido):
        self.chat_log += f"{contenido}\n"
        self.chat_log_label.setText(self.chat_log)

    def boton_master(self):
        self.cliente.send({"status": "iniciar"})

    def open_window(self, state):
        if state[0] == 4:
            self.hide()
            self.game.show()
            self.game.start()

class MainGame(window_name5, base_class5):

    move_character_signal = pyqtSignal(str)
    check_count_signal = pyqtSignal(str)
    check_count_signal2 = pyqtSignal(dict)
    signal_1 = pyqtSignal(dict)

    def __init__(self, cliente, servidor_signal, terminar_conexion_signal,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Señales
        self.servidor_signal = servidor_signal
        self.terminar_conexion_signal = terminar_conexion_signal
        self.cliente = cliente
        self.signal_1.connect(self.cliente.send)

        self.setupUi(self)

        self.frame_1 = 1
        self.color = ""
        self.backend_character = Character(self, 500, 485)
        self.move_character_signal.connect(self.backend_character.move)
        self.t = 30
        self.gamma = 30

        # Log
        self.chat_log = ""

        # Se crea el personaje en el frontend.
        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprites/{}.png'.format(
            self.cliente.color)))
        self.lista = []
        self.chosen_left = "L"
        self.chosen_right = "R"
        self.timer = QtCore.QBasicTimer()
        self.score = 0
        self.color = self.cliente.color
        self.x = randrange(160, 770)
        self.y = randrange(3, 523)
        self.front_character.move(self.x, self.y)
        self.lastKeyPress = 'RIGHT'
        self.timer = QtCore.QBasicTimer()
        self.isPaused = False
        self.isOver = False
        self.speed = 100
        self.contador = 0
        self.start()

        self.pausar.clicked.connect(self.boton_callback)
        self.salir.clicked.connect(self.boton_callback)
        self.new_game.clicked.connect(self.boton_callback)
        self.spell_checker = CheckGame(self)
        self.check_count_signal.connect(self.spell_checker.check)
        self.check_count_signal2.connect(self.spell_checker.check)

    @property
    def frame_(self):
        return self.frame_1

    @frame_.setter
    def frame_(self, value):

        if value > 3:
            self.frame_1 = 1
        else:
            self.frame_1 = value

    def boton_callback(self):
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label3.
        sender = self.sender()

        # Se Instancia el CountChecker.
        self.check_count_signal.emit(sender.text())

    # CODIGO https://github.com/mlisbit/pyqt_snake

    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

    # CODIGO https://github.com/mlisbit/pyqt_snake

    def start(self):
        self.isPaused = False
        self.timer.start(self.speed, self)
        self.update()

    # CODIGO https://github.com/mlisbit/pyqt_snake --> TODO

    def keyPressEvent(self, e):

        if not self.isPaused:
            if e.key() == QtCore.Qt.Key_Up and self.lastKeyPress != 'UP':
                self.direction("UP")
                # self.move_character_signal.emit('U')

            elif e.key() == QtCore.Qt.Key_Down and self.lastKeyPress != 'DOWN':
                self.direction("DOWN")
                # self.lastKeyPress = 'DOWN'
                # self.move_character_signal.emit('D')

            elif e.key() == QtCore.Qt.Key_Left and self.lastKeyPress != 'LEFT':
                self.direction("LEFT")
                # self.lastKeyPress = 'LEFT'
                # self.move_character_signal.emit(self.chosen_left)

            elif e.key() == QtCore.Qt.Key_Right and self.lastKeyPress != 'RIGHT':
                self.direction("RIGHT")
                # self.lastKeyPress = 'RIGHT'
                # self.move_character_signal.emit(self.chosen_right)

            elif e.key() == QtCore.Qt.Key_P:
                self.pause()

        elif e.key() == QtCore.Qt.Key_P:
            self.start()

        elif e.key() == QtCore.Qt.Key_Space:
            self.newGame()

        elif e.key() == QtCore.Qt.Key_Escape:
            self.close()

    # CODIGO https://github.com/mlisbit/pyqt_snake

    def direction(self, dir):

        if dir == "DOWN" and self.checkStatus(self.x, self.y + 7):
            self.y += 7
            self.move_character_signal.emit('D')
            self.lastKeyPress = "DOWN"

        elif dir == "UP" and self.checkStatus(self.x, self.y - 7):
            self.y -= 7
            self.move_character_signal.emit('U')
            self.lastKeyPress = "UP"

        elif dir == "RIGHT" and self.checkStatus(self.x + 7, self.y):
            self.x += 7
            self.move_character_signal.emit('R')
            self.lastKeyPress = "RIGHT"

        elif dir == "LEFT" and self.checkStatus(self.x - 7, self.y):
            self.x -= 7
            self.move_character_signal.emit('L')
            self.lastKeyPress = "LEFT"

        if self.contador != :
            """
            Esto es con una distribución especifica
            """
            self.backend_character.pos.append(QLabel(self))
            largo = len(self.backend_character.pos)
            self.backend_character.pos[largo - 1].setPixmap(
                QPixmap('sprites/{}.png'.format(self.cliente.color)))
            self.backend_character.pos[largo - 1].move(
                self.backend_character.x, self.backend_character.y)
            self.backend_character.pos[largo - 1].show()
            self.signal_1.emit({"status": "draw", "dibujo": [self.cliente.color,
                 self.backend_character.x, self.backend_character.y]})

    # CODIGO https://github.com/mlisbit/pyqt_snake

    def checkStatus(self, x, y):

        if self.backend_character.x == 750 or self.backend_character.x == 160 \
                or self.backend_character.y == 3 or self.backend_character.y == \
                523:

            self.pause()
            self.isPaused = True
            self.isOver = True
            return True

        elif self.score >= 573:
            print("you win!")

        """
                elif self.y == self.foody and self.x == self.foodx:
            self.FoodPlaced = False
            self.score += 1
            return True
            
                elif self.snakeArray[0] in self.snakeArray[1:len(self.snakeArray)]:
            self.pause()
            self.isPaused = True
            self.isOver = True
            return False
        """
        return True

    # CODIGO https://github.com/mlisbit/pyqt_snake

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.direction(self.lastKeyPress)

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
        if event["x"] == None:
            self.pause()
            self.isPaused = True
            self.isOver = True

        else:
            self.front_character.move(event['x'], event['y'])

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por la del
        juego.
        :param state: bool
        :return: none
        """

        if isinstance(state , dict):
            self.backend_character.enemies.append(QLabel(self))
            largo = len(self.backend_character.pos)
            self.backend_character.enemies[largo - 1].setPixmap(
                QPixmap('sprites/{}.png'.format(state["dibujo"][0])))
            self.backend_character.enemies[largo - 1].move(
                state["dibujo"][1], state["dibujo"][2])
            self.backend_character.enemies[largo - 1].show()

        elif state == 1:
            self.hide()
            self.maingame = MainGame(self.cliente, self.servidor_signal,
                                     self.terminar_conexion_signal)
            self.maingame.show()

        elif state == 0:
            """
            Si desea volver hacia atras
            """
            self.hide()
            self.maingame = MainWindow(self.cliente)
            self.maingame.show()
            self.cliente.send({"status": "cerrar sesion"})

        else:
            if self.pausar.text() == "Pausa":
                self.pause()
                self.isPaused = True
                self.pausar.setText("Continuar")

            elif self.pausar.text() == "Continuar":
                self.start()
                self.isPaused = False
                self.pausar.setText("Pausa")


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())