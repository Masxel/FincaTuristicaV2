from Repository.ConexionRepository import ConexionRepository

class ClienteRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, cliente):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            nombre = cliente.nombre
            apellido = cliente.apellido
            telefono = cliente.telefono
            email = cliente.email
            
            cursor.execute(
                "CALL proc_insertar_cliente(?, ?, ?, ?, @respuesta)",
                (nombre, apellido, telefono, email)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
            return 0
    
    def actualizar(self, cliente):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_cliente = cliente.id
            nombre = cliente.nombre
            apellido = cliente.apellido
            telefono = cliente.telefono
            email = cliente.email
            
            cursor.execute(
                "CALL proc_actualizar_cliente(?, ?, ?, ?, ?, @respuesta)",
                (id_cliente, nombre, apellido, telefono, email)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return 0
    
    def eliminar(self, id_cliente):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_cliente(?, @respuesta)",
                (id_cliente,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return 0
    
    def consultar(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todos_clientes()")

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar clientes: {e}")
            return []