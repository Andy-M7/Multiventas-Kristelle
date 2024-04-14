from functools import partial
from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView

conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKristelle")
class Mostrar_cliente:
    def __init__(self, parent):
        self.parent = parent
        #self.mostrar_todos_clientes()  # Llamar a la función para mostrar todos los clientes al iniciar
        self.parent.btn_Consultar_Cliente.clicked.connect(self.buscar_cliente)
        self.parent.btn_ListCliente.clicked.connect(self.mostrar_todos_clientes)
        

    def mostrar_todos_clientes(self): 
        # Obtener todos los usuarios
        clientes = conexion.obtener_todos_clientes()
        
        # Mostrar todos los usuarios en la tabla
        for cliente in clientes:
            self.mostrar_cliente_en_tabla(cliente)

        # Cerrar la conexión
        #conexion.cerrar_conexion()

    def buscar_cliente(self):       
        id_cliente = self.parent.txt_buscar_cliente.text()

        # Obtener el Cliente por ID
        cliente = conexion.obtener_cliente(id_cliente)
        
        if cliente:
            # Cliente encontrado
            self.mostrar_cliente_en_tabla(cliente)
        else:
            # Cliente no encontrado
            QMessageBox.warning(self.parent, "Cliente no encontrado", "ID de cliente no existe")

        # Cerrar la conexión
        conexion.cerrar_conexion()

    def mostrar_cliente_en_tabla(self, cliente):
    # Agrega el usuario a la tabla
        row_count = self.parent.tbl_Cliente.rowCount()
        self.parent.tbl_Cliente.insertRow(row_count)
        self.parent.tbl_Cliente.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(cliente):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_Cliente.setItem(row_count, col_idx, item)

        # Agregar botones "Actualizar" y "Eliminar" a la fila
        btn_actualizar = QPushButton("Actualizar")
        btn_eliminar = QPushButton("Eliminar")

        # Conectar los botones a sus respectivas funciones, pasando el índice de la fila como argumento
        btn_actualizar.clicked.connect(partial(self.actualizar_cliente, row_count))
        btn_eliminar.clicked.connect(partial(self.eliminar_cliente, row_count))

        # Agregar los botones a la fila en las columnas respectivas
        self.parent.tbl_Cliente.setCellWidget(row_count, len(cliente), btn_actualizar)
        self.parent.tbl_Cliente.setCellWidget(row_count, len(cliente) + 1, btn_eliminar)

    def actualizar_cliente(self, row):
        item = self.parent.tbl_Cliente.item(row, 0)
        if item is not None:
            valor = item.text()
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Cliente no encontrado", "Actualiza la pagina")

    def eliminar_cliente(self, row):
        item = self.parent.tbl_Cliente.item(row, 0)
        if item is not None:
            valor = item.text()
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Cliente no encontrado", "Actualiza la pagina")
