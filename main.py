import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QLineEdit
)

body2_style = """
    background-color: white;
    color: black;
"""
label1_1_style =  """
    font-size: 30px;
    font-weight:bold;
    padding: 5px;
    border: 3px solid black;
"""
btn1_1_style = """
    font-size: 20px;
    color: black;
    background-color: green;
    border-radius: 20px;
    height: 50px;
"""

class AboutWindow(QWidget):
    def __init__(self, main_wind):
        super().__init__()
        self.main_wind = main_wind
        self.vbox = QVBoxLayout()
        self.setWindowTitle("About oynasi")
        self.setGeometry(1200, 200, 400, 700)
        self.setStyleSheet(body2_style)

        self.label1 = QLabel("About me!")
        self.label1.setStyleSheet(label1_1_style)
        self.vbox.addWidget(self.label1)

        self.btn1 = QPushButton("Back")
        self.btn1.setStyleSheet(btn1_1_style)
        self.btn1.clicked.connect(self.back_window)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
    
    def back_window(self):
        # self.new_window = MainWindow()
        # self.new_window.show()
        self.main_wind.show()
        self.hide()


body_style = """
    background-color: black;
    color: white;
"""
label1_style =  """
    font-size: 30px;
    font-weight:bold;
    padding: 5px;
    border: 3px solid white;
"""
btn1_style = """
    font-size: 20px;
    color: black;
    background-color: red;
    border-radius: 20px;
    height: 50px;
"""
input_style = """
    border: 3px solid black;
    font-size: 20px;
    color: black;
    background-color: white;
"""
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur oynasi")
        self.setGeometry(1200, 200, 400, 700)
        self.setStyleSheet(body_style)

        self.label1 = QLabel("Welcome")
        self.label1.setStyleSheet(label1_style)
        self.vbox.addWidget(self.label1)

        self.input = QLineEdit()
        self.input.setStyleSheet(input_style)
        self.vbox.addWidget(self.input)

        self.btn2 = QPushButton("Change text")
        self.btn2.setStyleSheet(btn1_style)
        self.btn2.clicked.connect(self.change_text)
        self.vbox.addWidget(self.btn2)

        self.btn1 = QPushButton("Open new window")
        self.btn1.setStyleSheet(btn1_style)
        self.btn1.clicked.connect(self.open_about)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
        self.show()
    
    def open_about(self):
        self.about_win = AboutWindow(self)
        self.about_win.show()
        self.hide()

    def change_text(self):
        self.label1.setText(f"Welcome {self.input.text()}!")




app = QApplication([])

win = MainWindow()

app.exec_()