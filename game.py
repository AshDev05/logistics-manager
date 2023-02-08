import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class GameWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Logistics Manager')
        self.setGeometry(0, 0, 1000, 520)
        self.initGUI(path='./images/bg.jpg')
    
    def initGUI(self, path):
        
        # Setting background image
        bg = qtw.QLabel(self)
        pixmap = qtg.QPixmap(path)
        bg.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        

        # Showing the Window
        self.show()

app = qtw.QApplication([])
mainWin = GameWindow()
app.exec_()