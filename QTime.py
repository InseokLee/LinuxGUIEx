from PyQt5.QtCore import QTime, QDate, Qt

now = QDate.currentDate()
print(now.toString(Qt.ISODate))


time = QTime.currentTime()
print(time.toString())
