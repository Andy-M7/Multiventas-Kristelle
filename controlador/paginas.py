from PyQt5.QtWidgets import QWidget

class Paginas(QWidget):
    def __init__(self, parent=None):
        super(Paginas, self).__init__(parent)
        self.parent = parent

        self.parent.btn_inicio.clicked.connect(self.mostrar_pagina)
        self.parent.btn_lista_usuario.clicked.connect(self.mostrar_pagina)
        self.parent.btn_nuevo_usuario.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListCliente.clicked.connect(self.mostrar_pagina)
        self.parent.btn_NewCliente.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListProductos.clicked.connect(self.mostrar_pagina)
        self.parent.btn_Newproductos.clicked.connect(self.mostrar_pagina)
        self.parent.btn_ListVentas.clicked.connect(self.mostrar_pagina)
        self.parent.btn_NewVentas.clicked.connect(self.mostrar_pagina)
        self.parent.btn_Empresa.clicked.connect(self.mostrar_pagina)

    def capturar_pagina(self, button):
        if button == self.parent.btn_inicio:
            pagname = "page_inicio"
        elif button == self.parent.btn_lista_usuario:
            pagname = "page_user_list"
        elif button == self.parent.btn_nuevo_usuario:
            pagname = "page_new_user"
        elif button == self.parent.btn_ListCliente:
            pagname = "page_client_list"
        elif button == self.parent.btn_NewCliente:
            pagname = "page_new_client"
        elif button == self.parent.btn_ListProductos:
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
        button = self.sender()
        if button:
            page_name = self.capturar_pagina(button)
            if page_name:
                widget = getattr(self.parent, page_name, None)
                if widget:
                    self.parent.WitgetDatos.setCurrentWidget(widget)