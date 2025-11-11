from Repository.ConexionRepository import ConexionRepository
from Models.Eventos import Eventos

class EventosRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, evento: Eventos):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_insertar_evento(?)", (evento.GetDescripcion(),))
            cursor.commit()
            
            cursor.close()
            conn.close()           
            return True
        except Exception as e:
            print(f"Error al insertar evento: {str(e)}")
            return False

    
    def actualizar(self, evento: Eventos):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_actualizar_eventos(?, ?, @respuesta)", 
                         (evento.GetId(), evento.GetDescripcion()))
            
            cursor.execute("SELECT @respuesta")
            
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()

            cursor.close()
            conn.close()
            return respuesta
        except Exception as e:
            print(f"Error al actualizar evento: {str(e)}")
            return 0
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_eliminar_eventos(?, @respuesta)", (id,))
            cursor.execute("SELECT @respuesta")
            
            resultado = cursor.fetchone()
            print(f"Resultado de la eliminación: {resultado}")
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()  
            cursor.close()          
            conn.close()
            return respuesta
        except Exception as e:
            print(f"Error al eliminar evento: {str(e)}")
            return 0
    
    def consultar_todos_eventos(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todos_eventos()")            
            resultados = cursor.fetchall()
            
            cursor.close()
            conn.close()
            return resultados
        except Exception as e:
            print(f"Error al consultar todos los eventos: {str(e)}")
            return []

    def consultar_evento_por_id(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_consultar_eventos_por_id(?)", (id,))
            
            resultado = cursor.fetchone()
            
            cursor.close()
            conn.close()
            return resultado    
        except Exception as e:
            print(f"Error al consultar evento por ID: {str(e)}")
            return None
        
    def consultar(self, id=None):
        if id is None:
            return self.consultar_todos_eventos()
        else:
            return self.consultar_evento_por_id(id)