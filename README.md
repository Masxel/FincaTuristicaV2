# FincaTuristicaV2
Nueva versión de fincaturistica con mejoras

El valor de los valores de precios pasa de entero a decimal para mayor precisión en los costos de las habitaciones.

Se crea el proceso almacenado que obtenga insumos por id para optimizar las consultas.

Se corrigen errores en la inserción de habitaciones, agregando los campos que faltaban y ajustando los nombres de los métodos para obtener los atributos de la clase Habitacion.

Se crearon el resto de procedimientos almacenados que faltaban de algunos models como: Habitacion, Insumo y Eventos

Creado la clase app.py para inicializar la aplicación Flask y registrar los blueprints de las rutas.

Creada la carpeta Routes para organizar las rutas de la aplicación para pasar de un control realizado desde consola a ser controladas por medio de API RESTfull.

Agregado el procedimiento almacenado para consultar una habitación por su id, ya que no existia y solo estaba el GET() que traia todas las habitaciones.