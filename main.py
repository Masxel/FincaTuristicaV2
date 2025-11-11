from Repository.ConexionRepository import ConexionRepository
from Services.ConexionService import ConexionService
from Services.InsumosService import InsumosService  
from Services.HabitacionService import HabitacionService
from Services.TiendaLocalService import TiendaLocalService
from Services.ClienteService import ClienteService
from Services.ReservaService import ReservaService

def mostrar_menu():
    print("SISTEMA FINCA TURÍSTICA")
    print("1. Gestión de Clientes")
    print("2. Gestión de Habitaciones") 
    print("3. Gestión de Reservas")
    print("4. Gestión de Empleados")
    print("5. Gestión de Cargos")
    print("6. Gestión de Insumos")
    print("7. Gestión de Facturas")
    print("8. Gestión de Métodos de Pago")
    print("9. Gestión de Zonas de Entretenimiento")
    print("10. Gestión de Opiniones")
    print("11. Gestión de Menús")
    print("12. Gestión de Tienda Local")
    print("13. Probar Conexión a la Base de Datos")
    print("14. Salir")

def Inicio():
    while True:
        mostrar_menu()
        
        # Capturar la opción del usuario
        opcion = input("\nSeleccione una opción (1-14): ").strip()

        if opcion == "1":
            servicio = ClienteService()
            servicio.MenuClientes()
            pass
            
        elif opcion == "2":
            servicio = HabitacionService()
            servicio.MenuHabitaciones()
            pass
            
        elif opcion == "3":
            servicio = ReservaService()
            servicio.MenuReservas()
            pass
            
        elif opcion == "4":
            pass
            
        elif opcion == "5":
            pass

        elif opcion == "6":
            servicio = InsumosService()
            servicio.MenuInsumos()
            pass
            
        elif opcion == "7":
            pass

        elif opcion == "8":
            pass

        elif opcion == "9":
            pass

        elif opcion == "10":
            pass
        
        elif opcion == "11":
            pass

        elif opcion == "12":
            servicio = TiendaLocalService()
            servicio.MenuTiendaLocal()
            pass

        elif opcion == "13":
            servicio = ConexionService()
            servicio.probarconexion()
            pass

        elif opcion == "14":
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 14.")

        input("Presione Enter para continuar...")

# ======================= Inicio de la aplicación =======================
Inicio()