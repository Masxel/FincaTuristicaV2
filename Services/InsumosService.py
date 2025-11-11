from Models.Insumos import Insumos
from Repository.InsumosRepository import InsumosRepository

class InsumosService:
    
    def InsertarInsumo(self):
        nombre = input("Ingrese el nombre del insumo: ")
        cantidad = int(input("Ingrese la cantidad del insumo: "))
        descripcion = input("Ingrese la descripcion del insumo: ")
        precio = float(input("Ingrese el precio del insumo: "))
        
        EntidadInsumo = Insumos()
        EntidadInsumo.SetNombre(nombre)
        EntidadInsumo.SetCantidad(cantidad)
        EntidadInsumo.SetDescripcion(descripcion)
        EntidadInsumo.SetPrecio(precio)

        respuesta = InsumosRepository().insertar(EntidadInsumo)
        if respuesta:
            print("Insumo insertado correctamente.")
        else:
            print("Error al insertar insumo.")


    def ConsultarInsumos(self):
        resultados = InsumosRepository().consultar()
        if resultados: #Dice si el resultado tiene algo
            for insumo in resultados:
                print(f"ID: {insumo[0]}, Nombre: {insumo[1]}, Cantidad: {insumo[2]}, Descripción: {insumo[3]}, Precio: {insumo[4]}")
        else:
            print("No se encontraron insumos en la base de datos.")
            
    def EliminarInsumo(self):
        print("Mostraremos todos los insumos disponibles para que pueda elegir el ID a eliminar: ")
        self.ConsultarInsumos()
        print("") #Linea en blanco
        id_insumo = int(input("Ingrese el ID del insumo a eliminar: "))
        respuesta = InsumosRepository().eliminar(id_insumo)
        if respuesta != 0:
            print("Insumo eliminado correctamente.")
        else:
            print("Error al eliminar insumo.")
            
    def ActualizarInsumo(self):
        print("Mostraremos todos los insumos disponibles para que pueda elegir el ID a actualizar: ")
        self.ConsultarInsumos()
        print("") 
        id_insumo = int(input("Ingrese el ID del insumo a actualizar: "))
                
        nombre = input("Ingrese el nuevo nombre del insumo: ")
        cantidad = int(input("Ingrese la nueva cantidad del insumo: "))
        descripcion = input("Ingrese la nueva descripcion del insumo: ")
        precio = float(input("Ingrese el nuevo precio del insumo: "))
        
        EntidadInsumo = Insumos()
        EntidadInsumo.SetIdInsumo(id_insumo)
        EntidadInsumo.SetNombre(nombre)
        EntidadInsumo.SetCantidad(cantidad)
        EntidadInsumo.SetDescripcion(descripcion)
        EntidadInsumo.SetPrecio(precio)

        respuesta = InsumosRepository().actualizar(EntidadInsumo)
        if respuesta != 0:
            print("Insumo actualizado correctamente.")
        else:
            print("Error al actualizar insumo.")

    def MenuInsumos(self):
        while True:
            print("\n--- Menú de Insumos ---")
            print("1. Insertar Insumo")
            print("2. Actualizar Insumo")
            print("3. Eliminar Insumo")
            print("4. Consultar Insumo")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarInsumo()
            elif opcion == '2':
                self.ActualizarInsumo()
            elif opcion == '3':
                self.EliminarInsumo()
            elif opcion == '4':
                self.ConsultarInsumos()
            elif opcion == '5':
                print("Saliendo del menú de insumos.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")