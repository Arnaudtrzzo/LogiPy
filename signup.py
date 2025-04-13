from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton,QDateTimeEdit,QDateEdit,QSpinBox
from PyQt6.QtGui import QIcon, QCursor, QPixmap
from PyQt6.QtCore import Qt
import sys

class Signup(QWidget):
    def __init__(self):
     super().__init__()
     
     self.btn = QPushButton(self,text="Se connecter")
     self.btn.setGeometry(200, 400, 100, 35)
     self.btn_to_login.clicked.connect(self.login)
     self.btn.setStyleSheet("""QPushButton{
         font-size: 14px;
         color: blue;
         background-color: transparent;
         border: none;
         text-decoration: underline;
     }""")
     
     self.date = QDateTimeEdit(self)
     self.btn.setGeometry(10,50,200,40)
     
     
     def login(self):
         self.close()
         from login import Login
         self.log = Login()
         self.log.show()
        

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Signup()
        window.show()
        sys.exit(app.exec())