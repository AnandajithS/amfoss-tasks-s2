
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
import os

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.w = None        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        self.setStyleSheet("""
            
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

        self.background=QLabel(self)
        self.background.setGeometry(0,0,self.width(),self.height())
        self.background.setStyleSheet("background-image: url('../assets/landing.jpg'); background-repeat: no-repeat; background-position: center;") 
        self.background.lower()


        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search_pokemon)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_pokemon)

        self.infobox=QLabel(self)
        self.infobox.setGeometry(425, 100, 425, 500)
        self.infobox.setWordWrap(True)

    def search_pokemon(self):
        self.pname=self.textbox.text()
        self.url=f'https://pokeapi.co/api/v2/pokemon/{self.pname}'
        self.response=requests.get(self.url)
        abilities=", ".join([i['ability']['name'] for i in self.response.json()['abilities']])
        types=", ".join([i['type']['name'] for i in self.response.json()['types']])
        stats="\n".join([f"{i['stat']['name']}: {i['base_stat']}" for i in self.response.json()['stats']])
        self.imageurl = self.response.json()['sprites']['other']['official-artwork']['front_default']

        self.artwork=QLabel(self)
        self.artwork.setGeometry(425,0,200,200)
        self.image=requests.get(self.imageurl)
        pixmap=QPixmap()
        pixmap.loadFromData(self.image.content)
        pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.artwork.setPixmap(pixmap)
        infotext=(f"Name: {self.pname}\nAbilities: {abilities}\nTypes: {types}\nStats:\n{stats}")
        self.background.setVisible(False)
        self.artwork.show()
        self.infobox.setText(infotext)
        self.infobox.setStyleSheet("font-size: 19px")

    def capture_pokemon(self):
        os.makedirs("captured", exist_ok=True)
        self.capturedlist=os.listdir("captured")
        if f"{self.pname}.png" in self.capturedlist:
            QMessageBox.warning(self, "Pokedex", f"Pokemon already caught!")
        else:
            self.filepath=f"captured/{self.pname}.png"
            with open(self.filepath,'wb') as file:
                file.write(self.image.content)
            QMessageBox.information(self, "Pokedex", f"Pokemon captured successfully!")

    def prev(self):
        if self.index>0:
            self.index-=1
        else:
            self.index=len(self.capturedlist)-1
        self.update_info()
           
    def next(self):
        if self.index<len(self.capturedlist)-1:
            self.index+=1
        else:
            self.index=0
        self.update_info()
    
    def update_info(self):
        self.displayname = self.capturedlist[self.index].replace(".png", "") 
        self.namelabel.setText(self.displayname)
        imagepath = f"captured/{self.displayname}.png"
        pixmap = QPixmap(imagepath)
        self.imagelabel.setPixmap(pixmap)


    def display_pokemon(self):
        self.w = QWidget()
        self.w.setWindowTitle("Captured Pokémon")
        self.w.setGeometry(0, 0, 700, 700)

        self.capturedlist=os.listdir("captured")
        self.index = 0

        self.namelabel = QLabel(self.w)
        self.namelabel.setGeometry(0, 575, 500, 50)
        self.namelabel.setStyleSheet("font-size: 30px")
        button_stylesheet = """
        QPushButton {
            background-color: black;
            color: white;
            border: 1px solid #BA263E;
            font: bold 16px;
            text-align: center;
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: #BA263E;
            color: black;
        }"""


        prev_button = QPushButton("Previous", self.w)
        prev_button.setGeometry(0, 660, 300, 40)
        prev_button.setStyleSheet(button_stylesheet)
        prev_button.clicked.connect(self.prev)
            
        next_button = QPushButton("Next", self.w)
        next_button.setGeometry(400, 660, 300, 40)
        next_button.setStyleSheet(button_stylesheet)
        next_button.clicked.connect(self.next)

        self.imagelabel = QLabel(self.w)
        self.imagelabel.setGeometry(0, 0, 700, 550)
        self.imagelabel.setScaledContents(True)
  
        self.update_info()
        self.w.show()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
