from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

class Barra_titulo():
    def __init__(self, parent):
        self.parent = parent

        # Eliminar barra de titulo
        self.parent.setWindowFlag(Qt.FramelessWindowHint)
        self.parent.setWindowOpacity(1)
        self.parent.btn_restaurar.hide()


        # Conectar botones   
        self.parent.BarraTitulo.mousePressEvent = self.mousePressEvent
        self.parent.BarraTitulo.mouseMoveEvent = self.mover_ventana
        self.parent.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.parent.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.parent.btn_restaurar.clicked.connect(self.control_btn_restaurar)
        self.parent.btn_cerrar.clicked.connect(self.control_btn_cerrar)

    def eventFilter(self, obj, event):
        if obj == self.parent and event.type() == QEvent.WindowStateChange:
            self.parent.changeEvent(event)
        return super().eventFilter(obj, event)
    
    # controlar botones
    def control_btn_minimizar(self):
        self.parent.setWindowIcon(QIcon("./icon/miapp.ico"))
        self.parent.showMinimized()

    def control_btn_maximizar(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()
    
    def control_btn_restaurar(self):
        self.parent.showNormal()

    def control_btn_cerrar(self):
        self.parent.close()
    
    # Arrastrar la ventana
    def mover_ventana(self, event):
        if self.parent.isMaximized() == False:
            if event.buttons() == Qt.LeftButton:
                if hasattr(self.parent, 'clickPosition'):
                    self.parent.move(self.parent.pos() + event.globalPos() - self.parent.clickPosition)
                    self.parent.clickPosition = event.globalPos()
                    event.accept()
        if event.globalPos().y() <= 20:
            self.parent.showMaximized()
        else:
            self.parent.showNormal()
            
    def mousePressEvent(self, event):
        self.parent.clickPosition = event.globalPos()

    
    