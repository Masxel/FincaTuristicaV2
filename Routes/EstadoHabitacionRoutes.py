import json
from flask import Blueprint, jsonify, request
from Models.EstadoHabitacion import EstadoHabitacion 
from Repository.EstadoHabitacionRepository import EstadoHabitacionRepository

estadohabitacion_bp = Blueprint('estadohabitacion', __name__)

@estadohabitacion_bp.route("/api/estadohabitacion/", methods=["GET"])
def obtener_todos_estadohabitacion():
    try:
        coleccion_datos = EstadoHabitacionRepository().consultar()
        
        if coleccion_datos:
            lista_estadohabitacion = []
            for dato in coleccion_datos:
                estado_habitacion = EstadoHabitacion()
                estado_habitacion.SetId(dato[0])
                estado_habitacion.SetDescripcion(dato[1])
                
                dict_estadohabitacion = {
                    "id": estado_habitacion.GetId(),
                    "descripcion": estado_habitacion.GetDescripcion()
                }
                lista_estadohabitacion.append(dict_estadohabitacion)
            
            return jsonify({
                "estado_habitaciones": lista_estadohabitacion,
                "cantidad_total_estado_habitaciones": len(lista_estadohabitacion),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "cantidad_total_estado_habitaciones": 0,
                "status": "success"
            }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadohabitacion_bp.route("/api/estadohabitacion/", methods=["POST"])
def crear_estadohabitacion():
    try:
        datos = request.get_json()
        nuevo_estadohabitacion = EstadoHabitacion()
        nuevo_estadohabitacion.descripcion = datos.get("descripcion")
        
        resultado = EstadoHabitacionRepository().insertar(nuevo_estadohabitacion)
        
        if resultado > 0:
            return jsonify({
                "message": "Estado de habitación creado exitosamente",
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": "Error al crear el estado de habitación",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadohabitacion_bp.route("/api/estadohabitacion/", methods=["PUT"])
def actualizar_estadohabitacion():
    try:
        datos = request.get_json()
        estadohabitacion_actualizado = EstadoHabitacion()
        estadohabitacion_actualizado.SetId(datos.get("id"))
        estadohabitacion_actualizado.SetDescripcion(datos.get("descripcion"))
        
        resultado = EstadoHabitacionRepository().actualizar(estadohabitacion_actualizado)
        
        if resultado > 0:
            return jsonify({
                "message": f"Estado de habitación ID '{datos.get('id')}' actualizado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al actualizar estado de habitación ID '{datos.get('id')}'",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@estadohabitacion_bp.route("/api/estadohabitacion/<int:id>", methods=["DELETE"])
def eliminar_estadohabitacion(id):
    try:
        resultado = EstadoHabitacionRepository().eliminar(id)
        
        if resultado > 0:
            return jsonify({
                "message": f"Estado de habitación ID '{id}' eliminado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al eliminar estado de habitación ID '{id}'",
                "status": "error"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500