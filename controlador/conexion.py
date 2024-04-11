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
    
    def obtener_usuario(self, id_Usuario):
        self.establecer_conexion()
        cursor = self.__conexion.cursor()
        # Aqui no se olviden cambiar la colummna del ID que tengan en la DB
        query  = "SELECT * FROM usuario WHERE idEmpleado = %s"
        cursor.execute(query, (id_Usuario)) 
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

    def cerrar_conexion(self):
        if self.__conexion is not None:
            self.__conexion.close()