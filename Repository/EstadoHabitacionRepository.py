from Repository.ConexionRepository import ConexionRepository
from Models.EstadoHabitacion import EstadoHabitacion

class EstadoHabitacionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, estado_habitacion: EstadoHabitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
        
            descripcion = estado_habitacion.GetDescripcion()
            
            cursor.execute(
                "CALL proc_insertar_estado_habitacion(?)",
                (descripcion,)
            )
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return True 
        except Exception as e:
            print(f"Error al insertar estado de habitación: {str(e)}")
            return False
        
    
    def actualizar(self, estado_habitacion: EstadoHabitacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
        
            id_estado = estado_habitacion.GetId()
            descripcion = estado_habitacion.GetDescripcion()
            
            cursor.execute("SET @respuesta = 0")
            cursor.execute(
                "CALL proc_actualizar_estado_habitacion(?, ?, @respuesta)",
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
            print(f"Error al actualizar estado de habitación: {str(e)}")
            return 0
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
        
            cursor.execute("SET @respuesta = 0")
            cursor.execute(
                "CALL proc_eliminar_estado_habitacion(?, @respuesta)",
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
            print(f"Error al eliminar estado de habitación: {str(e)}")
            return 0
    
    def consultar(self, id=None):
        try:
         conn = self.conexion.conectar_base_datos()
         cursor = conn.cursor()
        
         if id is None:
             cursor.execute("CALL proc_consultar_estados_habitacion()")
         else:
             cursor.execute("CALL proc_consultar_estadohabitacion_por_id(?)", (id,))
         
         resultados = cursor.fetchall()
            
         cursor.close()
         conn.close()
         return resultados
        except Exception as e:
            print(f"Error al consultar estado de habitación: {str(e)}")
            return []
        