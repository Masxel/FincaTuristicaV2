from Repository.ConexionRepository import ConexionRepository
from Models.Reserva import Reserva

class ReservaRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, reserva: Reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute(
                "CALL proc_insertar_reserva(?, ?, ?, ?, ?, ?, @respuesta)",
                (reserva.GetFechaLlegada(), reserva.GetFechaSalida(), reserva.GetIdCliente(), 
                 reserva.GetIdHabitacion(), reserva.GetEstadoReserva(), reserva.GetIdEvento())
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar reserva: {e}")
            return 0
    
    def actualizar(self, reserva: Reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute(
                "CALL proc_actualizar_reserva(?, ?, ?, ?, ?, ?, ?, @respuesta)",
                (reserva.GetId(), reserva.GetFechaLlegada(), reserva.GetFechaSalida(), 
                 reserva.GetIdCliente(), reserva.GetIdHabitacion(), reserva.GetEstadoReserva(), reserva.GetIdEvento())
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar reserva: {e}")
            return 0
    
    def eliminar(self, id_reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_reserva(?, @respuesta)",
                (id_reserva,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar reserva: {e}")
            return 0
    
    def consultar(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todas_reservas()")

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar reservas: {e}")
            return []
    
    def consultar_por_id(self, id_reserva):
        try:
            print("Consultando reserva por ID:", id_reserva)
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            cursor = conn.cursor()
            print("Cursor creado.")
            cursor.execute("CALL proc_consultar_reserva_por_id(?)", (id_reserva,))
            print("Procedimiento almacenado ejecutado.")
            resultado = cursor.fetchone()
            print("Resultado obtenido:", resultado)
            
            cursor.close()
            conn.close()

            return resultado

        except Exception as e:
            print(f"Error al consultar reserva por ID: {e}")
            return None
        
    def consultar_reservas_por_habitacion(self, id_habitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_reservas_por_habitacion(?)", (id_habitacion,))

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar reservas por habitación: {e}")
            return []