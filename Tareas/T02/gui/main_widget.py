import os

from PyQt5.Qt import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtWidgets import QApplication,QWidget

import sys

_PATH = os.path.dirname(os.path.abspath(__file__))


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__timer = QTimer(self)
        self.background = QLabel(self)
        self.background.lower()
        self.background.setPixmap(
            QPixmap(_PATH + os.sep + "assets" + os.sep + "map" + os.sep +
                    "background.png"))

    def startMain(self, main, delay=25):
        self.__timer.timeout.connect(main)
        self.__timer.start(delay)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec_())