class Insumos:
    id: int = 0
    nombre: str = ""
    cantidad: int = 0
    descripcion: str = ""
    precio: float = 0.0 # Precio por unidad
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value
    
    def GetCantidad(self) -> int:
        return self.cantidad
    def SetCantidad(self, value: int) -> None:
        self.cantidad = value
    
    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
    
    def GetPrecio(self) -> float:
        return self.precio
    def SetPrecio(self, value: float) -> None:
        self.precio = value