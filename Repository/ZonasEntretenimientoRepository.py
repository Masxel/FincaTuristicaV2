from Repository.ConexionRepository import ConexionRepository

class ZonasEntretenimientoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, zona):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_zona_entretenimiento(?, ?, ?)", 
                         (zona.get_nombre(), 
                          zona.get_descripcion(),
                          zona.get_estado()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar zona de entretenimiento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, zona):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_zona_entretenimiento(?, ?, ?, ?)", 
                         (zona.get_id(),
                          zona.get_nombre(), 
                          zona.get_descripcion(),
                          zona.get_estado()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar zona de entretenimiento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_zona_entretenimiento(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar zona de entretenimiento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todas_zonas_entretenimiento(self):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_zonas_entretenimiento()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar zonas de entretenimiento: {str(e)}")
            return []
        finally:
            cursor.close()