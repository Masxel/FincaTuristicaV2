from Repository.ConexionRepository import ConexionRepository

class InsumosRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, insumo):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            nombre = insumo.nombre
            cantidad = insumo.cantidad
            descripcion = insumo.descripcion
            precio = insumo.precio
            
            cursor.execute(
                "CALL proc_insertar_insumos(?, ?, ?, ?, @respuesta)",
                (nombre, cantidad, descripcion, precio)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar insumo: {e}")
            return 0
    
    def actualizar(self, insumo):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            id_insumo = insumo.id
            nombre = insumo.nombre
            cantidad = insumo.cantidad
            descripcion = insumo.descripcion
            precio = insumo.precio
            
            cursor.execute(
                "CALL proc_actualizar_insumo(?, ?, ?, ?, ?, @respuesta)",
                (id_insumo, nombre, cantidad, descripcion, precio)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
        except Exception as e:
            print(f"Error al actualizar insumo: {e}")
            return 0
    
    def eliminar(self, idInsumo):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()

            cursor.execute(
                "CALL proc_eliminar_insumo(?, @respuesta)",
                (idInsumo,)
            )
            
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
        except Exception as e:
            print(f"Error al eliminar insumo: {e}")
            return 0
    
    def consultar(self, id=None):
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            if id is None:
                # Consultar todos los insumos
                cursor.execute("CALL proc_consultar_todos_insumos()")
            else:
                # Consultar insumo por ID
                cursor.execute("CALL proc_consultar_insumo_por_id(?)", (id,))

            resultados = cursor.fetchall()
            cursor.close()
            conn.close()

            return resultados

        except Exception as e:
            print(f"Error al consultar insumos: {e}")
            return []
    
    def consultar_por_id(self, id):
        """Consulta un insumo específico por su ID"""
        try:
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            cursor.execute("CALL proc_consultar_insumo_por_id(?)", (id,))

            resultado = cursor.fetchone()
            cursor.close()
            conn.close()

            return resultado

        except Exception as e:
            print(f"Error al consultar insumo por ID: {e}")
            return None