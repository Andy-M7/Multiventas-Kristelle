#codigo de prueba
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from controlador.titleBar import Barra_titulo
from controlador.menuBar import Barra_Menu
from controlador.paginas import Paginas


class Home(QMainWindow):
    
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # Configurar la interfaz de usuario y otros elementos
        uic.loadUi("UI/Home.ui", self) 

        # Configurar la barra de menú personalizada
        self.barra_menu = Barra_Menu(self)
        self.paginas = Paginas(self)
        self.barra_titulo = Barra_titulo(self)