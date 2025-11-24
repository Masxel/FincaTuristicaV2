import flask
from Routes.ClientesRoutes import clientes_bp
from Routes.CargoRoutes import cargo_bp
from Routes.EmpleadosRoutes import empleados_bp
from Routes.EstadoHabitacionRoutes import estadohabitacion_bp
from Routes.EstadoReservaRoutes import estadoreserva_bp
from Routes.EventosRoutes import eventos_bp
from Routes.InsumosRoutes import insumos_bp
from Routes.HabitacionRoutes import habitaciones_bp
from Routes.MenuAlimentacionRoutes import menualimentacion_bp
from Routes.MetodoPagoRoutes import metodopago_bp
from Routes.TiendaLocalRoutes import tiendalocal_bp
from Routes.ZonaEntretenimientoRoutes import zonaentretenimiento_bp
from Routes.ReservaRoutes import reservas_bp
from Routes.FacturaRoutes import facturas_bp

# Crear la aplicación Flask
app = flask.Flask(__name__)

# Registrar blueprints (rutas)
app.register_blueprint(clientes_bp)
app.register_blueprint(cargo_bp)
app.register_blueprint(empleados_bp)
app.register_blueprint(estadohabitacion_bp)
app.register_blueprint(estadoreserva_bp)
app.register_blueprint(eventos_bp)
app.register_blueprint(insumos_bp)
app.register_blueprint(habitaciones_bp)
app.register_blueprint(menualimentacion_bp)
app.register_blueprint(metodopago_bp)
app.register_blueprint(tiendalocal_bp)
app.register_blueprint(zonaentretenimiento_bp)
app.register_blueprint(reservas_bp)
app.register_blueprint(facturas_bp)

# Solo ejecutar si es el archivo principal
if __name__ == '__main__':
    print(f"Iniciando servidor Flask en http://localhost:4560")
    app.run('localhost', port=4560, debug=True)