import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.resize(200,50)
        self.setWindowTitle('PyQt5 Intro')
        self.label = QLabel(self)
        self.label.setText('Hello World!')
        font = QFont()
        font.setFamily('Ethnocentric')
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()