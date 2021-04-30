
from PyQt5.QtWidgets import QApplication,QWidget

import sys
"""
__app = None
__main_widget = None


def init():
    global __app, __main_widget
    __app = QApplication([])
    __main_widget = main_widget.MainWidget()


def add_entity(entity):
    entity.setParent(__main_widget)
    entity.show()
    return entity


def set_size(x, y):
    __main_widget.setFixedSize(x, y)
    entities._SCALE = 2.5 * y / 800


def run(main, delay=25):
    __main_widget.show()
    __main_widget.startMain(main, delay)
    #__main_widget.showFullScreen()
    __app.exec()
"""

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_top_left, y_top_left, width, height)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Mi Primera Ventana')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MiVentana()
    window.show()
    sys.exit(app.exec_())
