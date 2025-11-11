import pyodbc

class ConexionRepository:
    __str_conexion: str = ""
    
    def _cadena_de_conexion(self) -> None:
        self.__str_conexion = """
        Driver={MySQL ODBC 9.4 Unicode Driver};
        Server=localhost;
        Database=db_fincaturistica;
        PORT=3306;
        user=root;
        password=;"""
        
    def conectar_base_datos(self) -> pyodbc.Connection:
        self._cadena_de_conexion()
        return pyodbc.connect(self.__str_conexion)

    def cerrar_conexion(self, conexion: pyodbc.Connection) -> None:
        conexion.close()