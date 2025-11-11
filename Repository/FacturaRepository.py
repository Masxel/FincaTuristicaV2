from Repository.ConexionRepository import ConexionRepository

class FacturaRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, factura):
        pass
    
    def actualizar(self, factura):
        pass
    
    def eliminar(self, id):
        pass
    
    def consultar(self, id=None):
        pass