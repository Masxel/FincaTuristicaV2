from Repository.ConexionRepository import ConexionRepository

class OpinionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, opinion):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_opinion(?, ?, ?)", 
                         (opinion.get_idcliente(), 
                          opinion.get_calificacion(),
                          opinion.get_comentario()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar opinión: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, opinion):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_opinion(?, ?, ?, ?)", 
                         (opinion.get_id(),
                          opinion.get_idcliente(), 
                          opinion.get_calificacion(),
                          opinion.get_comentario()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar opinión: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_opinion(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar opinión: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todas_opiniones(self):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_opiniones()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar opiniones: {str(e)}")
            return []
        finally:
            cursor.close()