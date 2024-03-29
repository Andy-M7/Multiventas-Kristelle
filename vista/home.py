import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QThread, Qt, QEvent, QPropertyAnimation

class Home(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        # Configurar la interfaz de usuario y otros elementos
        uic.loadUi("UI/Home.ui", self) 
        

        # Eliminar  Barra y opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Cambiar tamaño
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self) 
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        self.BarraTitulo.mouseMoveEvent= self.mover_ventana

        # Acceder paginas
        self.btn_inicio.clicked.connect(self.mostrar_pagina_1)


        # Control barra de titulo
        self.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.btn_restaurar.clicked.connect(self.control_btn_normal)
        self.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.btn_cerrar.clicked.connect(self.control_btn_cerrar)

        # Menu lateral
        self.btn_menu_bar.clicked.connect(self.mover_menu)

    def control_btn_minimizar(self):
        self.showMinimized()

    def control_btn_normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()


    def mover_menu(self):
        if self.frame_menu.isVisible():
            self.frame_menu.hide()
            self.MarginOcultar.hide()
        else:
            self.frame_menu.show()
            self.MarginOcultar.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

    def control_btn_cerrar(self):
        self.close()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() & Qt.WindowMinimized:
                # La ventana estaba minimizada antes del cambio de estado
                if self.windowState() & Qt.WindowMaximized:
                    # Si la ventana se maximizó, no la minimicemos nuevamente
                    return
                if self.window_state_before_minimize is not None:
                    # Restaurar el estado de la ventana antes de minimizar
                    self.setWindowState(self.window_state_before_minimize)
                    self.show()
            elif self.windowState() & Qt.WindowMinimized:
                # Guardar el estado de la ventana antes de minimizar
                self.window_state_before_minimize = self.windowState()

    def mostrar_pagina_1(self):
        self.WitgetDatos.setCurrentWidget(self.page_1)