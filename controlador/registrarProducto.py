from controlador.conexion import DB_conexion
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import pymssql

class RegistrarProducto:
    def __init__(self, parent):
        self.parent = parent
        self.parent.btnRegistrarP.clicked.connect(self.registrar_producto)

    def registrar_producto(self):
        nombre = self.parent.txt_nombre.text()
        precio = self.parent.txt_precio.text()
        stock = self.parent.txt_stock.text()
        presentacion = self.parent.txt_presentacion.text()
        categoria = self.parent.cbx_categoria.currentText()

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
            query = "INSERT INTO Productos (nombre, precio, stock, presentacion, categoria) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre, precio, stock, presentacion, categoria))

            # Confirmar la transacción
            conn.commit()

            # Mostrar un mensaje de éxito
            QMessageBox.information(self.parent, "Registro Exitoso", "Producto registrado correctamente")

            # Limpiar los campos del formulario después del registro
            self.parent.txt_nombre.clear()
            self.parent.txt_precio.clear()
            self.parent.txt_stock.clear()
            self.parent.txt_presentacion.clear()
            self.parent.cbx_categoria.setCurrentIndex(0)
            # Cerrar la conexión
            conn.close()

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", "Error al registrar Producto en la base de datos: {}".format(e))