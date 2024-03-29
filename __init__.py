# codigos de referencias
import sys, time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton

qtCreatorFileLogin = "MainWindow.ui"
qtCreatorFileMenu = "windows/home.ui"

class FormularioLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioLogin, self).__init__()
        uic.loadUi(qtCreatorFileLogin, self)
        self.btn_login_init.clicked.connect(self.iniciar)
        
                
        self.show()
        
    def iniciar(self):
        username = self.txt_user.text()
        password = self.txt_password.text()

        # Aquí puedes implementar tu lógica de autenticación
        # Por ejemplo, podrías comprobar si el usuario y la contraseña son correctos

        # Simplemente para este ejemplo, comprobamos si el usuario y la contraseña son "admin"
        if username == "admin" and password == "admin":
            self.mostrar_menu()
        #else:
        #    QMessageBox.warning(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos")

    def mostrar_menu(self):
        self.segundo_formulario = FormularioMenu()
        self.segundo_formulario.show()
        self.close()
        
    

class FormularioMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioMenu, self).__init__()
        uic.loadUi(qtCreatorFileMenu, self)
        
        self.btn_usuario.clicked.connect(self.ocultar)
        self.targetBtn = QPushButton('target', self)
        self.targetBtn.move(100, 100)
        self.setGeometry(100, 100, 300, 300)
        self.show()   
         
    def ocultar(self):
        self.targetBtn.setEnabled(False)

        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioLogin()
    sys.exit(app.exec())


    def mover_menu(self):
        if True:
            width = self.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 400
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()