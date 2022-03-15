from PyQt5 import QtWidgets, uic, QtCore
import sys

class Lose(QtWidgets.QDialog):
	def __init__(self,question,main):
		self.main = main
		self.question = question
		super(Lose, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.initUI()
		self.question.close()
		self.main.close()
		self.show()

	def initUI(self):
		uic.loadUi('./UI/You_Lose.ui', self)

		self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
		self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

		self.Close.clicked.connect(sys.exit)
		self.minimize.clicked.connect(self.showMinimized)

		self.PlayAgain = self.findChild(QtWidgets.QPushButton, 'PlayAgain')
		self.HomeScreen = self.findChild(QtWidgets.QPushButton, 'HomeScreen')

		self.HomeScreen.clicked.connect(self.Disp_HomeScreen)

	def Disp_HomeScreen(self):
		self.close()
		self.window=self.main.show()

	