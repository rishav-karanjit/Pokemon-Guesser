from PyQt5 import QtWidgets, uic, QtCore
import sys

class SettingsUI(QtWidgets.QMainWindow):
	def __init__(self,main):
		self.main = main
		super(SettingsUI, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.initUI()
		self.main.close()
		self.show()

	def initUI(self):
		uic.loadUi('./UI/Setting_UI.ui', self)

		self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
		self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

		self.Close.clicked.connect(sys.exit)
		self.minimize.clicked.connect(self.showMinimized)
        
		self.Easy = self.findChild(QtWidgets.QPushButton, 'Easy')
		self.Medium = self.findChild(QtWidgets.QPushButton, 'Medium')
		self.Hard = self.findChild(QtWidgets.QPushButton, 'Hard')
        
		self.Generation_I = self.findChild(QtWidgets.QPushButton, 'Generation_I')
		self.Generation_II = self.findChild(QtWidgets.QPushButton, 'Generation_II')
		self.Generation_III = self.findChild(QtWidgets.QPushButton, 'Generation_III')
		self.Generation_IV = self.findChild(QtWidgets.QPushButton, 'Generation_IV')
		self.Generation_V = self.findChild(QtWidgets.QPushButton, 'Generation_V')
		self.Generation_VI = self.findChild(QtWidgets.QPushButton, 'Generation_VI')
		self.Generation_VII = self.findChild(QtWidgets.QPushButton, 'Generation_VII')
		
		self.HomeScreen = self.findChild(QtWidgets.QPushButton, 'Home_Screen')
		
		self.HomeScreen.clicked.connect(self.Disp_HomeScreen)

        

	def Disp_HomeScreen(self):
		self.close()
		self.window=self.main.show()