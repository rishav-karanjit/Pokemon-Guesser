from PyQt5 import QtWidgets, uic, QtCore
import sys
from PyQt5.QtCore import QPoint
from Youlose import Lose

class QuestionScreen(QtWidgets.QMainWindow):
	def __init__(self,main):
		self.main = main
		super(QuestionScreen, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.initUI()
		self.main.close()
		self.show()

	def initUI(self):
		self.Answer = "Pokemon 1"
		Poke1 = "Pokemon 1"
		Poke2 = "Pokemon 2"
		Poke3 = "Pokemon 3"
		Poke4 = "Pokemon 4"
		Question = "Question 1"
		Difficulty = "Medium"
		Score = "1"

		uic.loadUi('./UI/Question_Menu.ui', self)
		self.Close = self.findChild(QtWidgets.QPushButton, 'Close')
		self.minimize = self.findChild(QtWidgets.QPushButton, 'minimize')

		self.Close.clicked.connect(sys.exit)
		self.minimize.clicked.connect(self.showMinimized)

		self.P1 = self.findChild(QtWidgets.QPushButton, 'P1')
		self.P2 = self.findChild(QtWidgets.QPushButton, 'P2')
		self.P3 = self.findChild(QtWidgets.QPushButton, 'P3')
		self.P4 = self.findChild(QtWidgets.QPushButton, 'P4')

		self.Questions = self.findChild(QtWidgets.QTextBrowser,'Questions')
		self.Score = self.findChild(QtWidgets.QLabel,'score')
		self.Difficulty = self.findChild(QtWidgets.QLabel,'DifficultyLevel')		


		self.Questions.setText(Question)
		self.Difficulty.setText(Difficulty)
		self.Score.setText(Score)

		self.P1.setText(Poke1)
		self.P2.setText(Poke2)
		self.P3.setText(Poke3)
		self.P4.setText(Poke4)
		
		self.P1.clicked.connect(self.Answer1_Clicked)
		self.P2.clicked.connect(self.Answer2_Clicked)
		self.P3.clicked.connect(self.Answer3_Clicked)
		self.P4.clicked.connect(self.Answer4_Clicked)
		

	def Answer1_Clicked(self):
		if(self.P1.text() == self.Answer):
			self.window=QuestionScreen(self)
		else:
			self.window=Lose(self,self.main)

	def Answer2_Clicked(self):
		if(self.P2.text() == self.Answer):
			self.window=QuestionScreen(self)
		else:
			self.window=Lose(self,self.main)

	def Answer3_Clicked(self):
		if(self.P3.text() == self.Answer):
			self.window=QuestionScreen(self)
		else:
			self.window=Lose(self,self.main)

	def Answer4_Clicked(self):
		if(self.P4.text() == self.Answer):
			self.window=QuestionScreen(self)
		else:
			self.window=Lose(self,self.main)