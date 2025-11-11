from Repository.ConexionRepository import ConexionRepository

class ConexionService:
    
    # Metodo basico para validar la conexion a la base de datos.
    def ValidarConexion(self):
        try:
            conexion = ConexionRepository()
            conexion.conectar_base_datos()
            print("Conectado")
            conexion.cerrar_conexion(conexion)
        except:
            print("No se pudo conectar")
            
    def probarconexion(self):
        try:
            conexion = ConexionRepository()
            conn = conexion.conectar_base_datos()
            if conn:
                print("Conexión exitosa a la base de datos.")
                conexion.cerrar_conexion(conn)
            else:
                print("No se pudo conectar a la base de datos.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")