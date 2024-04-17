from functools import partial
from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView

conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKristelle")
class Mostrar_producto:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btn_ListProductos.clicked.connect(self.mostrar_todos_productos) # Llamar a la función para mostrar todos los Productos al iniciar       
        self.parent.btn_Consultar_Producto.clicked.connect(self.buscar_producto)

    def mostrar_todos_productos(self):               
        # Obtener todos los usuarios
        productos = conexion.obtener_todos_productos()
        # Mostrar todos los usuarios en la tabla
        for producto in productos:
            self.mostrar_producto_en_tabla(producto)

    def buscar_producto(self):        
        id_usuario = self.parent.txt_buscar_Producto.text()
        # Obtener el Producto por ID
        producto = conexion.obtener_producto(id_usuario)
        self.parent.tbl_Productos.clearContents()
        self.parent.tbl_Productos.setRowCount(0)
        if producto:
            # Producto encontrado
            self.mostrar_producto_en_tabla(producto)
        else:
            # Producto no encontrado
            QMessageBox.warning(self.parent, "Producto no encontrado", "ID de Producto no existe")

    def mostrar_producto_en_tabla(self, producto):
    # Agrega el Producto a la tabla
        row_count = self.parent.tbl_Productos.rowCount()
        self.parent.tbl_Productos.insertRow(row_count)
        self.parent.tbl_Productos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(producto):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_Productos.setItem(row_count, col_idx, item)
        # Agregar botones "Actualizar" y "Eliminar" a la fila
        btn_actualizar = QPushButton("Actualizar")
        btn_eliminar = QPushButton("Eliminar")
        # Conectar los botones a sus respectivas funciones, pasando el índice de la fila como argumento
        btn_actualizar.clicked.connect(partial(self.actualizar_producto, row_count))
        btn_eliminar.clicked.connect(partial(self.eliminar_producto, row_count))
        # Agregar los botones a la fila en las columnas respectivas
        self.parent.tbl_Productos.setCellWidget(row_count, len(producto), btn_actualizar)
        self.parent.tbl_Productos.setCellWidget(row_count, len(producto) + 1, btn_eliminar)

    def actualizar_producto(self, row):
        item = self.parent.tbl_Productos.item(row, 0)
        if item is not None:
            valor = item.text()
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Usuario no encontrado", "Actualiza la pagina")

    def eliminar_producto(self, row):
        item = self.parent.tbl_Productos.item(row, 0)
        if item is not None:
            valor = item.text()
            Mostrar_producto.mostrar_todos_productos
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Usuario no encontrado", "Actualiza la pagina")