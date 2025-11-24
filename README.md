# FincaTuristicaV2
Nueva versión de fincaturistica con mejoras en la estructura del proyecto y optimización de código.

El valor de los valores de precios pasa de entero a decimal para mayor precisión en los costos de las habitaciones.

Se crea el proceso almacenado que obtenga insumos por id para optimizar las consultas.

Se corrigen errores en la inserción de habitaciones, agregando los campos que faltaban y ajustando los nombres de los métodos para obtener los atributos de la clase Habitacion.

Se crearon el resto de procedimientos almacenados que faltaban de algunos models como: Habitacion, Insumo y Eventos

Creado la clase app.py para inicializar la aplicación Flask y registrar los blueprints de las rutas.

Creada la carpeta Routes para organizar las rutas de la aplicación para pasar de un control realizado desde consola a ser controladas por medio de API RESTfull.

Agregado el procedimiento almacenado para consultar una habitación por su id, ya que no existia y solo estaba el GET() que traia todas las habitaciones.

Agregado procedimiento almacenado para consultar menú de alimentación por id, ya que no existia y solo estaba el GET() que traia todos los menús.

Algunos repositorios estaban presentando errores con la conexión a base de datos, por lo que se corrigieron las llamadas a los cursores y conexiones para que funcionen correctamente.

Se corrigieron los nombres de los métodos en MetodoPagoRepository para que coincidan con los llamados en MetodoPagoRoutes.

Metodo de pago ahora tiene consulta por id implementada en el repositorio y la ruta correspondiente.

Craedo procedimiento almacenado para consultar productos de la tienda local por id, ya que no existia y solo estaba el GET() que traia todos los productos.
Se agrego consulta de los productos en la tienda local por id en el repositorio y la ruta correspondiente.

Creado procedimiento almacenado para consultar zonas de entretenimiento por id, ya que no existia y solo estaba el GET() que traia todas las zonas.
Se agrego consulta de las zonas de entretenimiento por id en el repositorio y la ruta correspondiente

Creado procedimiento almacenado para obtener todas las reservas realizadas en la finca por la habitación.

Creado procedimiento almacenado para obtener reservas por Id de reserva.

Creado FacturaModel, FacturaRepository, FacturaHelper y FacturaRoutes para gestionar la creación y consulta de facturas en la aplicación.

Se implementó la funcionalidad para crear facturas basadas en reservas existentes, incluyendo la validación del estado de la reserva y el cálculo del total a pagar según el método de pago seleccionado.