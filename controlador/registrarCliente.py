from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import pymssql

class RegistrarCliente:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnRegistrarC.clicked.connect(self.registrar_cliente)

    def registrar_cliente(self):
        nombre_cliente = self.parent.txt_nombre_cliente.text()
        apellidos_cliente = self.parent.txt_apellidos_cliente.text()
        telefono_cliente = self.parent.txt_telefono_cliente.text()
        email_cliente = self.parent.txt_email_cliente.text()

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
            query = "INSERT INTO cliente (nombre_cliente, apellidos_cliente, telefono_cliente, email_cliente) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre_cliente, apellidos_cliente, telefono_cliente, email_cliente))

            # Confirmar la transacción
            conn.commit()

            # Mostrar un mensaje de éxito
            QMessageBox.information(self.parent, "Registro Exitoso", "Cliente registrado correctamente")

            # Limpiar los campos del formulario después del registro
            self.parent.txt_nombre_cliente.clear()
            self.parent.txt_apellidos_cliente.clear()
            self.parent.txt_telefono_cliente.clear()
            self.parent.txt_email_cliente.clear()

            # Cerrar la conexión
            conn.close()

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", "Error al registrar cliente en la base de datos: {}".format(e))