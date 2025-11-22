from Repository.ConexionRepository import ConexionRepository
from Models.Habitacion import Habitacion

class HabitacionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, habitacion: Habitacion):
        try:
            print("Antes de conectar a la base de datos")
            conn = self.conexion.conectar_base_datos()
            print("Conexión exitosa a la base de datos")
            print("Antes de crear el cursor")
            cursor = conn.cursor()
            print("Cursor creado exitosamente")

            print("Antes de obtener los atributos de la habitación")
            tipohabitacion = habitacion.GetTipoHabitacion()
            print("Tipo de habitacion obtenido:", tipohabitacion)
            precio = habitacion.GetPrecio()
            print("Precio obtenido:", precio)
            capacidad = habitacion.GetCapacidad()
            print("Capacidad obtenida:", capacidad)
            estado = habitacion.GetEstado()
            print("Estado obtenido:", estado)
            descripcion = habitacion.GetDescripcion()
            print("Descripción obtenida:", descripcion)
            
            print("Antes de ejecutar el procedimiento almacenado")
            cursor.execute(
                "CALL proc_insertar_habitacion(?, ?, ?, ?, ?, @respuesta)",
                (tipohabitacion, precio, capacidad, estado, descripcion)
            )
            print("Procedimiento almacenado ejecutado")
            print("Antes de obtener la respuesta")
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            print("Respuesta obtenida:", resultado[0])
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar habitación: {e}")
            return 0
    
    def actualizar(self, habitacion: Habitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_habitacion = habitacion.GetId()
            tipohabitacion = habitacion.GetTipoHabitacion()
            precio = habitacion.GetPrecio()
            capacidad = habitacion.GetCapacidad()
            estado = habitacion.GetEstado()
            descripcion = habitacion.GetDescripcion()
            
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
    
    def consultar(self, id: str):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_habitacion_por_id(?)", (id))

            resultados = cursor.fetchone()
            print("Resultados obtenidos:", resultados)
            
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar habitaciones: {e}")
            return []
    
    def consultar_lista_habitaciones(self):
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