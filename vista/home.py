from PyQt5 import QtWidgets, uic
#from vista.VentanaProductos import VentanaProductos
#from vista.VentanaClientes import VentanaClientes

class Home(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        super(Home, self).__init__(parent)
        uic.loadUi("UI/Home.ui", self) 
        
    #    self.btnProductos.clicked.connect(self.AbrirVentanaProductos)
    #    self.btnClientes.clicked.connect(self.AbrirVentanaClientes)
        
    #def AbrirVentanaProductos (self):
    #    vproductos = VentanaProductos(self)
    #    vproductos.show()
        
    #def AbrirVentanaClientes (self):
    #    vclientes = VentanaClientes(self)
    #    vclientes.show()   