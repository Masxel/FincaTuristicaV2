from Repository.ConexionRepository import ConexionRepository
from Models.Factura import Factura

class FacturaRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, factura: Factura):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            fecha = factura.GetFecha()
            total = factura.GetTotal()
            idreserva = factura.GetIdReserva()
            idmetodopago = factura.GetIdMetodoPago()
            
            cursor.execute(
                "CALL proc_insertar_factura(?, ?, ?, ?, @respuesta)",
                (fecha, total, idreserva, idmetodopago)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar factura: {e}")
            return 0
    
    def actualizar(self, factura: Factura):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_factura = factura.GetId()
            fecha = factura.GetFecha()
            total = factura.GetTotal()
            idreserva = factura.GetIdReserva()
            idmetodopago = factura.GetIdMetodoPago()
            
            cursor.execute(
                "CALL proc_actualizar_factura(?, ?, ?, ?, ?, @respuesta)",
                (id_factura, fecha, total, idreserva, idmetodopago)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
        except Exception as e:
            print(f"Error al actualizar factura: {e}")
            return 0
    
    def eliminar(self, id):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_factura(?, @respuesta)",
                (id,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
        except Exception as e:
            print(f"Error al eliminar factura: {e}")
            return 0
    
    def consultar(self, id=None):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            if id is None:
                # Consultar todas las facturas
                cursor.execute("CALL proc_consultar_todas_facturas()")
            else:
                # Consultar factura por ID
                cursor.execute("CALL proc_consultar_factura_por_id(?)", (id,))

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados
        except Exception as e:
            print(f"Error al consultar facturas: {e}")
            return []