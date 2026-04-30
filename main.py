import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox
)

body_style = """
    background-color: #f3f7c3;
"""

label_style = """
    font-size: 32px;
    color: #e05b2f;
"""

label2_style = """
    font-size: 20px;
"""
menu_style = """
    font-size: 20px;
    background-color: #dfe665;
    color: #6044bd;
"""

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(body_style)
        self.vbox = QVBoxLayout()
        # self.setFixedSize(400, 700)
        self.label1 = QLabel("Restoran Menusi")
        self.label1.setStyleSheet(label_style)
        self.vbox.addWidget(self.label1)

        self.label2 = QLabel("Savat: bo'sh")
        self.label2.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label2)
        
        self.menu = QComboBox()
        self.menu.addItems(['Somsa', 'Qazi', 'Osh', 'Manti', 'Qozon kabob', 'Shashlik', 'Beshbarmoq'])
        self.vbox.addWidget(self.menu)
        self.menu.setStyleSheet(menu_style)
        self.menu.currentTextChanged.connect(self.get_food)
        self.setLayout(self.vbox)
        self.show()
    
    def get_food(self):
        current = self.menu.currentText()
        self.label2.setText(f"Savat: {current}")
        


app = QApplication([])
win = MyWindow()
app.exec_()

