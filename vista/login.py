from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from vista.home import Home
from controlador.conexion import DB_conexion

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/Login.ui', self)
        self.btn_login_init.clicked.connect(self.verify_login)
        self.home_window = None

    def verify_login(self):
        usuario = self.txt_user.text()
        contraseña = self.txt_password.text()

        try:
            # Crear una instancia de DB_conexion con los datos de conexión
            conexion = DB_conexion( Servidor="localhost",
                                    Usuario="sa",
                                    Password="12345",
                                    Base_Datos="MinimarketKristelle")
            
            # Verificar usuario
            if conexion.verificar_usuario(usuario, contraseña):
                # Inicio de sesión exitoso
                self.home_window = Home()
                self.home_window.show()
                self.hide()
            else:
                # Nombre de usuario o contraseña incorrectos
                QMessageBox.warning(self, "Inicio de Sesión Fallido", "Nombre de usuario o contraseña incorrectos")

            # Cerrar la conexión
            conexion.cerrar_conexion()

        except Exception as e:
            QMessageBox.critical(self, "Error", "Error al conectar a la base de datos: {}".format(e))