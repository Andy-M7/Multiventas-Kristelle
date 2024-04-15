from functools import partial
from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QAbstractItemView

conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKristelle")
class Mostrar_usuario:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btn_lista_usuario.clicked.connect(self.mostrar_todos_usuarios) # Llamar a la función para mostrar todos los usuarios al iniciar       
        self.parent.btn_Consultar_Usuario.clicked.connect(self.buscar_usuario)

    def mostrar_todos_usuarios(self):               
        # Obtener todos los usuarios
        usuarios = conexion.obtener_todos_usuarios() 
        # Mostrar todos los usuarios en la tabla
        for usuario in usuarios:
            self.mostrar_usuario_en_tabla(usuario)

    def buscar_usuario(self):       
        id_usuario = self.parent.txt_buscar_usuario.text()
        # Obtener el usuario por ID
        usuario = conexion.obtener_usuario(id_usuario)  
        if usuario:
            # Usuario encontrado
            self.mostrar_usuario_en_tabla(usuario)
        else:
            # Usuario no encontrado
            QMessageBox.warning(self.parent, "Usuario no encontrado", "ID de usuario no existe")


    def mostrar_usuario_en_tabla(self, usuario):
    # Agrega el usuario a la tabla
        row_count = self.parent.tbl_Usuario.rowCount()
        self.parent.tbl_Usuario.insertRow(row_count)
        self.parent.tbl_Usuario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for col_idx, atributo in enumerate(usuario):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_Usuario.setItem(row_count, col_idx, item)
        # Agregar botones "Actualizar" y "Eliminar" a la fila
        btn_actualizar = QPushButton("Actualizar")
        btn_eliminar = QPushButton("Eliminar")
        # Conectar los botones a sus respectivas funciones, pasando el índice de la fila como argumento
        btn_actualizar.clicked.connect(partial(self.actualizar_usuario, row_count))
        btn_eliminar.clicked.connect(partial(self.eliminar_usuario, row_count))
        # Agregar los botones a la fila en las columnas respectivas
        self.parent.tbl_Usuario.setCellWidget(row_count, len(usuario), btn_actualizar)
        self.parent.tbl_Usuario.setCellWidget(row_count, len(usuario) + 1, btn_eliminar)



    def actualizar_usuario(self, row):
        item = self.parent.tbl_Usuario.item(row, 0)
        if item is not None:
            valor = item.text()
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Usuario no encontrado", "Actualiza la pagina")

    def eliminar_usuario(self, row):
        item = self.parent.tbl_Usuario.item(row, 0)
        if item is not None:
            valor = item.text()
            Mostrar_usuario.mostrar_todos_usuarios
            print(valor)
        else:
            QMessageBox.warning(self.parent, "Usuario no encontrado", "Actualiza la pagina")