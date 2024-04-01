from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel,QFrame

class Barra_Menu(QWidget):
    def __init__(self, parent=None):
        super(Barra_Menu, self).__init__(parent)
        self.parent = parent
        
        # Ocultar los botones al inicio
        self.parent.btn_lista_usuario.hide()
        self.parent.btn_nuevo_usuario.hide()
        self.parent.btn_ListCliente.hide()
        self.parent.btn_NewCliente.hide()
        self.parent.btn_ListProductos.hide()
        self.parent.btn_Newproductos.hide()
        self.parent.btn_ListVentas.hide()
        self.parent.btn_NewVentas.hide()
        self.parent.btn_Empresa.hide()
        self.parent.btn_nuevo_usuario.hide()

        parent.btn_menu_bar.clicked.connect(self.mover_menu)
        parent.btn_usuario.clicked.connect(self.menu_usuario)
        parent.btn_Clientes.clicked.connect(self.menu_cliente)
        parent.btn_Productos.clicked.connect(self.menu_producto)
        parent.btn_Ventas.clicked.connect(self.menu_venta)
        parent.btn_Config.clicked.connect(self.menu_config)
        parent.btn_SessionClose.clicked.connect(self.cerrar_session)

    def mover_menu(self):
        if self.parent.frame_menu.isVisible():
            self.parent.frame_menu.hide()
            self.parent.lbl_menu1.hide()
        else:
            self.parent.frame_menu.show()
            self.parent.lbl_menu1.show()

    def menu_usuario(self):
        if self.parent.btn_lista_usuario.isHidden():
            self.parent.btn_lista_usuario.show()
            self.parent.btn_nuevo_usuario.show()
        else:
            self.parent.btn_lista_usuario.hide()
            self.parent.btn_nuevo_usuario.hide()

    def menu_cliente(self):
        if self.parent.btn_ListCliente.isHidden():
            self.parent.btn_ListCliente.show()
            self.parent.btn_NewCliente.show()
        else:
            self.parent.btn_ListCliente.hide()
            self.parent.btn_NewCliente.hide()

    def menu_producto(self):
        if self.parent.btn_ListProductos.isHidden():
            self.parent.btn_ListProductos.show()
            self.parent.btn_Newproductos.show()
        else:
            self.parent.btn_ListProductos.hide()
            self.parent.btn_Newproductos.hide()

    def menu_venta(self):
        if self.parent.btn_ListVentas.isHidden():
            self.parent.btn_ListVentas.show()
            self.parent.btn_NewVentas.show()
        else:
            self.parent.btn_ListVentas.hide()
            self.parent.btn_NewVentas.hide()
    
    def menu_config(self):
        if self.parent.btn_Empresa.isHidden():
            self.parent.btn_Empresa.show()
            self.parent.btn_nuevo_usuario.show()
        else:
            self.parent.btn_Empresa.hide()
            self.parent.btn_nuevo_usuario.hide()

    def cerrar_session(self):
        self.parent.close()