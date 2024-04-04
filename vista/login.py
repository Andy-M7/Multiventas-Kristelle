from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from vista.home import Home

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/Login.ui', self)
        self.btn_login_init.clicked.connect(self.verify_login)
        self.home_window = None

    def verify_login(self):
        usuario = self.txt_user.text()
        contraseña = self.txt_password.text()
        if usuario == "admin" and contraseña == "1234":
            self.home_window = Home()
            self.home_window.show()
            self.hide()
