from PyQt5.QtWidgets import QPushButton
from controlador import mostrarUsuario, mostrarCliente, mostrarProducto

count = 0

class Paginas:
    def __init__(self, parent):
        self.parent = parent

        self.parent.btn_inicio.clicked.connect(self.mostrar_pagina)
        self.parent.btn_lista_usuario.clicked.connect(self.mostrar_pagina)
        self.parent.btn_nuevo_usuario.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListCliente.clicked.connect(self.mostrar_pagina)
        self.parent.btn_NewCliente.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListProductos.clicked.connect(self.mostrar_pagina)
        self.parent.btn_Consultar_Usuario.clicked.connect(self.user_list)
        self.parent.btn_Newproductos.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListVentas.clicked.connect(self.mostrar_pagina)
        self.parent.btn_NewVentas.clicked.connect(self.mostrar_pagina)
        self.parent.btn_Empresa.clicked.connect(self.mostrar_pagina)
        

    def capturar_pagina(self, button):
        if button == self.parent.btn_inicio:
            pagname = "page_inicio"

        elif button == self.parent.btn_lista_usuario:
            self.parent.tbl_Usuario.clearContents()
            self.parent.tbl_Usuario.setRowCount(0)    
            mostrarUsuario.Mostrar_usuario.mostrar_todos_usuarios            
            pagname = "page_user_list"

        elif button == self.parent.btn_nuevo_usuario:
            pagname = "page_new_user"

        elif button == self.parent.btn_ListCliente:
            self.parent.tbl_Cliente.clearContents()
            self.parent.tbl_Cliente.setRowCount(0)    
            mostrarCliente.Mostrar_cliente.mostrar_todos_clientes
            pagname = "page_client_list"

        elif button == self.parent.btn_NewCliente:
            pagname = "page_new_client"

        elif button == self.parent.btn_ListProductos:
            self.parent.tbl_Productos.clearContents()
            self.parent.tbl_Productos.setRowCount(0)    
            mostrarProducto.Mostrar_producto.mostrar_todos_productos
            pagname = "page_product_list"

        elif button == self.parent.btn_Newproductos:
            pagname = "page_new_product"

        elif button == self.parent.btn_ListVentas:
            pagname = "page_sold_list"

        elif button == self.parent.btn_NewVentas:
            pagname = "page_new_sold"

        elif button == self.parent.btn_Empresa:
            pagname = "page_empresa"
            
        else:
            pagname = None
        return pagname

    def mostrar_pagina(self):
        button = self.parent.sender()
        if button:
            page_name = self.capturar_pagina(button)
            if page_name:
                widget = getattr(self.parent, page_name, None)
                if widget:
                    self.parent.WitgetDatos.setCurrentWidget(widget)

    #probar agregar boton en las celdas
    def user_list(self):
        button = QPushButton("Click me")
        button
        self.parent.tbl_Usuario.setCellWidget(1, 1, button)