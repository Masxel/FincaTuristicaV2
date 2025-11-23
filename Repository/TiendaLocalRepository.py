from Repository.ConexionRepository import ConexionRepository
from Models.TiendaLocal import TiendaLocal

class TiendaLocalRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, producto: TiendaLocal):
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
    
    def actualizar(self, producto: TiendaLocal):
        try:
            print("Entrando al método actualizar")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida")
            cursor = conn.cursor()
            print("Cursor creado")

            print("Obteniendo datos del producto")
            id_producto = producto.GetId()
            nombre = producto.GetNombre()
            descripcion = producto.GetDescripcion()
            precio = producto.GetPrecio()
            cantidaddisponible = producto.GetCantidadDisponible()
            
            print(f"Antes de ejecutar el procedimiento almacenado para el producto ID: {id_producto}")
            cursor.execute(
                "CALL proc_actualizar_tienda_local(?, ?, ?, ?, ?, @respuesta)",
                (id_producto, nombre, descripcion, precio, cantidaddisponible)
            )
            print("Procedimiento almacenado ejecutado")
            print("Obteniendo la respuesta")
            cursor.execute("SELECT @respuesta")
            print("Respuesta obtenida")
            resultado = cursor.fetchone()
            print(f"Respuesta: {resultado}")
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
    
    def obtenerLstProductosTiendaLocal(self):
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
        
    def obtenerProductoTiendaLocal_Id(self, id_producto):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_tienda_local_por_id(?)", (id_producto,))
                                    
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()

            return resultado

        except Exception as e:
            print(f"Error al obtener producto por ID: {e}")
            return None