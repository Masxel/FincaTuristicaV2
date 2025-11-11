class Habitacion:
    id: int = 0
    tipohabitacion: str = ""
    precio: int = 0
    capacidad: int = 0
    estado: int = 0
    descripcion: str = ""
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetTipoHabitacion(self) -> str:
        return self.tipohabitacion
    def SetTipoHabitacion(self, value: str) -> None:
        self.tipohabitacion = value
    
    def GetPrecio(self) -> int:
        return self.precio
    def SetPrecio(self, value: int) -> None:
        self.precio = value
    
    def GetCapacidad(self) -> int:
        return self.capacidad
    def SetCapacidad(self, value: int) -> None:
        self.capacidad = value
    
    def GetEstado(self) -> int:
        return self.estado
    def SetEstado(self, value: int) -> None:
        self.estado = value
    
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value