import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#class에 멤버변수, 멤버함수를 만들고 안에 widget을 추가(멤버변수형태로)
#self 클레스의 최상단에 멤버변수를 추가하겠다는 뜻

class Button(QToolButton):
	def __init__(self, text, parent = None):
		super(Button, self).__init__(parent)

		self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		self.setText(text)

	def sizeHint(self):
		size = super(Button, self).sizeHinf()
		size.setHeight(size.height() + 20)
		size.setWidth(max(size.width(), size.height()))
		return size
		
class Calculater(QWidget):
	NumDigitButtons = 10
	
	def __init__(self, parent = None):    # 처음 생성되어지는 생성자
		super(Calculator, self).__init__(parent) # 부모클래스에 있는 init을 실행(QWidget 에 init을 실행)
#self.initUI()
		
		#QLineEdit Properties
		self.display = QLineEdit('2')
		self.display.setReadOnly(True)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setMaxLength(15)
		
		#QLineEdit font Properties
		font = self.display.font()
		font.setPointSize(font.pointSize() + 8)
		self.display.setFont(font) #font 적용

		self.digitButtons = []

		for i in range(Calculator.NumDigitButtons):
			self.digitButtons.append(self.createButton(str(i), self.digitClicked))

		self.backspaceButton = self.createButton("DEL", self.backspaceClicked)
		self.clearAllButton = self. createButton("C", self.clear)

		self.divisionButton = self.createButton(u"\N{DIvISION SIGN}", self.multiplicativeOperatorClicked)
		self.timesButton = self.createButton(u"\N{MULTIPLICATION SIGN}", self.multiplicativeOperatorClicked)
		self.minusButton = self.createButton("-", self.additiveOperatorClicked)
		self.plusButton = self.createButton("+", self.additiveOperatorClicked)
		
		self.equalButton = self.createButton("=", self.equalClicked)

		mainLayout = QGridLayout()
		mainLayout.setSizeConstrain(QLayout.SetFixedSize)

		mainLayout.addWidget(self.display, 0, 1, 1, 4)
		mainLayout.addWidget(self.backspaceButton, 5, 3)
		for i in range(1, Calculator.NumDigitButtons):
			row = ((9 - i) / 3) + 2
			column = ((i - 1) % 3) + 1
			mainLayout.addWidget(self.digitButtons[i], row, column)

		mainLayout.addWidget(self.digitButtons[0], 5, 1, 1, 2)
		mainLayout.addWidget(self.plusButton, 1, 1)
		mainLayout.addWidget(self.minusButton, 1, 2)
		mainLayout.addWidget(self.timesButton, 1, 3)
		mainLayout.addWidget(self.divisionButton, 1, 4)
		mainLayout.addWidget(self.clearAllButton, 2, 4, 2, 1)
		mainLayout.addWidget(self.equalButton, 4, 4, 2, 1)
		self.setLayout(mainLayout)

		self.setWindowTitle("Calculator")

		


"""
	def NumClicked(self):
		test = self.sender()
		testText = int(test.text())	
		disText = self.display.text()
		value = int(disText) + int(testText)
		self.display.setText(str(value))
"""	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	calc = Calculater()
	calc.show()
	sys.exit(app.exec_())
