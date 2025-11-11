class MenuAlimentacion:
    id: int = 0
    dia: str = ""
    plato_principal: str = ""
    acompanamiento: str = ""
    postre: str = ""
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetDia(self) -> str:
        return self.dia
    def SetDia(self, value: str) -> None:
        self.dia = value
    
    def GetPlatoPrincipal(self) -> str:
        return self.plato_principal
    def SetPlatoPrincipal(self, value: str) -> None:
        self.plato_principal = value
    
    def GetAcompanamiento(self) -> str:
        return self.acompanamiento
    def SetAcompanamiento(self, value: str) -> None:
        self.acompanamiento = value
    
    def GetPostre(self) -> str:
        return self.postre
    def SetPostre(self, value: str) -> None:
        self.postre = value