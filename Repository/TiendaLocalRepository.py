from Repository.ConexionRepository import ConexionRepository

class TiendaLocalRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, producto):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            nombre = producto.nombre
            descripcion = producto.descripcion
            precio = producto.precio
            cantidaddisponible = producto.cantidaddisponible
            
            cursor.execute(
                "CALL proc_insertar_tienda_local(?, ?, ?, ?, @respuesta)",
                (nombre, descripcion, precio, cantidaddisponible)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar producto: {e}")
            return 0
    
    def actualizar(self, producto):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_producto = producto.id
            nombre = producto.nombre
            descripcion = producto.descripcion
            precio = producto.precio
            cantidaddisponible = producto.cantidaddisponible
            
            cursor.execute(
                "CALL proc_actualizar_tienda_local(?, ?, ?, ?, ?, @respuesta)",
                (id_producto, nombre, descripcion, precio, cantidaddisponible)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return 0
    
    def eliminar(self, id_producto):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_tienda_local(?, @respuesta)",
                (id_producto,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            return 0
    
    def consultar(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todos_tienda_local()")

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar productos: {e}")
            return []