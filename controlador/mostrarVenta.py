from functools import partial
from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView, QComboBox

conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKristelle")

class Mostrar_venta:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btn_ListVentas.clicked.connect(self.mostrar_todas_ventas) # Llamar a la función para mostrar todas las ventas al iniciar       
        self.parent.btn_Consultar_Venta.clicked.connect(self.buscar_venta)
        self.parent.btn_P_venta.clicked.connect(self.buscar_P_venta)

    def mostrar_todas_ventas(self):               
        # Obtener todas las ventas
        ventas = conexion.obtener_todas_ventas()
        # Mostrar todas las ventas en la tabla
        for venta in ventas:
            self.mostrar_venta_en_tabla(venta)
        # Cerrar la conexión
        #conexion.cerrar_conexion()

    def buscar_venta(self):      
        id_venta = self.parent.txt_buscar_venta.text()
        # Obtener la venta por ID
        venta = conexion.obtener_venta(id_venta)     
        if venta:
            # Venta encontrada
            self.mostrar_venta_en_tabla(venta)
        else:
            # Venta no encontrada
            QMessageBox.warning(self.parent, "Venta no encontrada", "ID de venta no existe")
        #conexion.cerrar_conexion()

    def mostrar_venta_en_tabla(self, venta):
        # Agrega la venta a la tabla
        row_count = self.parent.tbl_Venta.rowCount()
        self.parent.tbl_Venta.insertRow(row_count)
        self.parent.tbl_Venta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(venta):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_Venta.setItem(row_count, col_idx, item)
        # Agregar botones "Actualizar" y "Eliminar" a la fila
        btn_actualizar = QPushButton("Actualizar")
        btn_eliminar = QPushButton("Eliminar")
        # Conectar los botones a sus respectivas funciones, pasando el índice de la fila como argumento
        btn_actualizar.clicked.connect(partial(self.actualizar_venta, row_count))
        btn_eliminar.clicked.connect(partial(self.eliminar_venta, row_count))
        # Agregar los botones a la fila en las columnas respectivas
        self.parent.tbl_Venta.setCellWidget(row_count, len(venta), btn_actualizar)
        self.parent.tbl_Venta.setCellWidget(row_count, len(venta) + 1, btn_eliminar)

    def actualizar_venta(self, row):
        item = self.parent.tbl_Venta.item(row, 0)
        if item is not None:
            valor = item.text()
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Venta no encontrada", "Actualiza la página")

    def eliminar_venta(self, row):
        item = self.parent.tbl_Venta.item(row, 0)
        if item is not None:
            valor = item.text()
            Mostrar_venta.mostrar_todas_ventas
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Venta no encontrada", "Actualiza la página")

    # PRODUCTOS PARA SELECCIONAR EN VENTA
    
    def buscar_P_venta(self):      
        id_Pventa = self.parent.txt_Pventa.text()
        # Obtener la venta por ID
        Pventa = conexion.obtener_p_venta(id_Pventa)     
        if Pventa:
            # Venta encontrada
            self.mostrar_P_venta(Pventa)
        else:
            # Venta no encontrada
            QMessageBox.warning(self.parent, "Venta no encontrada", "ID de venta no existe")
        # Cerrar la conexión
        #conexion.cerrar_conexion()

    def mostrar_P_venta(self, venta):
        row_count = self.parent.tbl_P_venta.rowCount()
        self.parent.tbl_P_venta.insertRow(row_count)
        self.parent.tbl_P_venta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(venta):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_P_venta.setItem(row_count, col_idx, item)
        combo_stock = QComboBox()
        # Aquí debes llenar el QComboBox con los valores de stock disponibles para el producto
        # Supongamos que tienes una lista llamada stock_disponible con los valores de stock
        stock_disponible = [1, 2, 3, 4, 5]  # Ejemplo de valores de stock disponibles
        combo_stock.addItems([str(stock) for stock in stock_disponible])
        self.parent.tbl_P_venta.setCellWidget(row_count, len(venta), combo_stock)
        btn_agregar = QPushButton("Añadir")
        btn_agregar.clicked.connect(partial(self.agregar_venta, row_count))
        self.parent.tbl_P_venta.setCellWidget(row_count, len(venta) + 1, btn_agregar)

    def agregar_venta(self, row):
        codigo_item = self.parent.tbl_P_venta.item(row, 0)
        cantidad_combo = self.parent.tbl_P_venta.cellWidget(row, self.parent.tbl_P_venta.columnCount() - 2).currentText()
        if codigo_item is not None:
            codigo = codigo_item.text()
            cantidad = int(cantidad_combo)  # Convertir la cantidad a entero
            producto, precio = conexion.obtener_precio_producto(codigo)
            if producto and precio:
                self.insertar_detalle_venta(codigo, producto, cantidad, precio)
                # Agregar el botón "Remover" a la fila correspondiente en tbl_detalle_venta
                row_count_detalle = self.parent.tbl_detalle_venta.rowCount()  # Nuevo contador de filas para tbl_detalle_venta
                col_count_detalle = self.parent.tbl_detalle_venta.columnCount()  # Nuevo contador de columnas para tbl_detalle_venta
                btn_remover = QPushButton("Remover")
                btn_remover.clicked.connect(partial(self.remover_venta, row_count_detalle))  # Usar el nuevo contador de filas
                print("Fila para tbl_detalle_venta:", row_count_detalle)
                print("Columna para tbl_detalle_venta:", col_count_detalle)
                self.parent.tbl_detalle_venta.setCellWidget(row_count_detalle, col_count_detalle + 1, btn_remover)
            else:
                QMessageBox.warning(self.parent, "Producto no encontrado", "No se encontró el producto en la base de datos")
        else:
            QMessageBox.warning(self.parent, "Venta no encontrada", "Actualiza la página")

    def insertar_detalle_venta(self, codigo_producto, nombre_producto, cantidad, precio):
        subtotal = cantidad * precio
        nueva_fila = [codigo_producto, nombre_producto, cantidad, precio, subtotal]
        row_count_detalle = self.parent.tbl_detalle_venta.rowCount()  # Nuevo contador de filas para tbl_detalle_venta
        self.parent.tbl_detalle_venta.insertRow(row_count_detalle)
        for col_idx, valor in enumerate(nueva_fila):
            item = QTableWidgetItem(str(valor))
            self.parent.tbl_detalle_venta.setItem(row_count_detalle, col_idx, item)

    def remover_venta(self, row):
        # Aquí deberías remover la fila correspondiente en tbl_detalle_venta
        pass