from Repository.ConexionRepository import ConexionRepository

class HabitacionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, habitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            tipohabitacion = habitacion.tipohabitacion
            precio = habitacion.precio
            capacidad = habitacion.capacidad
            estado = habitacion.estado
            descripcion = habitacion.descripcion
            
            cursor.execute(
                "CALL proc_insertar_habitacion(?, ?, ?, ?, ?, @respuesta)",
                (tipohabitacion, precio, capacidad, estado, descripcion)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar habitación: {e}")
            return 0
    
    def actualizar(self, habitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_habitacion = habitacion.id
            tipohabitacion = habitacion.tipohabitacion
            precio = habitacion.precio
            capacidad = habitacion.capacidad
            estado = habitacion.estado
            descripcion = habitacion.descripcion
            
            cursor.execute(
                "CALL proc_actualizar_habitacion(?, ?, ?, ?, ?, ?, @respuesta)",
                (id_habitacion, tipohabitacion, precio, capacidad, estado, descripcion)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar habitación: {e}")
            return 0
    
    def eliminar(self, id_habitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_habitacion(?, @respuesta)",
                (id_habitacion,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar habitación: {e}")
            return 0
    
    def consultar(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todas_habitaciones()")

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar habitaciones: {e}")
            return []