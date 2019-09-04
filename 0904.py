import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#QTabWidget()
		tabs = QTabWidget()
		tabs.addTab(FirstTab(), '길이')
		tabs.addTab(SecondTab(), '무게')
		
		vbox = QVBoxLayout()
		vbox.addWidget(tabs)

		self.setLayout(vbox)

		self.setWindowTitle('길이 무게 구하기')
		self.setGeometry(300, 300, 300, 200)
		self.show()


class FirstTab(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):		
		#QGridLayout
		grid = QGridLayout()
		self.setLayout(grid)
		
		#QLineEdit
		self.lineEdit = QLineEdit(self)
		grid.addWidget(self.lineEdit, 1, 0)

		#QComboBox
		cb = QComboBox(self)
		self.list = ['mm','cm','m','km']
		cb.addItems(self.list)
		cb.activated[str].connect(self.onActivated)
		grid.addWidget(cb, 1, 1)
		
		#value QLabel
		self.FirstText = 'mm\ncm\nm\nkm'
		self.labelText = QLabel(self.FirstText, self)
		self.labelText.setAlignment(Qt.AlignRight)
		grid.addWidget(self.labelText, 2, 0, 4, 2)
		
	def onActivated(self, text):
		num = float(self.lineEdit.text())
		
		if text == self.list[0]:
			num_mm = str(num * 1)
			num_cm = str(num * 0.1)
			num_m  = str(num * 0.001)
			num_km = str(num * 0.000001)
		elif text == self.list[1]:
			num_mm = str(num * 10)
			num_cm = str(num * 1)
			num_m  = str(num * 0.01)
			num_km = str(num * 0.00001)
		elif text == self.list[2]:
			num_mm = str(num * 1000)
			num_cm = str(num * 100)
			num_m  = str(num * 1)
			num_km = str(num * 0.001)
		elif text == self.list[3]:
			num_mm = str(num * 1000000)
			num_cm = str(num * 100000)
			num_m  = str(num * 1000)
			num_km = str(num * 1)
			
		self.labelText.setText(num_mm + ' mm\n' + num_cm + ' cm\n' + num_m + ' m\n' + num_km + ' km\n')

class SecondTab(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):		
		#QGridLayout
		grid = QGridLayout()
		self.setLayout(grid)
		
		#QLineEdit
		self.lineEdit = QLineEdit(self)
		grid.addWidget(self.lineEdit, 1, 0)

		#QComboBox
		cb = QComboBox(self)
		self.list = ['mg','g','kg','t']
		cb.addItems(self.list)		
		cb.activated[str].connect(self.onActivated)
		grid.addWidget(cb, 1, 1)

		#value QLabel
		self.FirstText = 'mg\ng\nkg\nt'
		self.labelText = QLabel(self.FirstText, self)
		self.labelText.setAlignment(Qt.AlignRight)
		grid.addWidget(self.labelText, 2, 0, 4, 2)

	def onActivated(self, text):
		num = float(self.lineEdit.text())

		if text == self.list[0]:
			num_mm = str(num * 1)
			num_cm = str(num / 1000)
			num_m  = str(num / 1000000)
			num_km = str(num / 1000000000)
		elif text == self.list[1]:
			num_mm = str(num * 1000)
			num_cm = str(num * 1)
			num_m  = str(num / 1000)
			num_km = str(num / 1000000)
		elif text == self.list[2]:
			num_mm = str(num * 1000000)
			num_cm = str(num * 1000)
			num_m  = str(num * 1)
			num_km = str(num /1000)
		elif text == self.list[3]:
			num_mm = str(num * 1000000000)
			num_cm = str(num * 1000000)
			num_m  = str(num * 1000)
			num_km = str(num * 1)
			
		self.labelText.setText(num_mm + ' mg\n' + num_cm + ' g\n' + num_m + ' kg\n' + num_km + ' t\n')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())
