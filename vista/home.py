from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

class Home(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        uic.loadUi("UI/Home.ui", self) 

        self.btn_close.clicked.connect(self.cerrar)
        self.btn_minimizar.clicked.connect(self.minimizar)

        # Ocultar barra de tareas
        self.setWindowFlag(Qt.FramelessWindowHint)
        
    def cerrar(self):
        self.close()

    def minimizar(self):
        self.setWindowState(Qt.WindowMinimized)

        
    #    self.btnProductos.clicked.connect(self.AbrirVentanaProductos)
    #    self.btnClientes.clicked.connect(self.AbrirVentanaClientes)
        
    #def AbrirVentanaProductos (self):
    #    vproductos = VentanaProductos(self)
    #    vproductos.show()
        
    #def AbrirVentanaClientes (self):
    #    vclientes = VentanaClientes(self)
    #    vclientes.show()   