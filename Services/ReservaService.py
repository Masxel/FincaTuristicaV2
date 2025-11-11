from datetime import datetime
from Models.Reserva import Reserva
from Repository.ReservaRepository import ReservaRepository
from Services.ClienteService import ClienteService

class ReservaService:
    
    CantEventos: int = 0
    CantEstados: int = 0
    
    def mostrar_clientes_disponibles(self):
        print("\n--- CLIENTES QUE YA EXISTEN ---")
        clientes = ReservaRepository().consultar_clientes_disponibles()
        if clientes:
            for cliente in clientes:
                print(f"ID: {cliente[0]} - {cliente[1]} {cliente[2]} - Tel: {cliente[3]}")
            print("0 - Registrar nuevo cliente")
        else:
            print("No hay clientes registrados.")
            print("0 - Registrar nuevo cliente")
    
    def solicitar_cliente(self):
        self.mostrar_clientes_disponibles()
        
        idcliente_input = int(input("\nIngrese el ID del cliente (o 0 para registrar nuevo): "))
        
        if idcliente_input == 0:
            cliente_service = ClienteService()
            cliente_service.InsertarCliente()
            idcliente = cliente_service.UltimoId
            return idcliente
        else:
            return idcliente_input
    
    def mostrar_habitaciones_disponibles(self):
        print("\n--- HABITACIONES DISPONIBLES ---")
        habitaciones = ReservaRepository().consultar_habitaciones_disponibles()
        if habitaciones:
            for habitacion in habitaciones:
                print(f"ID: {habitacion[0]} - Tipo: {habitacion[1]} - Precio: ${habitacion[2]} - Capacidad: {habitacion[3]} - Estado: {habitacion[6]}")
            return True
        else:
            print("No hay habitaciones registradas.")
            return False
    
    def solicitar_habitacion(self):
        if not self.mostrar_habitaciones_disponibles():
            print("No se pueden crear reservas sin habitaciones registradas.")
            print("Por favor, registre habitaciones primero desde el menú principal.")
            return None
        
        idhabitacion = int(input("\nIngrese el ID de la habitación: "))
        return idhabitacion
    
    def mostrar_estados_reserva(self):
        print("\n--- ESTADOS DE RESERVA ---")
        estados = ReservaRepository().consultar_estados_reserva()
        if estados:
            self.CantEstados = len(estados)
            for estado in estados:
                print(f"{estado[0]}. {estado[1]}")
        else:
            print("No hay estados de reserva disponibles.")
        
    
    def mostrar_eventos_disponibles(self):
        print("\n--- EVENTOS DISPONIBLES ---")
        eventos = ReservaRepository().consultar_eventos_disponibles()
        if eventos:
            self.CantEventos = len(eventos)
            for evento in eventos:
                print(f"{evento[0]}. {evento[1]}")
        else:
            print("No hay eventos disponibles.")
    
    def InsertarReserva(self):
        try:
            idcliente = self.solicitar_cliente()
            
            idhabitacion = self.solicitar_habitacion()
            if idhabitacion is None:
                return  # Cancelar si no hay habitaciones disponibles
            
            print("\nIngrese las fechas (formato: YYYY-MM-DD):")
            fechallegada_str = input("Fecha de llegada: ")
            fechasalida_str = input("Fecha de salida: ")
            
            fechallegada = datetime.strptime(fechallegada_str, "%Y-%m-%d").date()
            fechasalida = datetime.strptime(fechasalida_str, "%Y-%m-%d").date()
            
            if fechallegada >= fechasalida:
                print("Error: La fecha de llegada debe ser anterior a la fecha de salida.")
                return
            
            self.mostrar_estados_reserva()
            estadoreserva = int(input(f"Seleccione el estado de la reserva (1-{self.CantEstados}): "))
            
            self.mostrar_eventos_disponibles()
            idevento = int(input(f"Seleccione el evento (0-{self.CantEventos}): "))
            
            EntidadReserva = Reserva()
            EntidadReserva.SetFechaLlegada(fechallegada)
            EntidadReserva.SetFechaSalida(fechasalida)
            EntidadReserva.SetIdCliente(idcliente)
            EntidadReserva.SetIdHabitacion(idhabitacion)
            EntidadReserva.SetEstadoReserva(estadoreserva)
            EntidadReserva.SetIdEvento(idevento)

            respuesta = ReservaRepository().insertar(EntidadReserva)
            if respuesta:
                print("Reserva insertada correctamente.")
            else:
                print("Error al insertar reserva.")
        except Exception as e:
            print(f"Error al insertar reserva: {e}")

    def ActualizarReserva(self):
        try:
            print("\n--- RESERVAS EXISTENTES ---")
            self.ConsultarReservas()
            
            id_reserva = int(input("\nIngrese el ID de la reserva a actualizar: "))
            
            idcliente = self.solicitar_cliente()
            
            idhabitacion = self.solicitar_habitacion()
            if idhabitacion is None:
                return  # Cancelar si no hay habitaciones disponibles
            
            print("\nIngrese las nuevas fechas (formato: YYYY-MM-DD):")
            fechallegada_str = input("Nueva fecha de llegada: ")
            fechasalida_str = input("Nueva fecha de salida: ")
            
            fechallegada = datetime.strptime(fechallegada_str, "%Y-%m-%d").date()
            fechasalida = datetime.strptime(fechasalida_str, "%Y-%m-%d").date()
            
            if fechallegada >= fechasalida:
                print("Error: La fecha de llegada debe ser anterior a la fecha de salida.")
                return
            
            self.mostrar_estados_reserva()
            estadoreserva = int(input("Seleccione el nuevo estado (1-3): "))
            
            self.mostrar_eventos_disponibles()
            idevento = int(input("Seleccione el nuevo evento (0-4): "))
            
            EntidadReserva = Reserva()
            EntidadReserva.SetId(id_reserva)
            EntidadReserva.SetFechaLlegada(fechallegada)
            EntidadReserva.SetFechaSalida(fechasalida)
            EntidadReserva.SetIdCliente(idcliente)
            EntidadReserva.SetIdHabitacion(idhabitacion)
            EntidadReserva.SetEstadoReserva(estadoreserva)
            EntidadReserva.SetIdEvento(idevento)

            respuesta = ReservaRepository().actualizar(EntidadReserva)
            if respuesta:
                print("Reserva actualizada correctamente.")
            else:
                print("Error al actualizar reserva o reserva no encontrada.")

        except Exception as e:
            print(f"Error al actualizar reserva: {e}")

    def EliminarReserva(self):
        print("\n--- RESERVAS EXISTENTES ---")
        self.ConsultarReservas()
        
        id_reserva = int(input("\nIngrese el ID de la reserva a eliminar: "))
        
        respuesta = ReservaRepository().eliminar(id_reserva)
        if respuesta:
            print("Reserva eliminada correctamente.")
        else:
            print("Error al eliminar reserva o reserva no encontrada.")

    def ConsultarReservas(self):
        resultados = ReservaRepository().consultar()
        if resultados:
            print("\n--- RESERVAS REGISTRADAS ---")
            for reserva in resultados:
                print(f"ID: {reserva[0]}")
                print(f"Cliente: {reserva[7]}")
                print(f"Habitación: {reserva[8]}")
                print(f"Llegada: {reserva[1]} | Salida: {reserva[2]}")
                print(f"Estado: {reserva[9]}")
                evento = reserva[10] if reserva[10] else "Sin evento"
                print(f"Evento: {evento}")
                print("")
        else:
            print("No se encontraron reservas en la base de datos.")

    def MenuReservas(self):
        while True:
            print("\n--- Menú de Reservas ---")
            print("1. Insertar Reserva")
            print("2. Actualizar Reserva")
            print("3. Eliminar Reserva")
            print("4. Consultar Reservas")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarReserva()
            elif opcion == '2':
                self.ActualizarReserva()
            elif opcion == '3':
                self.EliminarReserva()
            elif opcion == '4':
                self.ConsultarReservas()
            elif opcion == '5':
                print("Saliendo del menú de reservas.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")