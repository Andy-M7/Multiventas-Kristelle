from PyQt5 import QtWidgets, uic
from vista.home import Home

qtCreatorFile = "UI/Login.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi(qtCreatorFile,self)

        self.show()
        self.btn_login_init.clicked.connect(self.iniciarSesion)

    def iniciarSesion(self):
        usuario = self.txt_user.text()
        contraseña = self.txt_password.text()
        if usuario == "admin" and contraseña == "1234":
            self.close()
            vprincipal = Home(self)
            vprincipal.show()