#codigo de prueba
from PyQt5 import QtWidgets, uic
from controlador.titleBar import Barra_titulo
from controlador.menuBar import Barra_Menu

class Home(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # Configurar la interfaz de usuario y otros elementos
        uic.loadUi("UI/Home.ui", self) 

        # Configurar la barra de título personalizada
        self.barra_titulo = Barra_titulo(self)

        # Configurar la barra de menú personalizada
        self.barra_menu = Barra_Menu(self)
        #self.setCentralWidget(self.barra_menu) 