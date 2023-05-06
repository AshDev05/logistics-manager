import SHELL_BASE as sb # Import base functions from the shell app
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
import sys, time

profiles = sb.sqlselect("""SELECT name FROM profiles;""")

### UI CLASSES

# MAIN MENU
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to actions
        self.pushButton_2.clicked.connect(lambda: new_game_ui())
        self.pushButton_3.clicked.connect(lambda: load_game_ui())
        self.pushButton.clicked.connect(lambda: options_ui())

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Logistics Manager", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Load Game", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Welcome To Logistics Manager</span></p></body></html>", None))
    # retranslateUi

# New Game MENU
class Ui_NewGameWindow(object):
    def setupUi(self, NewGameWindow):
        if not NewGameWindow.objectName():
            NewGameWindow.setObjectName(u"NewGameWindow")
        NewGameWindow.resize(778, 534)
        self.centralwidget = QWidget(NewGameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_game_title = QLabel(self.centralwidget)
        self.new_game_title.setObjectName(u"new_game_title")

        self.verticalLayout.addWidget(self.new_game_title)

        self.changeable_label = QLabel(self.centralwidget)
        self.changeable_label.setObjectName(u"changeable_label")

        self.verticalLayout.addWidget(self.changeable_label)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_name = QLineEdit(self.centralwidget)
        self.save_name.setObjectName(u"save_name")

        self.horizontalLayout.addWidget(self.save_name)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_2)

        NewGameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewGameWindow)

        QMetaObject.connectSlotsByName(NewGameWindow)

        self.pushButton_2.clicked.connect(menu_ui)
        self.pushButton.clicked.connect(self.new_game_call)
    # setupUi

    def retranslateUi(self, NewGameWindow):
        NewGameWindow.setWindowTitle(QCoreApplication.translate("NewGameWindow", u"Logistics Manager", None))
        self.new_game_title.setText(QCoreApplication.translate("NewGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">New Game</span></p></body></html>", None))
        self.changeable_label.setText(QCoreApplication.translate("NewGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Create a new save game</span></p></body></html>", None))
        self.save_name.setText(QCoreApplication.translate("NewGameWindow", u"New Save Name", None))
        self.pushButton.setText(QCoreApplication.translate("NewGameWindow", u"Create", None))

        self.checkBox.setToolTip("")

        self.checkBox.setText(QCoreApplication.translate("NewGameWindow", u"DevLock", None))
        self.pushButton_2.setText(QCoreApplication.translate("NewGameWindow", u"Menu", None))
    # retranslateUi
    
    def new_game_call(self):
        global name

        name = str(self.save_name.text())

        if name not in profiles:
            sb.new_game(name= name)
        else:
            self.changeable_label.setText(QCoreApplication.translate("NewGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Name already exists!</span></p></body></html>", None))
            time.sleep(15)
            self.changeable_label.setText(QCoreApplication.translate("NewGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Create a new save game</span></p></body></html>", None))

    # Connect buttons to actions

# Load Game MENU
class Ui_LoadGameWindow(object):
    def setupUi(self, LoadGameWindow):
        if not LoadGameWindow.objectName():
            LoadGameWindow.setObjectName(u"LoadGameWindow")
        LoadGameWindow.resize(778, 534)
        self.centralwidget = QWidget(LoadGameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_game_title = QLabel(self.centralwidget)
        self.new_game_title.setObjectName(u"new_game_title")

        self.verticalLayout.addWidget(self.new_game_title)

        self.changeable_label = QLabel(self.centralwidget)
        self.changeable_label.setObjectName(u"changeable_label")

        self.verticalLayout.addWidget(self.changeable_label)

        self.verticalSpacer = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.profilesList = QListWidget(self.centralwidget)
        self.profilesList.setObjectName(u"profilesList")
        self.profilesList.setTabKeyNavigation(True)
        self.profilesList.setItemAlignment(Qt.AlignCenter)
        self.profilesList.setSortingEnabled(True)
        self.profilesList.setSelectionRectVisible(True)

        self.horizontalLayout.addWidget(self.profilesList)

        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.verticalScrollBar.setInvertedControls(True)

        self.horizontalLayout.addWidget(self.verticalScrollBar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_2)

        LoadGameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadGameWindow)

        QMetaObject.connectSlotsByName(LoadGameWindow)

        self.pushButton_2.clicked.connect(menu_ui)

        # FILL UP LIST

        for elt in profiles:
            self.profilesList.addItem(str(elt))
        
    # setupUi

    def retranslateUi(self, LoadGameWindow):
        LoadGameWindow.setWindowTitle(QCoreApplication.translate("LoadGameWindow", u"Logistics Manager", None))
        self.new_game_title.setText(QCoreApplication.translate("LoadGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">Load Game</span></p></body></html>", None))
        self.changeable_label.setText(QCoreApplication.translate("LoadGameWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Load an existing save</span></p></body></html>", None))
        self.profilesList.setToolTip(QCoreApplication.translate("LoadGameWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">As you create profiles, they will appear here.</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("LoadGameWindow", u"Load", None))
        self.pushButton_2.setText(QCoreApplication.translate("LoadGameWindow", u"Menu", None))
    # retranslateUi

### WINDOW CLASSES

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class NewGame_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_NewGameWindow()
        self.ui.setupUi(self)

class LoadGame_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LoadGameWindow()
        self.ui.setupUi(self)

# CONNECTED FUNCTIONS
def menu_ui():
    global window

    window.close()
    window= MainWindow()
    window.show()

def new_game_ui():
    global window

    window.close()
    window = NewGame_Window()
    window.show()

def load_game_ui():
    global window

    window.close()
    window = LoadGame_Window()
    window.show()

def options_ui():
    global window

    window.close()
    window.show()

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Run the event loop
    sys.exit(app.exec_())
