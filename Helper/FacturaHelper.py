from datetime import datetime, date
from Models.Reserva import Reserva
from Models.Factura import Factura
from Repository.ReservaRepository import ReservaRepository
from Repository.ClienteRepository import ClienteRepository
from Repository.HabitacionRepository import HabitacionRepository
from Repository.MetodoPagoRepository import MetodoPagoRepository


class reservaHelper:
    Mensaje: str = ""
    
    def getMensaje(self):
        return self.Mensaje;
    
    def calcular_total_reserva(self, facturamodel: Factura) -> int:
        
        repositorioReserva = ReservaRepository()
        reservaModel = Reserva()
        reserva_datos = repositorioReserva.consultar_por_id(facturamodel.GetIdReserva())
        
        if reserva_datos is None:
            self.Mensaje = "Reserva no encontrada para calcular total."
            return 0
        fecha_llegada = reserva_datos[1]
        fecha_salida = reserva_datos[2]
        id_habitacion = reserva_datos[4]
        
        dias_reserva = self.calcular_dias_reserva(fecha_llegada, fecha_salida)
        repositorioHabitacion = HabitacionRepository()
        
        habitacion_datos = repositorioHabitacion.consultar(id_habitacion)
        if habitacion_datos is None:
            self.Mensaje = "Habitación no encontrada para calcular total."
            return 0
        
        repositorymetodoPago = MetodoPagoRepository()
        metodo_pago_datos = repositorymetodoPago.obtenerMetodosPago_Id(facturamodel.GetIdMetodoPago())
        
        if metodo_pago_datos is None:
            self.Mensaje = "Método de pago no encontrado para calcular total."
            return 0
        print(f"Estado de la reserva: {reserva_datos[9]}")
        if reserva_datos[5] == 2:
            self.Mensaje = "La reserva ya ha sido facturada."
            return 0
        
        if reserva_datos[5] == 3:
            self.Mensaje = "La reserva ha sido cancelada, no se puede facturar."
            return 0
        
        reservaModel.SetId(reserva_datos[0])
        reservaModel.SetEstadoReserva(2) # Cambia estado de factura a 'Pagada'
        reservaModel.SetFechaLlegada(reserva_datos[1])
        reservaModel.SetFechaSalida(reserva_datos[2])
        reservaModel.SetIdCliente(reserva_datos[3])
        reservaModel.SetIdHabitacion(reserva_datos[4])
        reservaModel.SetIdEvento(reserva_datos[6])
        
        resultado = repositorioReserva.actualizar(reservaModel)
        if resultado == 0:
            self.Mensaje = "Error al actualizar el estado de la reserva."
            return 0
        
        precio_habitacion = habitacion_datos[2]
        total = dias_reserva * precio_habitacion
        return total
        
    
    def calcular_dias_reserva(self, fecha_llegada: date, fecha_salida: date) -> int:
        fecha_inicio = fecha_llegada
        fecha_fin = fecha_salida
        diferencia = fecha_fin - fecha_inicio
        return diferencia.days