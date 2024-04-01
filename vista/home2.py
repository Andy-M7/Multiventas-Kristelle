#codigo de prueba
from PyQt5 import QtWidgets, uic
from controlador.titleBar import Barra_titulo
from controlador.menuBar import Barra_Menu
from controlador.paginas import Paginas


class Home(QtWidgets.QMainWindow):
    
    def __init__(self, instanse_paginas, parent=None):
        super(Home, self).__init__(parent)
        # Configurar la interfaz de usuario y otros elementos
        uic.loadUi("UI/Home.ui", self) 

        # Configurar la barra de título personalizada
        self.barra_titulo = Barra_titulo(self)

        # Configurar la barra de menú personalizada
        self.barra_menu = Barra_Menu(self)
        #self.setCentralWidget(self.barra_menu) 

        self.paginas = Paginas()

        # Llamar al método mostrar_pagina en la instancia de Paginas
        self.paginas.mostrar_pagina(self)