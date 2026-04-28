import os
os.system('cls')

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget()
window.setGeometry(1200, 200, 400, 600)
window.setWindowTitle("Bu birinchi ilovam")
window.show()

app.exec_()