from flask import Blueprint, jsonify, request
from Repository.ZonasEntretenimientoRepository import ZonasEntretenimientoRepository 
from Models.ZonasEntretenimiento import ZonasEntretenimiento

zonaentretenimiento_bp = Blueprint('zonaentretenimiento_bp', __name__)

@zonaentretenimiento_bp.route('/api/zonaentretenimiento', methods=['GET'])
def obtener_lstZonaEntretenimiento():
    try:
        _repository = ZonasEntretenimientoRepository()
        zonaentretenimientorepository = _repository.consultar_todas_zonas_entretenimiento()
        
        if zonaentretenimientorepository is None or zonaentretenimientorepository == []:
            return jsonify({
                "message": f"No existen zonas de entretenimiento registradas en el sistema",
                "status": "error"
        }), 404
        
        lst_ZonaEntretenimiento = []
        
        for zonaentretenimientoData in zonaentretenimientorepository:
            dict_zonaentretenimiento = {
                "id": zonaentretenimientoData[0],
                "nombre": zonaentretenimientoData[1],
                "descripcion": zonaentretenimientoData[2],
            }
            if zonaentretenimientoData[3] == 1:
                dict_zonaentretenimiento["estado"] = "Activo"
            else:
                dict_zonaentretenimiento["estado"] = "Inactivo"
            lst_ZonaEntretenimiento.append(dict_zonaentretenimiento)
                                
        return jsonify({
            "lstZonasEntretenimiento": lst_ZonaEntretenimiento,
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@zonaentretenimiento_bp.route('/api/zonaentretenimiento/<int:id>', methods=['GET'])
def obtener_zonaentretenimiento_por_id(id):
    try:
        _repository = ZonasEntretenimientoRepository()
        zonaentretenimientoData = _repository.consultar_zona_entretenimiento_por_id(id)
        
        if zonaentretenimientoData is None:
            return jsonify({
                "mensaje": f"La zona de entretenimiento con id {id} no fue encontrada",
                "status": "error"
        }), 404
        
        dict_zonaentretenimiento = {
            "id": zonaentretenimientoData[0],
            "nombre": zonaentretenimientoData[1],
            "descripcion": zonaentretenimientoData[2],
        }
        if zonaentretenimientoData[3] == 1:
            dict_zonaentretenimiento["estado"] = "Activo"
        else:
            dict_zonaentretenimiento["estado"] = "Inactivo"
                                
        return jsonify({
            "zonaEntretenimiento": dict_zonaentretenimiento,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@zonaentretenimiento_bp.route('/api/zonaentretenimiento', methods=['POST'])
def crear_zonaentretenimiento():
    try:
        data = request.get_json()
        nueva_zonaentretenimiento = ZonasEntretenimiento()
        nueva_zonaentretenimiento.SetNombre(data.get('nombre'))
        nueva_zonaentretenimiento.SetDescripcion(data.get('descripcion'))
        nueva_zonaentretenimiento.SetEstado(data.get('estado'))
        
        zonaentretenimientoRepository = ZonasEntretenimientoRepository()
        resultado = zonaentretenimientoRepository.insertar(nueva_zonaentretenimiento)
        
        if resultado:
            return jsonify({
                'mensaje': f'La zona de entretenimiento \'{nueva_zonaentretenimiento.GetNombre()}\' fue creada exitosamente',
                'status': 'success'
            }), 201
        else:
            return jsonify({
                'mensaje': 'Error al crear la zona de entretenimiento',
                'status': 'error'
            }), 500
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@zonaentretenimiento_bp.route('/api/zonaentretenimiento/<int:id>', methods=['PUT'])
def actualizar_zonaentretenimiento(id):
    try:
        data = request.get_json()
        zonaentretenimiento_actualizada = ZonasEntretenimiento()
        zonaentretenimiento_actualizada.SetId(id)
        zonaentretenimiento_actualizada.SetNombre(data.get('nombre'))
        zonaentretenimiento_actualizada.SetDescripcion(data.get('descripcion'))
        zonaentretenimiento_actualizada.SetEstado(data.get('estado'))
        
        zonaentretenimientoRepository = ZonasEntretenimientoRepository()
        resultado = zonaentretenimientoRepository.actualizar(zonaentretenimiento_actualizada)
        
        if resultado:
            return jsonify({
                'mensaje': f'La zona de entretenimiento con id {id} fue actualizada exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': f'Error al actualizar la zona de entretenimiento con id {id}',
                'status': 'error'
            }), 500
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@zonaentretenimiento_bp.route('/api/zonaentretenimiento/<int:id>', methods=['DELETE'])
def eliminar_zonaentretenimiento(id):
    try:
        zonaentretenimientoRepository = ZonasEntretenimientoRepository()
        resultado = zonaentretenimientoRepository.eliminar(id)
        
        if resultado:
            return jsonify({
                'mensaje': f'La zona de entretenimiento con id {id} fue eliminada exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': f'Error al eliminar la zona de entretenimiento con id {id}',
                'status': 'error'
            }), 500
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500