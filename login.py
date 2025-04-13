from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QCursor, QPixmap
from PyQt6.QtCore import Qt
import sys
from signup import Signup

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 500)  
        self.photo = QLabel(self)
        fond = QPixmap("images/IMG_5647.JPG")
        taille_images = fond.scaled(400, 500)  
        self.photo.setPixmap(taille_images)
        self.photo.setGeometry(0, 0, 400, 500)  
        self.setWindowTitle("Login")
        
        self.espace_log = QLabel(self)
        self.espace_log.setGeometry(50, 50, 300, 400)   
        self.espace_log.setStyleSheet("""QLabel{
            font-size: 16px;
            color: #fff;
            border-radius: 5px;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.7); 
        }
        """)
        
        style= "font-size: 20px; color: #000; font-weight: bold;" 
        style_btn = "color: #fff; background-color: #0066cc; border-radius: 5px; padding: 8px;"
        self.email_label = QLabel("Email:", self)
        self.email_label.setGeometry(70, 150, 100, 35)
        self.email_label.setStyleSheet(style)
        
        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(170, 150, 180, 35) 
        self.input_email.setPlaceholderText("Entrer votre Email")
        self.input_email.setStyleSheet(style_btn)
        
        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(70, 220, 100, 35) 
        self.password_label.setStyleSheet(style)
        
        self.input_password = QLineEdit(self)
        self.input_password.setGeometry(170, 220, 180, 35)   
        self.input_password.setPlaceholderText("Entrer votre mot de passe")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setStyleSheet(style_btn)
        
        self.login_button = QPushButton("Se Connecter", self)
        self.login_button.setGeometry(150, 290, 100, 35)
        self.login_button.setStyleSheet(style_btn)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        
        self.btn_to_signup = QPushButton("Si pas encore inscrit, inscrivez-vous", self)
        self.btn_to_signup.setGeometry(70, 350, 260, 35)
        self.btn_to_signup.setStyleSheet("""QPushButton{
            font-size: 14px;
            color: blue;
            background: none;
            border: none;
            border-bottom: 1px solid #000;
            padding: 8px;
        }
        QPushButton:hover {
            border-bottom: 2px solid #000;
        }""")
        self.btn_to_signup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.btn_to_signup.clicked.connect(self.inscription)
        
        
    def inscription(self):
        # print("Inscription")
        self.ouvrir_fen = Signup()
        self.ouvrir_fen.show()
        self.close()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    connex = Login()
    connex.show()
    sys.exit(app.exec())