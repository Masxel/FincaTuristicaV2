import json
from flask import Blueprint, jsonify, request
from Models.Cliente import Cliente
from Repository.ClienteRepository import ClienteRepository

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/api/clientes', methods=["PUT"])
def ActualizarCliente():
    data = request.get_json()
    try:        
        clienteConsultado = ClienteRepository().consultar_por_id(data.get("id"))
        
        if clienteConsultado:
            ClienteModel = Cliente()             
            ClienteModel.SetId(clienteConsultado[0])
            ClienteModel.SetNombre(data.get("nombre"))
            ClienteModel.SetApellido(data.get("apellido"))
            ClienteModel.SetTelefono(data.get("telefono"))
            ClienteModel.SetEmail(data.get("email"))
            
            servicio_cliente = ClienteRepository()
            respuesta = servicio_cliente.actualizar(ClienteModel)

            if respuesta > 0:
                return jsonify({
                    "mensaje": f"Cliente {data.get('id')} actualizado exitosamente",
                    "status": "success"
                }), 200
            else:
                return jsonify({
                    "mensaje": f"Error al actualizar el cliente {data.get('id')}",
                    "status": "error"
                }), 500 
        else:
            return jsonify({
                "mensaje": f"No se encontró cliente con ID {data.get('id')}",
                "status": "not_found"
            }), 404       
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes', methods=["GET"])
def obtener_clientes(): 
    try:
        datos_clientes = ClienteRepository().consultar()
        
        lista_clientes = []
        
        if datos_clientes:
            for dato in datos_clientes:
                cliente = Cliente()
                cliente.SetId(dato[0])
                cliente.SetNombre(dato[1])
                cliente.SetApellido(dato[2])
                cliente.SetTelefono(dato[3])
                cliente.SetEmail(dato[4])
                
                cliente_dict = {
                    "id": cliente.GetId(),
                    "nombre": cliente.GetNombre(),
                    "apellido": cliente.GetApellido(), 
                    "telefono": cliente.GetTelefono(),
                    "email": cliente.GetEmail()
                }
                
                lista_clientes.append(cliente_dict)
        
        return jsonify({
            "clientes": lista_clientes,
            "cantidad_total_clientes": len(lista_clientes),
            "status": "success"
        })
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes/<int:id_cliente>', methods=["GET"])
def obtener_cliente_por_id(id_cliente):
    try:
        dato_cliente = ClienteRepository().consultar_por_id(id_cliente)
        
        if dato_cliente:
            cliente = Cliente()
            cliente.SetId(dato_cliente[0])
            cliente.SetNombre(dato_cliente[1])
            cliente.SetApellido(dato_cliente[2])
            cliente.SetTelefono(dato_cliente[3])
            cliente.SetEmail(dato_cliente[4])
            
            cliente_dict = {
                "id": cliente.GetId(),
                "nombre": cliente.GetNombre(),
                "apellido": cliente.GetApellido(),
                "telefono": cliente.GetTelefono(),
                "email": cliente.GetEmail()
            }
            
            return jsonify({
                "cliente": cliente_dict,
                "status": "success"
            })
        else:
            return jsonify({
                "mensaje": f"No se encontró cliente con ID {id_cliente}",
                "status": "not_found"
            }), 404
            
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes', methods=["POST"])
def crear_cliente():   
    try:
        data = request.get_json()
        
        ClienteModel = Cliente()
        ClienteModel.SetId(data.get("id"))
        ClienteModel.SetNombre(data.get("nombre"))
        ClienteModel.SetApellido(data.get("apellido"))
        ClienteModel.SetTelefono(data.get("telefono"))
        ClienteModel.SetEmail(data.get("email"))

        servicio_cliente = ClienteRepository()
        nuevo_id = servicio_cliente.insertar(ClienteModel)

        if nuevo_id == 0:
            return jsonify({
                "mensaje": "Error al crear el cliente",
                "status": "error"
            }), 500
        else:
            return jsonify({
                "mensaje": f"Cliente {nuevo_id} creado exitosamente",
                # "data": data,
                "status": "success"
        }), 201
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes/<int:id_cliente>', methods=["DELETE"])
def eliminar_cliente(id_cliente):
    try:
        cliente_existente = ClienteRepository().consultar_por_id(id_cliente)
                
        if not cliente_existente:
            return jsonify({
                "mensaje": f"No se encontró cliente con ID {id_cliente}",
                "status": "not_found"
            }), 404

        resultado = ClienteRepository().eliminar(id_cliente)

        if resultado > 0:
            return jsonify({
                "mensaje": f"Cliente con ID {id_cliente} eliminado exitosamente",
                "id_eliminado": id_cliente,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"No se pudo eliminar el cliente con ID {id_cliente}",
                "status": "error"
            }), 500

    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500