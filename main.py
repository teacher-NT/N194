import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)
from PyQt5.QtGui import QFont

# font1 = QFont("Courier", 18)
# font1 = QFont("Comic Sans MS", 18)


app = QApplication([])

window = QWidget()
window.setGeometry(1200, 200, 400, 600)
window.setWindowTitle("Bu birinchi ilovam")

matn1 = QLabel(window)
matn1.setText("Python dasturidan salom")
# matn1.setGeometry(20,50,300,200)
matn1.setStyleSheet("""font-size:28px; 
                    margin-top:50px;
                    margin-left:20px; 
                    color:red;
                    font-weight: bold;""")
# matn1.setFont(font1)
style1 = """
    font-size: 18px;
    color: blue;
    background-color: lime;
    border-radius: 20px;
    border: 4px solid cyan;
"""

def func_btn1():
    global matn1
    matn1.setText("Salom Ibrohim!!!")

button1 = QPushButton(window)
button1.setText("Start")
button1.setGeometry(80, 150, 100, 50)
button1.setStyleSheet(style1)
button1.clicked.connect(func_btn1)

color = "white"
def func_btn2():
    global color
    if color == "white":
        color = 'black'
    else:
        color = 'white'
    window.setStyleSheet(f"background-color:{color};")

button2 = QPushButton(window)
button2.setText("Stop")
button2.setGeometry(250, 150, 100, 50)
button2.setStyleSheet(style1)
button2.clicked.connect(func_btn2)

window.show()
app.exec_()