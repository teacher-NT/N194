import os
os.system('cls')

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel
)

from PyQt5.QtCore import QTimer

app  = QApplication([])
win = QWidget()
win.setWindowTitle("Svetafor")
win.setGeometry(1200, 80, 400, 900)
win.setStyleSheet("""
    background-color: black;
""")

btn1 = QPushButton(win)
btn1.setGeometry(75, 50, 250,250)
btn1.setStyleSheet("""
    background-color: white;
                   border:  5px solid blue;
                   border-radius: 125;
""")


btn2 = QPushButton(win)
btn2.setGeometry(75, 310, 250,250)
btn2.setStyleSheet("""
    background-color: white;
                   border:  5px solid blue;
                   border-radius: 125;
""")


btn3 = QPushButton(win)
btn3.setGeometry(75, 570, 250,250)
btn3.setStyleSheet("""
    background-color: white;
                   border:  5px solid blue;
                   border-radius: 125;
""")

seconds = 23
def func1():
    global seconds
    if 13 < seconds <= 23:
        btn1.setStyleSheet("""
            background-color: red;
                        border:  5px solid blue;
                        border-radius: 125;
                        font-size: 70px;
                        color: white;
        """)
        n = seconds - 13
        btn1.setText(str(n))
        btn2.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
        btn3.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
    elif 10 < seconds <= 13:
        btn1.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
        btn2.setStyleSheet("""
            background-color: yellow;
                        border:  5px solid blue;
                        border-radius: 125;
                        font-size: 70px;
                        color: black;
        """)
        n = seconds - 10
        btn2.setText(str(n))
        btn3.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
    elif 0 < seconds <= 10:
        btn1.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
        btn2.setStyleSheet("""
            background-color: black;
                        border:  5px solid blue;
                        border-radius: 125;
        """)
        btn3.setStyleSheet("""
            background-color: lime;
                        border:  5px solid blue;
                        border-radius: 125;
                        font-size: 70px;
                        color: white;
        """)
        btn3.setText(str(seconds))
    elif seconds <= 0:
        seconds = 23
    seconds -= 1

 
timer = QTimer()
timer.timeout.connect(func1)
timer.start(1000)


win.show()
app.exec_()