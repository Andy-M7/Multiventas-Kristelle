from functools import partial
from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView

conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKristelle")

class Mostrar_venta:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btn_ListVentas.clicked.connect(self.mostrar_todas_ventas) # Llamar a la función para mostrar todas las ventas al iniciar       
        self.parent.btn_Consultar_Venta.clicked.connect(self.buscar_venta)

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

        # Cerrar la conexión
        conexion.cerrar_conexion()


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

    def mostrar_P_venta(self, venta):
    # Agrega la venta a la tabla
        self.parent.tbl_Usuario.clearContents()
        self.parent.tbl_Usuario.setRowCount(0) 
        row_count = self.parent.tbl_Venta.rowCount()
        self.parent.tbl_P_Venta.insertRow(row_count)
        self.parent.tbl_P_Venta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(venta):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_P_Venta.setItem(row_count, col_idx, item)

        # Agregar botones "Actualizar" y "Eliminar" a la fila
        btn_actualizar = QPushButton("Actualizar")
        btn_eliminar = QPushButton("Eliminar")

        # Conectar los botones a sus respectivas funciones, pasando el índice de la fila como argumento
        btn_actualizar.clicked.connect(partial(self.actualizar_venta, row_count))
        btn_eliminar.clicked.connect(partial(self.eliminar_venta, row_count))

        # Agregar los botones a la fila en las columnas respectivas
        self.parent.tbl_P_Venta.setCellWidget(row_count, len(venta), btn_actualizar)
        self.parent.tbl_P_Venta.setCellWidget(row_count, len(venta) + 1, btn_eliminar)

    def actualizar_venta(self, row):
        item = self.parent.tbl_P_Venta.item(row, 0)
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