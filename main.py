import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QRadioButton
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

check_tyle = """
    font-size: 20px;
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
        self.label3 = QLabel("Ichimliklar: bo'sh")
        self.label3.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label3)
        self.label4 = QLabel("To'lov turi: tanlanmagan")
        self.label4.setStyleSheet(label2_style)
        self.vbox.addWidget(self.label4)

        self.menu = QComboBox()
        self.menu.addItems(['Somsa', 'Qazi', 'Osh', 'Manti', 'Qozon kabob', 'Shashlik', 'Beshbarmoq'])
        self.vbox.addWidget(self.menu)
        self.menu.setStyleSheet(menu_style)
        self.menu.currentTextChanged.connect(self.get_food)
        self.add_checkbox()
        self.add_radio()
        self.setLayout(self.vbox)
        self.show()
    
    def get_food(self):
        current = self.menu.currentText()
        self.label2.setText(f"Savat: {current}")

    def add_checkbox(self):
        self.check1 = QCheckBox("Choy")
        self.vbox.addWidget(self.check1)
        self.check1.setStyleSheet(check_tyle)
        self.check1.stateChanged.connect(self.check_func)

        self.check2 = QCheckBox("Kofe")
        self.vbox.addWidget(self.check2)
        self.check2.setStyleSheet(check_tyle)
        self.check2.stateChanged.connect(self.check_func)


        self.check3 = QCheckBox("Mineral Suv")
        self.vbox.addWidget(self.check3)
        self.check3.setStyleSheet(check_tyle)
        self.check3.stateChanged.connect(self.check_func)


        self.check4 = QCheckBox("Sut")
        self.vbox.addWidget(self.check4)
        self.check4.setStyleSheet(check_tyle)
        self.check4.stateChanged.connect(self.check_func)


    def check_func(self):
        result = "Ichimliklar: "
        if self.check1.isChecked():
            result += f"{self.check1.text()}, "
        if self.check2.isChecked():
            result += f"{self.check2.text()}, "
        if self.check3.isChecked():
            result += f"{self.check3.text()}, "
        if self.check4.isChecked():
            result += f"{self.check4.text()}, "
        
        self.label3.setText(result)

    def add_radio(self):
        self.r1 = QRadioButton("Naqd")
        self.vbox.addWidget(self.r1)
        self.r1.setStyleSheet(check_tyle)
        self.r1.clicked.connect(self.radio_func)
        self.r2 = QRadioButton("Karta")
        self.r2.setStyleSheet(check_tyle)
        self.r2.clicked.connect(self.radio_func)
        self.vbox.addWidget(self.r2)
        self.r3 = QRadioButton("Crypto")
        self.r3.setStyleSheet(check_tyle)
        self.r3.clicked.connect(self.radio_func)
        self.vbox.addWidget(self.r3)

    def radio_func(self):
        if self.r1.isChecked():
            self.label4.setText(f"To'lov turi: {self.r1.text()}")
        elif self.r2.isChecked():
            self.label4.setText(f"To'lov turi: {self.r2.text()}")
        elif self.r3.isChecked():
            self.label4.setText(f"To'lov turi: {self.r3.text()}")

app = QApplication([])
win = MyWindow()
app.exec_()

