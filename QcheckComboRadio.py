import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#QCheckBox
		cb = QCheckBox('Show title', self)
		cb.move(20, 20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		#QRadioButton
		rbtn1 = QRadioButton('First Button', self)
		rbtn1.move(50, 50)
		rbtn1.setChecked(True)

		rbtn2 = QRadioButton(self)
		rbtn2.move(50, 70)
		rbtn2.setText('Second Button')
	
		#QComboBox
		-<F10>
		self.setWindowTitle('QCheckBox, QRadioButton, QComboBox')
		self.setGeometry(300, 300, 300, 200)
		self.show()

	def changeTitle(self, state):
		if state == Qt.Checked:
			self.setWindowTitle('QCheckBox')
		else:
			self.setWindowTitle(' ')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())
