from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton,QComboBox
import sys
from tkinter import filedialog
from PyQt6.QtGui import QIcon,QCursor
from PyQt6.QtCore import Qt
from yt_dlp import YoutubeDL 

class YoutubeDown(QWidget):
    def __init__(self):
        super().__init__()
             
        self.setFixedSize(800, 600)
        self.setWindowTitle("Youtube Downloader")
        self.setStyleSheet("background-color: #f0f0f0;")

        self.titre = QLabel("Youtube Video Downloader", self)
        self.titre.setGeometry(250, 50, 400, 100)
        self.titre.setStyleSheet("""
            color: #e62117;
            font-size: 28px;
            font-weight: bold;
        """)

        self.text = QLabel("Enter YouTube URL:", self)
        self.text.setGeometry(250, 130, 400, 50)
        self.text.setStyleSheet("""
            color: #282828;
            font-size: 16px;
        """)

        self.lien = QLineEdit(self)
        self.lien.setGeometry(250, 180, 300, 40)
        self.lien.setStyleSheet("""
            QLineEdit {
            border: 2px solid #e62117;
            border-radius: 20px;
            padding: 5px 15px;
            background: black;
            font-size: 14px;
            }
            QLineEdit:focus {
            border: 2px solid #ff0000;
            }
        """)

        self.format = QComboBox(self)
        self.format.addItems(["Select Format", "mp3", "mp4"])
        self.format.setGeometry(250, 240, 150, 40)
        self.format.setStyleSheet("""
            QComboBox {
            border: 2px solid #e62117;
            border-radius: 20px;
            padding: 5px 15px;
            background: black;
            color: white;
            font-size: 14px;
            }
            QComboBox::drop-down {
            border: none;
            }
            QComboBox QAbstractItemView {
            background: black;
            color: white;
            selection-background-color: #e62117;
            selection-color: white;
            padding: 5px;
            }
        """)

        self.btn = QPushButton("Download", self)
        self.btn.setGeometry(250, 300, 150, 40)
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setStyleSheet("""
            QPushButton {
            background-color: #e62117;
            color: white;
            border-radius: 20px;
            font-size: 16px;
            font-weight: bold;
            }
            QPushButton:hover {
            background-color: #000;
            }
        """)
        self.btn.clicked.connect(self.telecharger)
        
            
    def telecharger(self):
        dest_fichier = filedialog.askdirectory()
        lien = self.lien.text()
        format = self.format.currentText()
        
        
        if lien and format and dest_fichier:
            try: 
                video_down ={
                    "format":format,
                    "outtmpl":f'{dest_fichier}/%(title)s.%(ext)s',
                }
                with YoutubeDL(video_down) as ydl:
                    ydl.download([lien])
                    print("Video telecharger")
            except:
                print("Erreur de telechargement")
            
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    down = YoutubeDown()
    down.show()
    sys.exit(app.exec())