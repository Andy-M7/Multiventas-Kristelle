import sys
from PyQt5 import QtWidgets
from vista.login import Login
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon/miapp.ico'))
    ventana_login = Login()
    ventana_login.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets, uic
from vista.home2 import Home
from PyQt5.QtGui import QIcon

qtCreatorFile = "UI/Login.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi(qtCreatorFile, self)
      

        self.show()
        self.btn_login_init.clicked.connect(self.iniciarSesion)
        self.setWindowIcon(QIcon("./icon/miapp.ico"))
    

    def iniciarSesion(self):
        usuario = self.txt_user.text()
        contraseña = self.txt_password.text()
        if usuario == "admin" and contraseña == "1234":
            self.close()
            vprincipal = Home(self)
            vprincipal.show()

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
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class Barra_Menu(QWidget):
    def __init__(self, parent=None):
        super(Barra_Menu, self).__init__(parent)
        self.parent = parent
        parent.btn_menu_bar.clicked.connect(self.mover_menu)

    def mover_menu(self):
        if self.parent.frame_menu.isVisible():
            self.parent.frame_menu.hide()
            self.parent.lbl_menu1.hide()
        else:
            self.parent.frame_menu.show()
            self.parent.lbl_menu1.show()

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class Barra_titulo(QWidget):
    def __init__(self, parent=None):
        super(Barra_titulo, self).__init__(parent)
        self.parent = parent

        # Eliminar barra de titulo
        self.parent.setWindowFlag(Qt.FramelessWindowHint)
        self.parent.setWindowFlag(Qt.Tool)
        self.parent.setWindowOpacity(1)
        self.parent.btn_restaurar.hide()

        # Conectar botones   
        parent.BarraTitulo.mousePressEvent = self.mousePressEvent
        parent.BarraTitulo.mouseMoveEvent = self.mover_ventana
        parent.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        parent.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        parent.btn_restaurar.clicked.connect(self.control_btn_restaurar)
        parent.btn_cerrar.clicked.connect(self.control_btn_cerrar)
        

        # Conectar el evento changeEvent
        parent.installEventFilter(self)
        parent.windowTitleChanged.connect(self.on_window_state_changed)

        self.window_minimized = False
        
    def eventFilter(self, obj, event):
        if obj == self.parent and event.type() == QEvent.WindowStateChange:
            self.changeEvent(event)
        return super().eventFilter(obj, event)
        
    # controlar botones
    def control_btn_minimizar(self):
        self.parent.setWindowIcon(QIcon("./icon/miapp.ico"))
        self.parent.showMinimized()

    def control_btn_maximizar(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()
    
    def control_btn_restaurar(self):
        self.parent.showNormal()

    def control_btn_cerrar(self):
        self.parent.close()
    
    # Arrastrar la ventana
    def mover_ventana(self, event):
        if self.parent.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                if hasattr(self.parent, 'clickPosition'):
                    self.parent.move(self.parent.pos() + event.globalPos() - self.parent.clickPosition)
                    self.parent.clickPosition = event.globalPos()
                    event.accept()
        if event.globalPos().y() <= 20:
            self.parent.showMaximized()
        else:
            self.parent.showNormal()
            
    def mousePressEvent(self, event):
        self.parent.clickPosition = event.globalPos()

    # Verificaciones de cambios en la ventana
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.parent.isMaximized():
                self.parent.btn_maximizar.setIcon(QIcon("./icon/restaurar.png"))
            else:
                self.parent.btn_maximizar.setIcon(QIcon("./icon/maximizar.png"))
            if self.parent.isMaximized():
                self.parent.btn_maximizar.hide()
                self.parent.btn_restaurar.show()
            else:
                self.parent.btn_maximizar.show()
                self.parent.btn_restaurar.hide()

    def on_window_state_changed(self, state):
        if state & Qt.WindowMinimized:
            self.window_minimized = True
        else:
            if self.window_minimized:
                if not self.parent.isMinimized():
                # Restaura la configuración de la ventana
                    self.parent.setWindowFlag(Qt.Tool, True)
                    self.parent.showNormal()
                    self.window_minimized = False