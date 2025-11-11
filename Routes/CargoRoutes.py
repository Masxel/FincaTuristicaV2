import json
from flask import Blueprint, jsonify, request
from Models.Cargo import Cargo
from Repository.CargoRepository import CargoRepository


cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/api/cargos', methods=["GET"])
def obtener_cargos(): 
    try:
        datos_cargos = CargoRepository().consultar_todos_cargos()
        lista_cargos = []
        if datos_cargos:
            for dato in datos_cargos:
                cargo = Cargo()
                cargo.SetId(dato[0])
                cargo.SetDescripcion(dato[1])

                cargo_dict = {
                    "id": cargo.GetId(),
                    "descripcion": cargo.GetDescripcion()
                }

                lista_cargos.append(cargo_dict)

        return jsonify({
            "cargos": lista_cargos,
            "cantidad_total_cargos": len(lista_cargos),
            "status": "success"
        })
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@cargo_bp.route('/api/cargos', methods=["POST"])
def crear_cargo():
    try:
        data = request.json
        
        nuevo_cargo = Cargo()
        nuevo_cargo.SetDescripcion(data.get("descripcion"))

        if CargoRepository().insertar(nuevo_cargo):
            return jsonify({
                "message": f"Cargo '{nuevo_cargo.GetDescripcion()}' creado exitosamente",
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": f"Error al crear cargo '{nuevo_cargo.GetDescripcion()}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@cargo_bp.route('/api/cargos/<int:id>', methods=["PUT"])
def actualizar_cargo(id):
    try:
        data = request.json
        
        cargo_actualizado = Cargo()
        cargo_actualizado.SetId(id)
        cargo_actualizado.SetDescripcion(data.get("descripcion"))

        if CargoRepository().actualizar(cargo_actualizado):
            return jsonify({
                "message": f"Cargo ID '{id}' actualizado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al actualizar cargo ID '{id}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@cargo_bp.route('/api/cargos/<int:id>', methods=["DELETE"])
def eliminar_cargo(id):
    try:
        if CargoRepository().eliminar(id):
            return jsonify({
                "message": f"Cargo ID '{id}' eliminado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al eliminar cargo ID '{id}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500