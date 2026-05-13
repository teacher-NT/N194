from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel,
    QMessageBox
)
import json
import datetime

class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Yangi tadbir qo'shish ilovasi")
        self.setFixedSize(450,350)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Tadbir nomi: ")
        self.vbox.addWidget(self.name_input)
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Joyi: ")
        self.vbox.addWidget(self.location_input)
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("Sana: (YYYY-MM-DD)")
        self.vbox.addWidget(self.date_input)
        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("Tur: ")
        self.vbox.addWidget(self.type_input)
        self.add_button = QPushButton("Qo'shish")
        self.add_button.clicked.connect(self.add_data)
        self.vbox.addWidget(self.add_button)

        self.setLayout(self.vbox)
        self.load_file()

    def load_file(self):
        try:
            self.file = open("events.json")
        except:
            print("Yangi fayl yaratildi")
            self.file = open("events.json", "w")
            json.dump([], self.file)
            self.file.close()
            self.file = open("events.json")
        finally:
            self.data = json.load(self.file)
            self.file.close()
    
    def add_data(self):
        name = self.name_input.text()
        loc = self.location_input.text()
        date = self.date_input.text()
        type_ = self.type_input.text()
        
        if len(name)==0 or len(loc)==0 or len(date)==0 or len(type_)==0:
            QMessageBox.warning(self, "Ogohlantirish", "Iltimos barcha maydonlarni to'ldiring!")
            return
        try:
            iso_date = datetime.date.fromisoformat(date)
        except:
            QMessageBox.warning(self, "Ogohlantirish", "Sana formatini to'g'ri kiriting (YYYY-MM-DD)")
            return
        
        if iso_date < datetime.date.today():
            QMessageBox.warning(self, "Ogohlantirish", "Sana kelajakda bo'lishi kerak!")
            return
        m = {
            "name": name,
            "location": loc,
            "date": date,
            "type": type_
        }
        self.data.append(m)
        with open("events.json", "w") as file:
            json.dump(self.data, file, indent=4)
            print("Yozildi...")





app = QApplication([])
win = Oyna()
win.show()
app.exec_()