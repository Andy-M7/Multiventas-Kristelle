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