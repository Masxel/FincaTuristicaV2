from Repository.ConexionRepository import ConexionRepository
from Models.EstadoReserva import EstadoReserva

class EstadoReservaRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, estado_reserva: EstadoReserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            descripcion = estado_reserva.GetDescripcion()
            
            cursor.execute(
                "CALL proc_insertar_estadoreserva(?, @respuesta)",
                (descripcion,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar estado reserva: {e}")
            return 0
        
    
    def actualizar(self, estado_reserva: EstadoReserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_estado = estado_reserva.GetId()
            descripcion = estado_reserva.GetDescripcion()
            
            cursor.execute(
                "CALL proc_actualizar_estadoreserva(?, ?, @respuesta)",
                (id_estado, descripcion)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar estado reserva: {e}")
            return 0
    
    def eliminar(self, id: int):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_estadoreserva(?, @respuesta)",
                (id,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar estado reserva: {e}")
            return 0
    
    def consultar(self, id=None):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            if id is None:
                # Consultar todos los estados de reserva
                cursor.execute("CALL proc_consultar_todos_estadosreserva()")
                resultados = cursor.fetchall()
            else:
                # Consultar un estado específico por ID
                cursor.execute("CALL proc_consultar_estadoreserva_por_id(?)", (id,))
                resultados = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            return resultados
            
        except Exception as e:
            print(f"Error al consultar estados de reserva: {e}")
            return [] if id is None else None