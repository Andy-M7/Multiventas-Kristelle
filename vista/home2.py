#codigo de prueba
from PyQt5 import QtWidgets, uic
from controlador.barraMenu import Barra_titulo

class Home(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # Configurar la interfaz de usuario y otros elementos
        uic.loadUi("UI/Home.ui", self) 

        # Configurar la barra de título personalizada
        self.title_bar = Barra_titulo(self)

        # Menu lateral
        self.btn_menu_bar.clicked.connect(self.mover_menu)

    def mover_menu(self):
        if self.frame_menu.isVisible():
            self.frame_menu.hide()
            self.MarginOcultar.hide()
        else:
            self.frame_menu.show()
            self.MarginOcultar.show()

