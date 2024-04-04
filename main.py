import sys
from PyQt5.QtWidgets import QApplication
from vista.login import Login
from vista.home import Home

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    home_window = Home()
    sys.exit(app.exec_())