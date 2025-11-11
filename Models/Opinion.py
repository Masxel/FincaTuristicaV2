class Opinion:
    id: int = 0
    idcliente: int = 0
    calificacion: int = 0
    comentario: str = ""
    
    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value
    
    def GetIdCliente(self) -> int:
        return self.idcliente
    def SetIdCliente(self, value: int) -> None:
        self.idcliente = value
    
    def GetCalificacion(self) -> int:
        return self.calificacion
    def SetCalificacion(self, value: int) -> None:
        self.calificacion = value
    
    def GetComentario(self) -> str:
        return self.comentario
    def SetComentario(self, value: str) -> None:
        self.comentario = value