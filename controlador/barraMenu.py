#codigo de prueba
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent, Qt

class Barra_titulo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Barra_titulo, self).__init__(parent)
        self.parent = parent

        # Eliminar Barra y opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Conectar botón de cerrar
        parent.btn_cerrar.clicked.connect(parent.close)

        # Conectar botón de minimizar
        parent.btn_minimizar.clicked.connect(parent.showMinimized)

        # Conectar botón de restaurar/maximizar
        parent.btn_restaurar.clicked.connect(self.toggle_restore_maximize)

        # Cambiar tamaño
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(parent) 
        self.grip.resize(self.gripSize, self.gripSize)

        # Mover ventana
        parent.mouseMoveEvent = self.mover_ventana

    def toggle_restore_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    def mover_ventana(self, event):
        if self.parent.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                self.parent.move(self.parent.pos() + event.globalPos() - self.parent.clickPosition)
                self.parent.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.parent.showMaximized()
        else:
            self.parent.showNormal()

    def resizeEvent(self, event):
        rect = self.parent.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.parent.clickPosition = event.globalPos()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if event.oldState() & Qt.WindowMinimized:
                # La ventana estaba minimizada antes del cambio de estado
                if self.parent.windowState() & Qt.WindowMaximized:
                    # Si la ventana se maximizó, no la minimicemos nuevamente
                    return
                if self.parent.window_state_before_minimize is not None:
                    # Restaurar el estado de la ventana antes de minimizar
                    self.parent.setWindowState(self.parent.window_state_before_minimize)
                    self.parent.show()
            elif self.parent.windowState() & Qt.WindowMinimized:
                # Guardar el estado de la ventana antes de minimizar
                self.parent.window_state_before_minimize = self.parent.windowState()
