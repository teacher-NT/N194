import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit
)
from PyQt5.QtGui import QFont

app = QApplication([])

window = QWidget()
window.setGeometry(1200, 200, 400, 600)
window.setWindowTitle("Bu birinchi ilovam")

matn1 = QLabel(window)
matn1.setText("Counter")
# matn1.setGeometry(20,50,300,200)
matn1.setStyleSheet("""font-size:28px; 
                    margin-top:50px;
                    margin-left:20px; 
                    color:red;
                    font-weight: bold;""")

in1 = QLineEdit(window)
in1.setGeometry(70,100, 280, 50)
in1.setStyleSheet("""font-size:25px;
                  border-radius:20px;
                  border: 2px solid black""")
in1.setPlaceholderText("rang kiriting...")

style1 = """
    font-size: 18px;
    color: blue;
    background-color: lime;
    border-radius: 20px;
    border: 4px solid cyan;
"""

style2 = """
    font-size: 18px;
    color: blue;
    background-color: red;
    border-radius: 20px;
    border: 4px solid cyan;
"""

def func_btn1():
    global in1
    color = in1.text()
    window.setStyleSheet(f"background-color: {color};")
    


button1 = QPushButton(window)
button1.setText("Count")
button1.setGeometry(80, 300, 100, 50)
button1.setStyleSheet(style1)
button1.clicked.connect(func_btn1)

window.show()
app.exec_()