from Repository.ConexionRepository import ConexionRepository

class MetodoPagoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, metodo_pago):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_metodo_pago(?)", (metodo_pago.get_descripcion(),))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar método de pago: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, metodo_pago):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_metodo_pago(?, ?)", 
                         (metodo_pago.get_id(), metodo_pago.get_descripcion()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar método de pago: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_metodo_pago(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar método de pago: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_metodos_pago(self):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_metodos_pago()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar métodos de pago: {str(e)}")
            return []
        finally:
            cursor.close()