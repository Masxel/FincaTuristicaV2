from Repository.ConexionRepository import ConexionRepository
from Models.MenuAlimentacion import MenuAlimentacion

class MenuAlimentacionRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, menu: MenuAlimentacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_insertar_menu_alimentacion(?, ?, ?, ?)", 
                         (menu.GetDia(), 
                          menu.GetPlatoPrincipal(),
                          menu.GetAcompanamiento(),
                          menu.GetPostre()))
            
            conn.conexion.commit()
            miId = cursor.LastInsertId()
            cursor.close()
            conn.close()
            
            menu.SetId(miId)
            
            return True
        except Exception as e:
            print(f"Error al insertar menú de alimentación: {str(e)}")
            return False
    
    def actualizar(self, menu: MenuAlimentacion):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_actualizar_menu_alimentacion(?, ?, ?, ?, ?)", 
                         (menu.GetId(),
                          menu.GetDia(), 
                          menu.GetPlatoPrincipal(),
                          menu.GetAcompanamiento(),
                          menu.GetPostre()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar menú de alimentación: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_eliminar_menu_alimentacion(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar menú de alimentación: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_lstMenuAlimentacion(self):
        try:
            print("Consultando menús de alimentación...")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            print("Obteniendo cursor...")
            cursor = conn.cursor()
            print("Cursor obtenido.")
            print("Ejecutando procedimiento almacenado proc_consultar_menus_alimentacion()...")
            cursor.execute("CALL proc_consultar_menus_alimentacion()")
            print("Procedimiento ejecutado. Obteniendo resultados...")
            resultados = cursor.fetchall()
            print("Resultados obtenidos:", resultados)
            
            cursor.close()
            conn.close()  
            return resultados
        except Exception as e:
            print(f"Error al consultar menús de alimentación: {str(e)}")
            return []
        
    def consultar_menu_alimentacion_por_id(self, id):
        try:
            print(f"Consultar menu de alimentación por ID")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            print("Obteniendo cursor...")
            cursor = conn.cursor()
            print("Cursor obtenido.")
            print(f"Ejecutando procedimiento almacenado")
            cursor.execute("CALL proc_consultar_menu_alimentacion_por_id(?)", (id,))
            print("Procedimiento ejecutado. Obteniendo resultados...")
            resultado = cursor.fetchone()
            print("Resultado obtenido:", resultado)
            
            cursor.close()
            conn.close()  
            return resultado
        except Exception as e:
            print(f"Error al consultar menú de alimentación por ID: {str(e)}")
            return None