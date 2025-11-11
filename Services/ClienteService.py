from Models.Cliente import Cliente
from Repository.ClienteRepository import ClienteRepository

class ClienteService:
    
    UltimoId: int
    
    def InsertarCliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        email = input("Ingrese el email del cliente: ")
        
        EntidadCliente = Cliente()
        EntidadCliente.SetNombre(nombre)
        EntidadCliente.SetApellido(apellido)
        EntidadCliente.SetTelefono(telefono)
        EntidadCliente.SetEmail(email)

        respuesta = ClienteRepository().insertar(EntidadCliente)
        if respuesta:
            self.UltimoId = respuesta
            print("Cliente insertado correctamente.")
        else:
            print("Error al insertar cliente.")

    def ActualizarCliente(self):
        id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        apellido = input("Ingrese el nuevo apellido del cliente: ")
        telefono = input("Ingrese el nuevo teléfono del cliente: ")
        email = input("Ingrese el nuevo email del cliente: ")
        
        EntidadCliente = Cliente()
        EntidadCliente.SetId(id_cliente)
        EntidadCliente.SetNombre(nombre)
        EntidadCliente.SetApellido(apellido)
        EntidadCliente.SetTelefono(telefono)
        EntidadCliente.SetEmail(email)

        respuesta = ClienteRepository().actualizar(EntidadCliente)
        if respuesta:
            print("Cliente actualizado correctamente.")
        else:
            print("Error al actualizar cliente o cliente no encontrado.")

    def EliminarCliente(self):
        id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
        
        respuesta = ClienteRepository().eliminar(id_cliente)
        if respuesta:
            print("Cliente eliminado correctamente.")
        else:
            print("Error al eliminar cliente o cliente no encontrado.")

    def ConsultarClientes(self):
        resultados = ClienteRepository().consultar()
        if resultados:
            print("\n--- CLIENTES REGISTRADOS ---")
            for cliente in resultados:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]} {cliente[2]}, Teléfono: {cliente[3]}, Email: {cliente[4]}")
        else:
            print("No se encontraron clientes en la base de datos.")

    def MenuClientes(self):
        while True:
            print("\n--- Menú de Clientes ---")
            print("1. Insertar Cliente")
            print("2. Actualizar Cliente")
            print("3. Eliminar Cliente")
            print("4. Consultar Clientes")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarCliente()
            elif opcion == '2':
                self.ActualizarCliente()
            elif opcion == '3':
                self.EliminarCliente()
            elif opcion == '4':
                self.ConsultarClientes()
            elif opcion == '5':
                print("Saliendo del menú de clientes.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")