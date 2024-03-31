from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class Barra_Menu(QWidget):
    def __init__(self, parent=None):
        super(Barra_Menu, self).__init__(parent)
        self.parent = parent
        layout = QVBoxLayout()

        parent.btn_menu_bar.clicked.connect(self.mover_menu)
        parent.setLayout(layout)

    def mover_menu(self):
        if self.parent.frame_menu.isVisible():
            self.parent.frame_menu.hide()
            self.parent.lbl_menu1.hide()
        else:
            self.parent.frame_menu.show()
            self.parent.lbl_menu1.show()
