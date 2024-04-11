from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class Mostrar_usuario:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btn_Consultar_Usuario.clicked.connect(self.buscar_usuario)


    def buscar_usuario(self):
        conexion = DB_conexion(Servidor="localhost", 
                               Usuario="sa", 
                               Password="12345", 
                               Base_Datos="MinimarketKrisstelle")
        
        id_usuario = self.parent.txt_buscar_usuario.text()

        # Obtener el usuario por ID
        usuario = conexion.obtener_usuario(id_usuario)
        
        if usuario:
            # Usuario encontrado
            self.mostrar_usuario_en_tabla(usuario)
        else:
            # Usuario no encontrado
            QMessageBox.warning(self.parent, "Usuario no encontrado", "ID de usuario no existe")

        # Cerrar la conexión
        conexion.cerrar_conexion()

    def mostrar_usuario_en_tabla(self, usuario):
        # Limpia la tabla antes de agregar nuevos datos
        self.parent.tbl_Usuario.clearContents()
        self.parent.tbl_Usuario.setRowCount(0)

        # Agrega el usuario a la tabla
        row_count = self.parent.tbl_Usuario.rowCount()
        self.parent.tbl_Usuario.insertRow(row_count)

        for col_idx, atributo in enumerate(usuario):
            item = QTableWidgetItem(str(atributo))
            self.parent.tbl_Usuario.setItem(row_count, col_idx, item)


        

        