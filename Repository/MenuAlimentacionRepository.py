from Repository.ConexionRepository import ConexionRepository

class MenuAlimentacionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, menu):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_menu_alimentacion(?, ?, ?, ?)", 
                         (menu.get_dia(), 
                          menu.get_plato_principal(),
                          menu.get_acompanamiento(),
                          menu.get_postre()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar menú de alimentación: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, menu):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_menu_alimentacion(?, ?, ?, ?, ?)", 
                         (menu.get_id(),
                          menu.get_dia(), 
                          menu.get_plato_principal(),
                          menu.get_acompanamiento(),
                          menu.get_postre()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar menú de alimentación: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_menu_alimentacion(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar menú de alimentación: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todos_menus_alimentacion(self):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_menus_alimentacion()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar menús de alimentación: {str(e)}")
            return []
        finally:
            cursor.close()