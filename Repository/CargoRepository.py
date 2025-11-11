from Repository.ConexionRepository import ConexionRepository
from Models.Cargo import Cargo

class CargoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, cargo):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            descripcion = cargo.GetDescripcion()
            
            cursor.execute("CALL proc_insertar_cargo(?)", 
                           (descripcion))
            cursor.commit()
                       
            return True
        except Exception as e:
            print(f"Error al insertar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
            conn.close()

    def actualizar(self, cargo):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_actualizar_cargo(?, ?)", 
                         (cargo.GetId(), cargo.GetDescripcion()))
            cursor.commit()
            
            return True
        except Exception as e:
            print(f"Error al actualizar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_eliminar_cargo(?)", (id))
            
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todos_cargos(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_cargos()")
            resultados = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            return resultados
        except Exception as e:
            print(f"Error al consultar cargos: {str(e)}")
            return []    