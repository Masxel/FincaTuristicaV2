from Repository.ConexionRepository import ConexionRepository

class ReservaRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            fechallegada = reserva.fechallegada
            fechasalida = reserva.fechasalida
            idcliente = reserva.idcliente
            idhabitacion = reserva.idhabitacion
            estadoreserva = reserva.estadoreserva
            idevento = reserva.idevento if reserva.idevento > 0 else None
            
            cursor.execute(
                "CALL proc_insertar_reserva(?, ?, ?, ?, ?, ?, @respuesta)",
                (fechallegada, fechasalida, idcliente, idhabitacion, estadoreserva, idevento)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar reserva: {e}")
            return 0
    
    def actualizar(self, reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_reserva = reserva.id
            fechallegada = reserva.fechallegada
            fechasalida = reserva.fechasalida
            idcliente = reserva.idcliente
            idhabitacion = reserva.idhabitacion
            estadoreserva = reserva.estadoreserva
            idevento = reserva.idevento if reserva.idevento > 0 else None
            
            cursor.execute(
                "CALL proc_actualizar_reserva(?, ?, ?, ?, ?, ?, ?, @respuesta)",
                (id_reserva, fechallegada, fechasalida, idcliente, idhabitacion, estadoreserva, idevento)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al actualizar reserva: {e}")
            return 0
    
    def eliminar(self, id_reserva):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_reserva(?, @respuesta)",
                (id_reserva,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al eliminar reserva: {e}")
            return 0
    
    def consultar(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todas_reservas()")

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar reservas: {e}")
            return []
    
    def consultar_clientes_disponibles(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todos_clientes()")
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            
            return resultados
            
        except Exception as e:
            print(f"Error al consultar clientes: {e}")
            return []
    
    def consultar_habitaciones_disponibles(self):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_todas_habitaciones()")
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            
            return resultados
            
        except Exception as e:
            print(f"Error al consultar habitaciones: {e}")
            return []
    
    def consultar_estados_reserva(self):
        """Consulta todos los estados de reserva disponibles"""
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_estados_reserva()")
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            
            return resultados
            
        except Exception as e:
            print(f"Error al consultar estados de reserva: {e}")
            return []
    
    def consultar_eventos_disponibles(self):
        """Consulta todos los eventos disponibles"""
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_eventos()")
            resultados = cursor.fetchall()
            cursor.close()
            conn.close()
            
            return resultados
            
        except Exception as e:
            print(f"Error al consultar eventos: {e}")
            return []