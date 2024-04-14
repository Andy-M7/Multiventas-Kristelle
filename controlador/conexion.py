import pymssql

class DB_conexion:
    def __init__(self, Servidor, Usuario, Password, Base_Datos):
        self.__Servidor = Servidor
        self.__Usuario = Usuario
        self.__Password = Password
        self.__Base_Datos = Base_Datos
        self.__conexion = None

    def establecer_conexion(self):
        if self.__conexion is None:
            self.__conexion = pymssql.connect(
                server   = self.__Servidor,
                user     = self.__Usuario,
                password = self.__Password,
                database = self.__Base_Datos
            )
    
    def verificar_usuario(self, usuario, contraseña):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        query  = "SELECT * FROM usuario WHERE username = %s AND password = %s"
        cursor.execute(query, (usuario, contraseña))
        result = cursor.fetchone()
        cursor.close()
        return result is not None
    
     # USUARIOS
     
    def obtener_usuario(self, id_Usuario):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        query  = "SELECT * FROM usuario WHERE idEmpleado = %s" # Aqui no se olviden cambiar la colummna del ID que tengan en la DB
        cursor.execute(query, (id_Usuario)) 
        usuario = cursor.fetchone()
        cursor.close()
        return usuario
       
    def obtener_todos_usuarios(self):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        cursor.execute("SELECT * FROM usuario")  # Aquí utilizo "usuario" en lugar de "usuarios"
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    
    # CLIENTES
         
    def obtener_cliente(self, id_Cliente):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        query  = "SELECT * FROM cliente WHERE idCliente = %s" # Aqui no se olviden cambiar la colummna del ID que tengan en la DB
        cursor.execute(query, (id_Cliente)) 
        cliente = cursor.fetchone()
        cursor.close()
        return cliente
    
    def obtener_todos_clientes(self):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        cursor.execute("SELECT * FROM cliente")  # Aquí utilizo "usuario" en lugar de "usuarios"
        clientes = cursor.fetchall()
        cursor.close()
        return clientes

    # PRODUCTOS
    
    def obtener_productos(self, id_Producto):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        # Aqui no se olviden cambiar la colummna del ID que tengan en la DB
        query  = "SELECT * FROM Productos WHERE idProducto = %s"
        cursor.execute(query, (id_Producto)) 
        producto = cursor.fetchone()
        cursor.close()
        return producto
    
    def obtener_todos_productos(self):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        cursor.execute("SELECT * FROM producto")  # Aquí utilizo "usuario" en lugar de "usuarios"
        producto = cursor.fetchall()
        cursor.close()
        return producto

    # VENTAS

    def obtener_venta(self, id_Ventas):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        # Aqui no se olviden cambiar la colummna del ID que tengan en la DB
        query  = "SELECT * FROM ventas WHERE id_ventas = %s"
        cursor.execute(query, (id_Ventas)) 
        venta = cursor.fetchone()
        cursor.close()
        return venta

    def obtener_todas_ventas(self):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        cursor.execute("SELECT * FROM ventas")  # Aquí utilizo "usuario" en lugar de "usuarios"
        print("se obtubieron las ventas Correctamente")
        venta = cursor.fetchall()
        cursor.close()
        return venta
    
    def cerrar_conexion(self):
        if self.__conexion is not None:
            self.__conexion.close()
            
    