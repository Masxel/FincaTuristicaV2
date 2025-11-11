from Models import Empleados
from Repository.ConexionRepository import ConexionRepository

class EmpleadosRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, empleado):
        try:
            cursor = self.conexion.conectar_base_datos()
            cursor.execute("CALL proc_insertar_empleado(?, ?, ?, ?, ?, ?)", 
                         (empleado.GetNombre(), 
                          empleado.GetApellido(),
                          empleado.GetTelefono(),
                          empleado.GetEmail(),
                          empleado.GetCargo(),
                          empleado.GetId()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar empleado: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, empleado: Empleados):
        try:
            cursor = self.conexion.conectar_base_datos()
            cursor.execute("CALL proc_actualizar_empleado(?, ?, ?, ?, ?, ?)", 
                         (empleado.GetId(),
                          empleado.GetNombre(), 
                          empleado.GetApellido(),
                          empleado.GetTelefono(),
                          empleado.GetEmail(),
                          empleado.GetCargo()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_eliminar_empleado(?)", (id,))
            cursor.commit()
            
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todos_empleados(self):
        try:           
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_empleados()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar empleados: {str(e)}")
            return []
        finally:
            cursor.close()
    
    def consultar_empleado_por_id(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_consultar_empleado_por_id(?)", (id,))
            
            resultado = cursor.fetchone()
            return resultado
        except Exception as e:
            print(f"Error al consultar empleado por ID: {str(e)}")
            return None
        finally:
            cursor.close()
    
    def consultar(self, id=None):
        if id is None:
            return self.consultar_todos_empleados()
        else:
            return self.consultar_empleado_por_id(id)