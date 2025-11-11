import json
from flask import Blueprint, request, jsonify
from Models.Eventos import Eventos
from Repository.EventosRepository import EventosRepository

eventos_bp = Blueprint('eventos', __name__)


@eventos_bp.route('/api/eventos', methods=['POST'])
def crear_evento():
    try:
        
     datos = request.get_json()
         
     evento = Eventos()
     evento.SetDescripcion(datos.get('descripcion'))
    
     nuevo_evento = EventosRepository().insertar(evento)
     if nuevo_evento:
         return jsonify({
             'mensaje': f'Evento {evento.GetDescripcion()} creado exitosamente'
         }), 201
     else:
         return jsonify({
             'mensaje': f'Error al crear el evento {evento.GetDescripcion()}'
         }), 500
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@eventos_bp.route('/api/eventos', methods=['PUT'])
def actualizar_evento():
    try:
        datos = request.get_json()
        
        evento_actualizado = Eventos()
        evento_actualizado.SetId(datos.get("id"))
        evento_actualizado.SetDescripcion(datos.get("descripcion"))
        
        resultado = EventosRepository().actualizar(evento_actualizado)
        
        if resultado > 0:
            return jsonify({
                'mensaje': f'Evento ID {datos.get("id")} actualizado exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al actualizar el evento',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@eventos_bp.route('/api/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    try:
        resultado = EventosRepository().eliminar(id)
        
        if resultado > 0:
            return jsonify({
                'mensaje': f'Evento ID {id} eliminado exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al eliminar el evento',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500
        
@eventos_bp.route('/api/eventos', methods=['GET'])
def obtener_eventos():
    try:
        eventos = EventosRepository().consultar()
         
        if eventos:
         listaEventos = []
         for evento in eventos:
             evento_dict = {
                 'id': evento[0],
                 'descripcion': evento[1]
             }
             listaEventos.append(evento_dict)
        
         return jsonify({
             'eventos': listaEventos,
             'cantidad_eventos': len(listaEventos),
             'status': 'success'
         }), 200
        else:
            return jsonify({
                'message': 'No se encontraron eventos',
                'status': 'error'
            }), 404
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500