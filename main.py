import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)
        self.label1 = QLabel(self)
        self.label1.setText("Salom Dunyo")
        self.label1.move(50, 50)
        self.btn1 = QPushButton(self)
        self.btn1.setText("Tugmacha")
        self.btn1.move(50, 150)
        self.btn1.clicked.connect(self.func1)

        self.show()
    
    def func1(self):
        self.label1.setText("Tuugmacha bosildi...")


app = QApplication([])
win = MyWindow()
app.exec_()

