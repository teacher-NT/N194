import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QHBoxLayout()
        # self.setFixedSize(400, 700)
        self.label1 = QLabel("Salom Dunyo")
        self.vbox.addWidget(self.label1)
        self.btn1 = QPushButton("Tugmacha 1")

        self.vbox.addWidget(self.btn1)
        self.btn1.clicked.connect(self.func1)
        self.btn2 = QPushButton("Tugmacha 2")
        self.vbox.addWidget(self.btn2)

        self.btn3 = QPushButton("Tugmacha 3")
        self.vbox.addWidget(self.btn3)

        self.setLayout(self.vbox)
        self.show()
    
    def func1(self):
        self.label1.setText("Tuugmacha bosildi...")


app = QApplication([])
win = MyWindow()
app.exec_()

