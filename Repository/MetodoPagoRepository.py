from Repository.ConexionRepository import ConexionRepository
from Models.MetodoPago import MetodoPago

class MetodoPagoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, metodo_pago: MetodoPago):
        try:
            print("Insertando método de pago...")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            cursor = conn.cursor()
            print("Ejecutando procedimiento almacenado...")
            cursor.execute("CALL proc_insertar_metodo_pago(?)", (metodo_pago.GetDescripcion(),))
            print("Procedimiento almacenado ejecutado.")
            conn.commit()
            
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al insertar método de pago: {str(e)}")
            return False
        
    
    def actualizar(self, metodo_pago: MetodoPago):
        try:
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            cursor = conn.cursor()
            print("Ejecutando procedimiento almacenado...")
            cursor.execute("CALL proc_actualizar_metodo_pago(?, ?)", 
                         (metodo_pago.GetId(), metodo_pago.GetDescripcion()))
            conn.commit()
            print("Procedimiento almacenado ejecutado.")
            return True
        except Exception as e:
            print(f"Error al actualizar método de pago: {str(e)}")
            return False

   
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_eliminar_metodo_pago(?)", (id,))
               
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al eliminar método de pago: {str(e)}")
            return False
    
    def consultarMetodosPago(self):
        try:
            print("Consultando métodos de pago...")
            conn = self.conexion.conectar_base_datos()
            print("Conexión establecida.")
            cursor = conn.cursor()
            print("Ejecutando procedimiento almacenado...")
            cursor.execute("CALL proc_consultar_metodos_pago()")
            print("Procedimiento almacenado ejecutado.")
            resultados = cursor.fetchall()
            print(f"Resultados obtenidos: {resultados}")
           
            cursor.close()
            conn.close()
            
            return resultados
        except Exception as e:
            print(f"Error al consultar métodos de pago: {str(e)}")
            return []

    def obtenerMetodosPago_Id(self, id: str):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            cursor.execute("CALL proc_consultar_metodo_pago_Id(?)", (id,))
            resultados = cursor.fetchone()
            
            cursor.close()
            conn.close()            
            
            return resultados
        except Exception as e:
            print(f"Error al obtener lista de métodos de pago: {str(e)}")
            return []
        