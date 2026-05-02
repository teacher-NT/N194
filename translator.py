import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QTextEdit,
    QComboBox,
    QVBoxLayout
)
from PyQt5.QtCore import Qt
from translate import Translator

import pyttsx3

body_style = """
    background-color: black;
"""
label1_style = """
    font-size: 30px;
    color: white;
"""
combo_style = """
    font-size: 20px;
    color: white;
    background-color: #5f9ded;
    height: 50px;
"""
textedit_style = """
    height: 50px;
    font-size: 20px;
    color: #c7ccd4;
    background-color: black;
"""
btn_style = """
    background-color: #5f9ded;
    color: white;
    height: 50px;
    border-radius: 20px;
    font-size: 20px;
"""


class TranslatorApp(QWidget):
    def  __init__(self):
        super().__init__()
        self.langs = {
            "Uzbek": "uz",
            "Russian": "ru",
            "English": "en",
            "Spanish": "es"
        }
        self.vbox = QVBoxLayout()
        self.setStyleSheet(body_style)
        self.setGeometry(1200,200,400,700)

        self.label1 = QLabel("Translator")
        self.label1.setStyleSheet(label1_style)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.vbox.addWidget(self.label1)

        self.fromlangs = QComboBox()
        self.fromlangs.addItems(self.langs.keys())
        self.fromlangs.setStyleSheet(combo_style)
        self.vbox.addWidget(self.fromlangs)

        self.from_text = QTextEdit()
        self.from_text.setStyleSheet(textedit_style)
        self.from_text.setPlaceholderText("Matn kiriting")
        self.vbox.addWidget(self.from_text)

        self.tolangs = QComboBox()
        self.tolangs.addItems(self.langs.keys())
        self.tolangs.setStyleSheet(combo_style)
        self.vbox.addWidget(self.tolangs)

        self.to_text = QTextEdit()
        self.to_text.setStyleSheet(textedit_style)
        self.to_text.setDisabled(True)
        self.vbox.addWidget(self.to_text)

        self.btn_translate = QPushButton("Tarjima")
        self.btn_translate.setStyleSheet(btn_style)
        self.btn_translate.clicked.connect(self.translate)
        self.vbox.addWidget(self.btn_translate)

        self.setLayout(self.vbox)
        self.show()

    def translate(self):
        fr = self.fromlangs.currentText()
        to = self.tolangs.currentText()
        fr = self.langs.get(fr)
        to2 = self.langs.get(to)
        tarjimon = Translator(from_lang=fr, to_lang=to2)
        text = tarjimon.translate(self.from_text.toPlainText())
        self.to_text.setPlainText(text)
        self.speak(text, to2, to)

    def speak(self, text, short, key):
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"{i}: {voice.id} - {voice.name}")
        russian_voice = None
        for voice in voices:
            if short in voice.id.lower() or key in voice.name.lower():
                russian_voice = voice.id
                break
        if russian_voice:
            engine.setProperty('voice', russian_voice)
            print(f"Ovoz topildi")
        else:
            print("Ovoz topilmadi!")

        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)

        engine.say(text)
        engine.runAndWait()




app = QApplication([])
win = TranslatorApp()

app.exec_()