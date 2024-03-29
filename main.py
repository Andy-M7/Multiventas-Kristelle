import sys
from PyQt5 import QtWidgets
from vista.login import Login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_login = Login()
    app.exec_()