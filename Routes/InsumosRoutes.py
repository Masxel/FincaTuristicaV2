import json
from flask import Blueprint, jsonify, request
from Models.Insumos import Insumos
from Repository.InsumosRepository import InsumosRepository
from Utils.Crypto import *


insumos_bp = Blueprint('insumos', __name__)

@insumos_bp.route('/api/insumos', methods=["GET"])
def obtener_insumos(): 
    try:
        datos_insumos = InsumosRepository().consultar()
        lista_insumos = []
        if datos_insumos:
            for dato in datos_insumos:
                insumo = Insumos()
                insumo.SetId(dato[0])
                insumo.SetNombre(dato[1])
                insumo.SetCantidad(dato[2])
                insumo.SetDescripcion(dato[3])
                insumo.SetPrecio(dato[4])

                insumo_dict = {
                    "id": insumo.GetId(),
                    "nombre": insumo.GetNombre(),
                    "cantidad": insumo.GetCantidad(),
                    "descripcion": insumo.GetDescripcion(),
                    "precio": insumo.GetPrecio()
                }

                lista_insumos.append(insumo_dict)

        return jsonify({
            "insumos": lista_insumos,
            "cantidad_total_insumos": len(lista_insumos),
            "status": "success"
        })
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@insumos_bp.route('/api/insumos/<int:id>', methods=["GET"])
def obtener_insumo_por_id(id): 
    try:
        dato = InsumosRepository().consultar_por_id(id)
        
        if dato:
            insumo = Insumos()
            insumo.SetId(dato[0])
            insumo.SetNombre(dato[1])
            insumo.SetCantidad(dato[2])
            insumo.SetDescripcion(dato[3])
            insumo.SetPrecio(dato[4])

            insumo_dict = {
                "id": insumo.GetId(),
                "nombre": insumo.GetNombre(),
                "cantidad": insumo.GetCantidad(),
                "descripcion": insumo.GetDescripcion(),
                "precio": insumo.GetPrecio()
            }

            return jsonify({
                "insumo": insumo_dict,
                "status": "success"
            })
        else:
            return jsonify({
                "message": f"Insumo con ID '{id}' no encontrado",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@insumos_bp.route('/api/insumos', methods=["POST"])
def crear_insumo():
    try:
        datosCifrados = request.get_json()

        data = decrypt_packet_aes(datosCifrados)

        #Si el dato es none, significa que hubo un error con el cifrado/datos, etc.
        if data is None:
            return jsonify({"error": "Datos cifrados inválidos."}), 400
        
        nuevo_insumo = Insumos()
        nuevo_insumo.SetNombre(data.get("nombre"))
        nuevo_insumo.SetCantidad(data.get("cantidad"))
        nuevo_insumo.SetDescripcion(data.get("descripcion"))
        nuevo_insumo.SetPrecio(float(data.get("precio")))
        insumosRepository = InsumosRepository()
        respuesta = insumosRepository.insertar(nuevo_insumo)
        if respuesta:
            return jsonify({
                "message": f"Insumo '{nuevo_insumo.GetNombre()}' creado exitosamente",
                "id": respuesta,
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": f"Error al crear insumo '{nuevo_insumo.GetNombre()}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@insumos_bp.route('/api/insumos/<int:id>', methods=["PUT"])
def actualizar_insumo(id):
    try:
        datosCifrados = request.get_json()

        data = decrypt_packet_aes(datosCifrados)

        #Si el dato es none, significa que hubo un error con el cifrado/datos, etc.
        if data is None:
            return jsonify({"error": "Datos cifrados inválidos."}), 400
        
        insumo_actualizado = Insumos()
        insumo_actualizado.SetId(id)
        insumo_actualizado.SetNombre(data.get("nombre"))
        insumo_actualizado.SetCantidad(data.get("cantidad"))
        insumo_actualizado.SetDescripcion(data.get("descripcion"))
        insumo_actualizado.SetPrecio(data.get("precio"))

        respuesta = InsumosRepository().actualizar(insumo_actualizado)
        if respuesta:
            return jsonify({
                "message": f"Insumo ID '{id}' actualizado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al actualizar insumo ID '{id}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@insumos_bp.route('/api/insumos/<int:id>', methods=["DELETE"])
def eliminar_insumo(id):
    try:
        respuesta = InsumosRepository().eliminar(id)
        if respuesta:
            return jsonify({
                "message": f"Insumo ID '{id}' eliminado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al eliminar insumo ID '{id}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
