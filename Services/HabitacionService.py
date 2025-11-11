from Models.Habitacion import Habitacion
from Repository.HabitacionRepository import HabitacionRepository

class HabitacionService:
    
    def mostrar_estados_disponibles(self):
        print("\n--- Estados Disponibles ---")
        print("1. Disponible")
        print("2. Ocupada")
        print("3. En mantenimiento")
    
    def InsertarHabitacion(self):
        tipohabitacion = input("Ingrese el tipo de habitación (Ej: Simple, Doble, Suite): ")
        precio = int(input("Ingrese el precio por noche: "))
        capacidad = int(input("Ingrese la capacidad (número de personas): "))
        
        self.mostrar_estados_disponibles()
        estado = int(input("Seleccione el estado (1-3): "))
        
        descripcion = input("Ingrese la descripción de la habitación: ")
        
        EntidadHabitacion = Habitacion()
        EntidadHabitacion.SetTipoHabitacion(tipohabitacion)
        EntidadHabitacion.SetPrecio(precio)
        EntidadHabitacion.SetCapacidad(capacidad)
        EntidadHabitacion.SetEstado(estado)
        EntidadHabitacion.SetDescripcion(descripcion)

        respuesta = HabitacionRepository().insertar(EntidadHabitacion)
        if respuesta:
            print("Habitación insertada correctamente.")
        else:
            print("Error al insertar habitación.")

    def ActualizarHabitacion(self):
        id_habitacion = int(input("Ingrese el ID de la habitación a actualizar: "))
        tipohabitacion = input("Ingrese el nuevo tipo de habitación: ")
        precio = int(input("Ingrese el nuevo precio por noche: "))
        capacidad = int(input("Ingrese la nueva capacidad: "))
        
        self.mostrar_estados_disponibles()
        estado = int(input("Seleccione el nuevo estado (1-3): "))
        
        descripcion = input("Ingrese la nueva descripción: ")
        
        EntidadHabitacion = Habitacion()
        EntidadHabitacion.SetId(id_habitacion)
        EntidadHabitacion.SetTipoHabitacion(tipohabitacion)
        EntidadHabitacion.SetPrecio(precio)
        EntidadHabitacion.SetCapacidad(capacidad)
        EntidadHabitacion.SetEstado(estado)
        EntidadHabitacion.SetDescripcion(descripcion)

        respuesta = HabitacionRepository().actualizar(EntidadHabitacion)
        if respuesta:
            print("Habitación actualizada correctamente.")
        else:
            print("Error al actualizar habitación o habitación no encontrada.")

    def EliminarHabitacion(self):
        id_habitacion = int(input("Ingrese el ID de la habitación a eliminar: "))
        
        respuesta = HabitacionRepository().eliminar(id_habitacion)
        if respuesta:
            print("Habitación eliminada correctamente.")
        else:
            print("Error al eliminar habitación o habitación no encontrada.")

    def ConsultarHabitaciones(self):
        resultados = HabitacionRepository().consultar()
        if resultados:
            print("\n--- HABITACIONES REGISTRADAS ---")
            for habitacion in resultados:
                print(f"ID: {habitacion[0]}")
                print(f"Tipo: {habitacion[1]}")
                print(f"Precio: ${habitacion[2]}")
                print(f"Capacidad: {habitacion[3]} personas")
                print(f"Estado: {habitacion[6]}")  # estado_descripcion del JOIN
                print(f"Descripción: {habitacion[5]}")
                print("-" * 40)
        else:
            print("No se encontraron habitaciones en la base de datos.")

    def MenuHabitaciones(self):
        while True:
            print("\n--- Menú de Habitaciones ---")
            print("1. Insertar Habitación")
            print("2. Actualizar Habitación")
            print("3. Eliminar Habitación")
            print("4. Consultar Habitaciones")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarHabitacion()
            elif opcion == '2':
                self.ActualizarHabitacion()
            elif opcion == '3':
                self.EliminarHabitacion()
            elif opcion == '4':
                self.ConsultarHabitaciones()
            elif opcion == '5':
                print("Saliendo del menú de habitaciones.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")