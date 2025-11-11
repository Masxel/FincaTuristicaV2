class TiendaLocal:
    id: int = 0
    nombre: str = ""
    descripcion: str = ""
    precio: int = 0
    cantidaddisponible: int = 0
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value
    
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
    
    def GetPrecio(self) -> int:
        return self.precio
    def SetPrecio(self, value: int) -> None:
        self.precio = value
    
    def GetCantidadDisponible(self) -> int:
        return self.cantidaddisponible
    def SetCantidadDisponible(self, value: int) -> None:
        self.cantidaddisponible = value