from Repository.ConexionRepository import ConexionRepository
from Models.ZonasEntretenimiento import ZonasEntretenimiento

class ZonasEntretenimientoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, zona: ZonasEntretenimiento):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_insertar_zona_entretenimiento(?, ?, ?)", 
                         (zona.GetNombre(), 
                          zona.GetDescripcion(),
                          zona.GetEstado()))
            cursor.commit()
            
            cursor.close()
            conn.close()
            
            return True
        except Exception as e:
            print(f"Error al insertar zona de entretenimiento: {str(e)}")
            return False
    
    def actualizar(self, zona: ZonasEntretenimiento):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_actualizar_zona_entretenimiento(?, ?, ?, ?)", 
                         (zona.GetId(),
                          zona.GetNombre(), 
                          zona.GetDescripcion(),
                          zona.GetEstado()))
            conn.commit()
            
            cursor.close()
            conn.close()
            
            return True
        except Exception as e:
            print(f"Error al actualizar zona de entretenimiento: {str(e)}")
            return False
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_eliminar_zona_entretenimiento(?)", (id,))
            conn.commit()
            
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al eliminar zona de entretenimiento: {str(e)}")
            return False
    
    def consultar_todas_zonas_entretenimiento(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_consultar_zonas_entretenimiento()")
            resultados = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            return resultados
        except Exception as e:
            print(f"Error al consultar zonas de entretenimiento: {str(e)}")
            return []
        
    def consultar_zona_entretenimiento_por_id(self, id):
        try:
            print("Antes de conectar a la base de datos")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida")
            cursor = conn.cursor()
            print(f"Consultando zona de entretenimiento con ID: {id}")
            print("Ejecutando el procedimiento almacenado")
            cursor.execute("CALL proc_consultar_zonas_entretenimiento_por_id(?)", (id,))
            print("Procedimiento almacenado ejecutado")
            resultado = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            return resultado
        except Exception as e:
            print(f"Error al consultar zona de entretenimiento por ID: {str(e)}")
            return None