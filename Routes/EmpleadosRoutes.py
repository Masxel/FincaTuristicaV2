import json
from flask import Blueprint, jsonify, request
from Repository.EmpleadosRepository import EmpleadosRepository
from Models.Empleados import Empleados

empleados_bp = Blueprint('empleados', __name__)
        


@empleados_bp.route('/api/empleados', methods=["GET"])
def obtener_empleados():
    try:
        datos_cargados = EmpleadosRepository().consultar_todos_empleados()
        list_empledos = []
        
        if datos_cargados:
            for dato in datos_cargados:
                empleado = Empleados()
                empleado.SetId(dato[0])
                empleado.SetNombre(dato[1])
                empleado.SetApellido(dato[2])
                empleado.SetTelefono(dato[3])
                empleado.SetEmail(dato[4])
                if dato[6] is None:
                    empleado.SetCargo(dato[5])
                else:
                    empleado.SetCargo(dato[6])

                dict_empleados = {
                    "id": empleado.GetId(),
                    "nombre": empleado.GetNombre(),
                    "apellido": empleado.GetApellido(),
                    "telefono": empleado.GetTelefono(),
                    "email": empleado.GetEmail(),
                    "cargo": empleado.GetCargo()
                }
                list_empledos.append(dict_empleados)
                
            return jsonify({
                "empleados": list_empledos,
                "cantidad_total_empleados": len(list_empledos),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "empleados": [],
                "cantidad_total_empleados": 0,
                "status": "success"
            }), 200
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@empleados_bp.route('/api/empleados/<int:id_empleado>', methods=["GET"])
def obtener_empleado_por_id(id_empleado):
    try:
        dato_empleado = EmpleadosRepository().consultar_empleado_por_id(id_empleado)
        
        if dato_empleado:
            empleado = Empleados()
            empleado.SetId(dato_empleado[0])
            empleado.SetNombre(dato_empleado[1])
            empleado.SetApellido(dato_empleado[2])
            empleado.SetTelefono(dato_empleado[3])
            empleado.SetEmail(dato_empleado[4])
            if dato_empleado[6] is None:
                empleado.SetCargo(dato_empleado[5])
            else:
                empleado.SetCargo(dato_empleado[6])
                
            dict_empleado = {
                "id": empleado.GetId(),
                "nombre": empleado.GetNombre(),
                "apellido": empleado.GetApellido(),
                "telefono": empleado.GetTelefono(),
                "email": empleado.GetEmail(),
                "cargo": empleado.GetCargo()
            }
            
            return jsonify({
                "empleado": dict_empleado,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Empleado con ID {id_empleado} no encontrado",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@empleados_bp.route('/api/empleados', methods=["POST"])
def crear_empleado():
    try:
        datos = request.get_json()
        nuevo_empleado = Empleados()
        nuevo_empleado.SetId(datos.get("id"))
        nuevo_empleado.SetNombre(datos.get("nombre"))
        nuevo_empleado.SetApellido(datos.get("apellido"))
        nuevo_empleado.SetTelefono(datos.get("telefono"))
        nuevo_empleado.SetEmail(datos.get("email"))
        nuevo_empleado.SetCargo(datos.get("cargo"))
        
        resultado = EmpleadosRepository().insertar(nuevo_empleado)

        if resultado:
            return jsonify({
                "message": f"Empleado {nuevo_empleado.GetId()} creado exitosamente",
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": "Error al crear el empleado",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
    
@empleados_bp.route('/api/empleados', methods=["PUT"])
def actualizar_empleado():
    try:
        datos = request.get_json()
        empleado_actualizado = Empleados()
        empleado_actualizado.SetId(datos.get("id"))
        empleado_actualizado.SetNombre(datos.get("nombre"))
        empleado_actualizado.SetApellido(datos.get("apellido"))
        empleado_actualizado.SetTelefono(datos.get("telefono"))
        empleado_actualizado.SetEmail(datos.get("email"))
        empleado_actualizado.SetCargo(datos.get("cargo"))
        
        resultado = EmpleadosRepository().actualizar(empleado_actualizado)

        if resultado:
            return jsonify({
                "message": f"Empleado ID '{empleado_actualizado.GetId()}' actualizado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Error al actualizar empleado ID '{empleado_actualizado.GetId()}'",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@empleados_bp.route('/api/empleados/<int:id>', methods=["DELETE"])
def eliminar_empleado(id):
    try:
        empleado_existente = EmpleadosRepository().eliminar(id)
                
        if not empleado_existente:
            return jsonify({
                "mensaje": f"No se encontró empleado con ID {id}",
                "status": "not_found"
            }), 404

        resultado = EmpleadosRepository().eliminar(id)

        if resultado:
            return jsonify({
                "mensaje": f"Empleado con ID {id} eliminado exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"Error al eliminar empleado con ID {id}",
                "status": "error"
            }), 500
            
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500