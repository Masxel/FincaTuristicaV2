from flask import Blueprint, jsonify, request
from Repository.HabitacionRepository import HabitacionRepository
from Models.Habitacion import Habitacion

habitaciones_bp = Blueprint('habitaciones_bp', __name__)

@habitaciones_bp.route('/api/habitaciones/<int:id>', methods=['GET'])
def obtener_habitacion(id):
    try:
        _repository = HabitacionRepository()
        habitacion = Habitacion()
        habitacionrepository = _repository.consultar(id)
        
        if habitacionrepository is None:
            return jsonify({
                "mensaje": f"La habitación con id {id} no fue encontrada",
                "status": "error"
        }), 404
        
        print(habitacionrepository)
        habitacion.SetId(habitacionrepository[0])
        habitacion.SetTipoHabitacion(habitacionrepository[1])
        habitacion.SetPrecio(habitacionrepository[2])
        habitacion.SetCapacidad(habitacionrepository[3])
        habitacion.SetEstado(habitacionrepository[6])
        habitacion.SetDescripcion(habitacionrepository[5])
        
        dict_habitacion = {
                "id": habitacion.GetId(),
                "tipohabitacion": habitacion.GetTipoHabitacion(),
                "precio": habitacion.GetPrecio(),
                "capacidad": habitacion.GetCapacidad(),
                "estado": habitacion.GetEstado(),
                "descripcion": habitacion.GetDescripcion()
            }
                                
        return jsonify({
            "habitaciones": dict_habitacion,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e)
            }), 500
        
@habitaciones_bp.route('/api/habitaciones', methods=['GET'])
def obtener_listahabitaciones():
    try:
        _repository = HabitacionRepository()
        habitacionesrepository = _repository.consultar_lista_habitaciones()
        lstHabitaciones = []
        if habitacionesrepository is None:
            return jsonify({
                "mensaje": "No se encontraron habitaciones",
                "status": "error"
        }), 404
        
        for habitacionData in habitacionesrepository:
            dict_habitacion = {
                "id": habitacionData[0],
                "tipohabitacion": habitacionData[1],
                "precio": habitacionData[2],
                "capacidad": habitacionData[3],
                "estado": habitacionData[7],
                "descripcion": habitacionData[5]
            }
            lstHabitaciones.append(dict_habitacion)
                                
        return jsonify({
            "habitaciones": lstHabitaciones,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e)
            }), 500
        
@habitaciones_bp.route('/api/habitaciones', methods=['POST'])
def crear_habitacion():
    try:
        data = request.get_json()
        nueva_habitacion = Habitacion()
        nueva_habitacion.SetCapacidad(data.get('capacidad'))
        nueva_habitacion.SetEstado(data.get('estado'))
        nueva_habitacion.SetDescripcion(data.get('descripcion'))
        nueva_habitacion.SetPrecio(data.get('precio'))
        nueva_habitacion.SetTipoHabitacion(data.get('tipohabitacion'))
        habitacionRepository = HabitacionRepository()
        resultado = habitacionRepository.insertar(nueva_habitacion)
        
        if resultado > 0:
            return jsonify({
                'mensaje': f'La habitación con id {resultado} fue creada exitosamente',
                'status': 'success'
            }), 201
        else:
            return jsonify({
                'mensaje': 'Error al crear la habitación',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500
        
        

@habitaciones_bp.route('/api/habitaciones/<int:id>', methods=['PUT'])
def actualizar_habitacion(id):
    try:
        data = request.get_json()
        habitacion_actualizada = Habitacion()
        habitacion_actualizada.SetId(id)
        habitacion_actualizada.SetCapacidad(data.get('capacidad'))
        habitacion_actualizada.SetEstado(data.get('estado'))
        habitacion_actualizada.SetNumero(data.get('numero'))
        habitacion_actualizada.SetPrecio(data.get('precio'))
        habitacion_actualizada.SetTipo(data.get('tipo'))
        
        resultado = HabitacionRepository().actualizar(habitacion_actualizada)
        
        if resultado > 0:
            return jsonify({
                'mensaje': 'Habitación actualizada exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al actualizar la habitación',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@habitaciones_bp.route('/api/habitaciones/<int:id>', methods=['DELETE'])
def eliminar_habitacion(id):
    try:
        resultado = HabitacionRepository().eliminar(id)
        
        if resultado > 0:
            return jsonify({
                'mensaje': 'Habitación eliminada exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al eliminar la habitación',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500