from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import pymssql

class RegistrarUsuario:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnRegistrarU.clicked.connect(self.registrar_usuario)

    def registrar_usuario(self):
        idEmpleado = self.parent.txt_idEmpleado.text()
        username = self.parent.txt_username.text()
        password = self.parent.txt_password.text()
        nivel = self.parent.txt_nivel.text()

        try:
            # Datos de conexión a la base de datos
            Servidor = "localhost"
            Usuario = "sa"
            Password = "12345"
            Base_Datos = "MinimarketKristelle"

            # Conexión a la base de datos
            conn = pymssql.connect(
                server=Servidor,
                user=Usuario,
                password=Password,
                database=Base_Datos
            )

            # Crear un cursor para ejecutar consultas SQL
            cursor = conn.cursor()

            # Consulta SQL para insertar un nuevo usuario
            query = "INSERT INTO usuario (idEmpleado, username, password, nivel) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (idEmpleado, username, password, nivel))

            # Confirmar la transacción
            conn.commit()

            # Mostrar un mensaje de éxito
            QMessageBox.information(self.parent, "Registro Exitoso", "Usuario registrado correctamente")

            # Limpiar los campos del formulario después del registro
            self.parent.txt_idEmpleado.clear()
            self.parent.txt_username.clear()
            self.parent.txt_password.clear()
            self.parent.txt_nivel.clear()

            # Cerrar la conexión
            conn.close()

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", "Error al registrar usuario en la base de datos: {}".format(e))