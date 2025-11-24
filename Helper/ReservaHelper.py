from datetime import datetime, date
from Models.Reserva import Reserva
from Models.Habitacion import Habitacion
from Repository.ReservaRepository import ReservaRepository
from Repository.ClienteRepository import ClienteRepository
from Repository.HabitacionRepository import HabitacionRepository
from Repository.EventosRepository import EventosRepository

from Services.ClienteService import ClienteService


class reservaHelper:
    Mensaje: str = ""
       
    def getMensaje(self):
        return self.Mensaje;
    
    def validarReserva(self, reservamodel: Reserva):
        
        print("Validando reserva...")
        repositoryCliente = ClienteRepository()
        
        print(f"Consultando cliente con ID: {reservamodel.GetIdCliente()}")
        clienteID = repositoryCliente.consultar_por_id(reservamodel.GetIdCliente())
        
        print(f"Resultado de la consulta del cliente: {clienteID}")
        if clienteID is None:
            self.Mensaje = "Cliente no encontrado"
            return False

        repositoryHabitacion = HabitacionRepository()
        print(f"Consultando habitación con ID: {reservamodel.GetIdHabitacion()}")
        
        _habitacion = repositoryHabitacion.consultar(reservamodel.GetIdHabitacion())
        print(f"Resultado de la consulta de la habitación: {_habitacion}")
        
        if _habitacion is None:
            self.Mensaje = "Habitación no encontrada"
            return False
        
        print(f"Estado de la habitación: {_habitacion[4]}")
        if _habitacion[4] != 1:
            self.Mensaje = "Habitación no disponible"
            return False
        
        print(f"Consultando reservas para la habitación con ID: {reservamodel.GetIdHabitacion()}")
        repositoryReserva = ReservaRepository()
        
        lstHabitacionReserva = repositoryReserva.consultar_reservas_por_habitacion(
            reservamodel.GetIdHabitacion())
        print(f"Reservas encontradas para la habitación: {lstHabitacionReserva}")
        esta_disponible = True 
        
        for habitacionReserva in lstHabitacionReserva:
            fechaInicioReserva = habitacionReserva[1]
            fechaFinReserva = habitacionReserva[2]
            
            fechallegada = datetime.strptime(reservamodel.GetFechaLlegada(), "%Y-%m-%d")
            fechasalida = datetime.strptime(reservamodel.GetFechaSalida(), "%Y-%m-%d")
            
            if isinstance(fechaInicioReserva, date) and not isinstance(fechaInicioReserva, datetime):
                fechaInicioReserva = datetime.combine(fechaInicioReserva, datetime.min.time())
            if isinstance(fechaFinReserva, date) and not isinstance(fechaFinReserva, datetime):
                fechaFinReserva = datetime.combine(fechaFinReserva, datetime.min.time())
                        
            if (fechallegada < fechaFinReserva and
                fechasalida > fechaInicioReserva):
                esta_disponible = False 
                break
        
        if not esta_disponible:
            self.Mensaje = "La habitación ya está reservada para las fechas seleccionadas"
            return False
        
        if reservamodel.GetFechaSalida() <= reservamodel.GetFechaLlegada():
            self.Mensaje = "La fecha de salida debe ser posterior a la fecha de llegada"
            return False
        
        return True
