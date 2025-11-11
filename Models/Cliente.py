class Cliente:
    id: int = 0
    nombre: str = ""
    apellido: str = ""
    telefono: str = ""
    email: str = ""
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value
    
    def GetApellido(self) -> str:
        return self.apellido
    def SetApellido(self, value: str) -> None:
        self.apellido = value
    
    def GetTelefono(self) -> str:
        return self.telefono
    def SetTelefono(self, value: str) -> None:
        self.telefono = value
    
    def GetEmail(self) -> str:
        return self.email
    def SetEmail(self, value: str) -> None:
        self.email = value