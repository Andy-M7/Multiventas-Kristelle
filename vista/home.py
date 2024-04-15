from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from controlador import mostrarUsuario, paginas, menuBar, titleBar, registrarUsuario
from controlador import registrarCliente, registrarProducto, mostrarCliente, mostrarVenta, mostrarProducto

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/Home.ui', self)
        self.login_window = None  # Referencia a la ventana de inicio de sesión

        self.barra_menu = menuBar.Barra_Menu(self)
        self.paginas = paginas.Paginas(self)
        self.barra_titulo = titleBar.Barra_titulo(self)
        self.registrarUsuario = registrarUsuario.RegistrarUsuario(self)
        self.registrarCliente = registrarCliente.RegistrarCliente(self)
        self.registrarProducto = registrarProducto.RegistrarProducto(self)
        self.mostrarUsuario = mostrarUsuario.Mostrar_usuario(self)
        self.mostrarCliente = mostrarCliente.Mostrar_cliente(self)
        self.mostrarVentas = mostrarVenta.Mostrar_venta(self)
        self.mostrarProductos = mostrarProducto.Mostrar_producto(self)

        self.installEventFilter(self)
        self.windowTitleChanged.connect(self.on_window_state_changed)
        self.window_minimized = False

    # Verificaciones de cambios en la ventana
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self.btn_maximizar.setIcon(QIcon("./icon/restaurar.png"))
                self.btn_maximizar.hide()
                self.btn_restaurar.show()
            else:
                self.btn_maximizar.setIcon(QIcon("./icon/maximizar.png"))
                self.btn_maximizar.show()
                self.btn_restaurar.hide()

    def on_window_state_changed(self, state):
        if state & Qt.WindowMinimized:
            self.window_minimized = True
        else:
            if self.window_minimized:
                if not self.isMinimized():
                    # Restaura la configuración de la ventana
                    self.setWindowFlag(Qt.Tool, True)
                    self.showNormal()
                    self.window_minimized = False
        

    def closeEvent(self, event):
        if self.login_window:
            self.login_window.show()