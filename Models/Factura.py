from datetime import datetime

class Factura:
    id: int = 0
    fecha: datetime = None
    total: int = 0
    idreserva: int = 0
    idmetodopago: int = 0
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetFecha(self) -> datetime:
        return self.fecha
    def SetFecha(self, value: datetime) -> None:
        self.fecha = value
    
    def GetTotal(self) -> int:
        return self.total
    def SetTotal(self, value: int) -> None:
        self.total = value
    
    def GetIdReserva(self) -> int:
        return self.idreserva
    def SetIdReserva(self, value: int) -> None:
        self.idreserva = value
    
    def GetIdMetodoPago(self) -> int:
        return self.idmetodopago
    def SetIdMetodoPago(self, value: int) -> None:
        self.idmetodopago = value