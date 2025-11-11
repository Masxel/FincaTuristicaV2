from datetime import datetime

class Reserva:
    id: int = 0
    fechallegada: datetime = None
    fechasalida: datetime = None
    idcliente: int = 0
    idhabitacion: int = 0
    estadoreserva: int = 0
    idevento: int = 0
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetFechaLlegada(self) -> datetime:
        return self.fechallegada
    def SetFechaLlegada(self, value: datetime) -> None:
        self.fechallegada = value
    
    def GetFechaSalida(self) -> datetime:
        return self.fechasalida
    def SetFechaSalida(self, value: datetime) -> None:
        self.fechasalida = value
    
    def GetIdCliente(self) -> int:
        return self.idcliente
    def SetIdCliente(self, value: int) -> None:
        self.idcliente = value
        
    def GetIdHabitacion(self) -> int:
        return self.idhabitacion
    def SetIdHabitacion(self, value: int) -> None:
        self.idhabitacion = value
        
    def GetEstadoReserva(self) -> int:
        return self.estadoreserva
    def SetEstadoReserva(self, value: int) -> None:
        self.estadoreserva = value
        
    def GetIdEvento(self) -> int:
        return self.idevento
    def SetIdEvento(self, value: int) -> None:
        self.idevento = value
