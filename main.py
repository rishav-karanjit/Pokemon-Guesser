from PyQt5 import QtWidgets, uic, QtCore
import sys
from Resources import images
from Questions import QuestionScreen
from Settings import SettingsUI

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        uic.loadUi('UI/Start_Screen.ui', self)
        self.initUI()

    def initUI(self):
        #Find Push buttons
        self.LetsPlay = self.findChild(QtWidgets.QPushButton, 'LetsPlay')
        self.Setting = self.findChild(QtWidgets.QPushButton, 'Settings')
        self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
        self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

        #button connect
        self.LetsPlay.clicked.connect(self.LetsPlay_Clicked)
        self.Setting.clicked.connect(self.Setting_Clicked)
        self.Close.clicked.connect(sys.exit)
        self.minimize.clicked.connect(self.showMinimized)
        #move window to (50,5)
        self.move(500, 300)

    def LetsPlay_Clicked(self):
        self.window=QuestionScreen(self)

    def Setting_Clicked(self):
        self.window = SettingsUI(self)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()