from Models.TiendaLocal import TiendaLocal
from Repository.TiendaLocalRepository import TiendaLocalRepository

class TiendaLocalService:
    
    def InsertarProducto(self):
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidaddisponible = int(input("Ingrese la cantidad disponible: "))
        
        EntidadProducto = TiendaLocal()
        EntidadProducto.SetNombre(nombre)
        EntidadProducto.SetDescripcion(descripcion)
        EntidadProducto.SetPrecio(precio)
        EntidadProducto.SetCantidadDisponible(cantidaddisponible)

        respuesta = TiendaLocalRepository().insertar(EntidadProducto)
        if respuesta:
            print("Producto insertado correctamente.")
        else:
            print("Error al insertar producto.")

    def ActualizarProducto(self):
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        nombre = input("Ingrese el nuevo nombre del producto: ")
        descripcion = input("Ingrese la nueva descripcion del producto: ")
        precio = int(input("Ingrese el nuevo precio del producto: "))
        cantidaddisponible = int(input("Ingrese la nueva cantidad disponible: "))
        
        EntidadProducto = TiendaLocal()
        EntidadProducto.SetId(id_producto)
        EntidadProducto.SetNombre(nombre)
        EntidadProducto.SetDescripcion(descripcion)
        EntidadProducto.SetPrecio(precio)
        EntidadProducto.SetCantidadDisponible(cantidaddisponible)

        respuesta = TiendaLocalRepository().actualizar(EntidadProducto)
        if respuesta:
            print("Producto actualizado correctamente.")
        else:
            print("Error al actualizar producto o producto no encontrado.")

    def EliminarProducto(self):
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        
        respuesta = TiendaLocalRepository().eliminar(id_producto)
        if respuesta:
            print("Producto eliminado correctamente.")
        else:
            print("Error al eliminar producto o producto no encontrado.")

    def ConsultarProductos(self):
        resultados = TiendaLocalRepository().consultar()
        if resultados:
            print("\n--- PRODUCTOS DE LA TIENDA LOCAL ---")
            for producto in resultados:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Precio: ${producto[3]}, Disponible: {producto[4]}")
        else:
            print("No se encontraron productos en la tienda local.")

    def MenuTiendaLocal(self):
        while True:
            print("\n--- Menú de Tienda Local ---")
            print("1. Insertar Producto")
            print("2. Actualizar Producto")
            print("3. Eliminar Producto")
            print("4. Consultar Productos")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarProducto()
            elif opcion == '2':
                self.ActualizarProducto()
            elif opcion == '3':
                self.EliminarProducto()
            elif opcion == '4':
                self.ConsultarProductos()
            elif opcion == '5':
                print("Saliendo del menú de tienda local.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")