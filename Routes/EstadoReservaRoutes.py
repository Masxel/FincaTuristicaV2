import json
from flask import Blueprint, request, jsonify
from Models.EstadoReserva import EstadoReserva
from Repository.EstadoReservaRepository import EstadoReservaRepository

estadoreserva_bp = Blueprint('estadoreserva', __name__)

@estadoreserva_bp.route("/api/estadoreserva/", methods=["GET"])
def obtener_todos_estadoreserva():
    try:
        coleccion_datos = EstadoReservaRepository().consultar()
        
        if coleccion_datos:
            lista_estadoreserva = []
            for dato in coleccion_datos:
                estado_reserva = EstadoReserva()
                estado_reserva.SetId(dato[0])
                estado_reserva.SetDescripcion(dato[1])
                
                dict_estadoreserva = {
                    "id": estado_reserva.GetId(),
                    "descripcion": estado_reserva.GetDescripcion()
                }
                lista_estadoreserva.append(dict_estadoreserva)
            
            return jsonify({
                "estado_reservas": lista_estadoreserva,
                "cantidad_total_estado_reservas": len(lista_estadoreserva),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "cantidad_total_estado_reservas": 0,
                "status": "success"
            }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadoreserva_bp.route("/api/estadoreserva/", methods=["POST"])
def crear_estadoreserva():
    try:
        datos = request.get_json()
        nuevo_estadoreserva = EstadoReserva()
        nuevo_estadoreserva.SetDescripcion(datos.get("descripcion"))
        
        resultado = EstadoReservaRepository().insertar(nuevo_estadoreserva)
        
        if resultado > 0:
            return jsonify({
                "message": f"Estado de reserva {nuevo_estadoreserva.GetDescripcion()} creado exitosamente",
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": "Error al crear el estado de reserva",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadoreserva_bp.route("/api/estadoreserva", methods=["PUT"])
def actualizar_estadoreserva():
    try:
        datos = request.get_json()
        estadoreserva_actualizado = EstadoReserva()
        estadoreserva_actualizado.SetId(datos.get("id"))
        estadoreserva_actualizado.SetDescripcion(datos.get("descripcion"))
        
        resultado = EstadoReservaRepository().actualizar(estadoreserva_actualizado)
        
        if resultado > 0:
            return jsonify({
                "message": f"Estado de reserva ID {estadoreserva_actualizado.GetId()} actualizado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": "Error al actualizar el estado de reserva",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadoreserva_bp.route("/api/estadoreserva/<int:id>", methods=["DELETE"])
def eliminar_estadoreserva(id):
    try:
        resultado = EstadoReservaRepository().eliminar(id)
        
        if resultado > 0:
            return jsonify({
                "message": f"Estado de reserva ID {id} eliminado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": "Error al eliminar el estado de reserva",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500