class ZonasEntretenimiento:
    id: int = 0
    nombre: str = ""
    descripcion: str = ""
    estado: int = 0
    
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
    
    def GetEstado(self) -> int:
        return self.estado
    def SetEstado(self, value: int) -> None:
        self.estado = value