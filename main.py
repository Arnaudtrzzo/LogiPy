from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton
import sys
from PyQt6.QtGui import QIcon,QCursor
from PyQt6.QtCore import Qt

class Fenetre(QWidget):#instantiation fenetre
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600) #position de la fenetre, taille de la fenetre
        #self.setFixedHeight(600) #hauteur de la fenetre
       # self.setFixedWidth(800) #largeur de la fenetre
       # self.setFixedSize(800, 600) #taille de la fenetre
        self.setWindowTitle("Ma première fenêtre")
        self.setWindowIcon(QIcon("images/IMG_5647.JPG")) #icone de la fenetre
        
        style_text = "font-size: 30px; color: #0066cc; font-weight: bold; background-color: #f0f0f0; border-radius: 10px; padding: 10px;"
        self.titre = QLabel("Bonjour tout le monde",self) #creation d'un label
        self.titre.setGeometry(250,50, 350, 100)  # Centered horizontally (800-300)/2 = 250
        self.titre.setStyleSheet(style_text) #style du label
        
        self.search = QLabel("Recherche",self)
        self.search.setGeometry(250, 200, 150, 50)
        self.search.setStyleSheet("""QLabel{
            font-size: 20px; color: #333; background-color: #f0f0f0; border-radius: 5px; padding: 10px;
        }
        """)
        
        self.input_search = QLineEdit(self)
        self.input_search.setGeometry(400, 200, 300, 50)
        self.input_search.setPlaceholderText("Entrer le texte")
        
        self.btn = QPushButton("Recherche",self)
        self.btn.setGeometry(400, 300, 150, 50)
        self.btn.setStyleSheet("""QPushButton{
            font-size: 20px; color: #fff; background-color: #0066cc; border-radius: 5px; padding: 10px;
        }
        
        
        QPushButton:hover{
            color:black;
            background-color:blue
            
            }""")
        
        self.btn.setCursor(QCursor(Qt.CursorShape.DragMoveCursor))
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Fenetre()
    fen.show()
    sys.exit(app.exec())

       