import json
from flask import Blueprint, jsonify, request
from Repository.ReservaRepository import ReservaRepository
from Models.Reserva import Reserva
from Helper.ReservaHelper import reservaHelper

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route('/api/reservas', methods=["GET"])
def obtener_reservas():
    try:
        datos_cargados = ReservaRepository().consultar()
        lista_reservas = []
        
        if datos_cargados:
            for dato in datos_cargados:
                print(dato)
                reserva = Reserva()
                reserva.SetId(dato[0])
                reserva.SetFechaLlegada(dato[1])
                reserva.SetFechaSalida(dato[2])
                reserva.SetIdCliente(dato[3])
                reserva.SetIdHabitacion(dato[4])

                dict_reserva = {
                "id": reserva.GetId(),
                "fecha_inicio": reserva.GetFechaLlegada(),
                "fecha_fin": reserva.GetFechaSalida(),
                "cliente": dato[7],
                "habitacion": dato[8],
                "estado_reserva": dato[9],
                "evento": dato[10]
                }
                lista_reservas.append(dict_reserva)
                
            return jsonify({
                "reservas": lista_reservas,
                "cantidad_total_reservas": len(lista_reservas),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "reservas": [],
                "cantidad_total_reservas": 0,
                "status": "success"
            }), 200
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@reservas_bp.route('/api/reservas/<int:id_reserva>', methods=["GET"])
def obtener_reserva_por_id(id_reserva):
    try:
        dato_reserva = ReservaRepository().consultar_por_id(id_reserva)
        if dato_reserva:
            reserva = Reserva()
            reserva.SetId(dato_reserva[0])
            reserva.SetFechaLlegada(dato_reserva[1])
            reserva.SetFechaSalida(dato_reserva[2])

            dict_reserva = {
                "id": reserva.GetId(),
                "fecha_inicio": reserva.GetFechaLlegada(),
                "fecha_fin": reserva.GetFechaSalida(),
                "cliente": dato_reserva[7],
                "habitacion": dato_reserva[9],
                "estado_reserva": dato_reserva[11],
                "evento": dato_reserva[12]
            }
            return jsonify({
                "reserva": dict_reserva,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"La reserva con id {id_reserva} no fue encontrada",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
@reservas_bp.route('/api/reservas', methods=["POST"])
def crear_reserva():
    try:
        datos = request.get_json()
        nueva_reserva = Reserva()
        nueva_reserva.SetFechaLlegada(datos.get("fechallegada"))
        nueva_reserva.SetFechaSalida(datos.get("fechasalida"))
        nueva_reserva.SetIdCliente(datos.get("idcliente"))
        nueva_reserva.SetIdHabitacion(datos.get("idhabitacion"))
        nueva_reserva.SetEstadoReserva(1) 
        nueva_reserva.SetIdEvento(datos.get("idevento") if datos.get("idevento") else 0)
        
        if nueva_reserva.GetFechaSalida() <= nueva_reserva.GetFechaLlegada():
            return jsonify({
                "mensaje": "La fecha de salida debe ser posterior a la fecha de llegada",
                "status": "error"
            }), 400
        
        helper = reservaHelper()
        if not helper.validarReserva(nueva_reserva):
            return jsonify({
                "mensaje": helper.getMensaje(),
                "status": "error"
            }), 400

        reserva_id = ReservaRepository().insertar(nueva_reserva)
        
        if reserva_id > 0:
            return jsonify({
                "mensaje": f"Reserva creada exitosamente codigo de la reserva {reserva_id}",
                "id_reserva": reserva_id,
                "status": "success"
            }), 201
        else:
            return jsonify({
                "mensaje": "Error al crear la reserva",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500


@reservas_bp.route('/api/reservas/<int:id_reserva>', methods=["DELETE"])
def eliminar_reserva(id_reserva):
    try:
        resultado = ReservaRepository().eliminar(id_reserva)
        if resultado:
            return jsonify({
                "mensaje": f"La reserva con id {id_reserva} fue eliminada exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"La reserva con id {id_reserva} no fue encontrada",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@reservas_bp.route('/api/reservas/<int:id_reserva>', methods=["PUT"])
def actualizar_reserva(id_reserva):
    try:
        datos = request.get_json()
        reserva_actualizada = Reserva()
        reserva_actualizada.SetId(id_reserva)
        reserva_actualizada.SetFechaLlegada(datos.get("fechallegada"))
        reserva_actualizada.SetFechaSalida(datos.get("fechasalida"))
        reserva_actualizada.SetIdCliente(datos.get("idcliente"))
        reserva_actualizada.SetIdHabitacion(datos.get("idhabitacion"))
        reserva_actualizada.SetEstadoReserva(datos.get("estadoreserva"))
        reserva_actualizada.SetIdEvento(datos.get("idevento"))
        
        reserva_repository = ReservaRepository()
        
        if reserva_repository.consultar_por_id(id_reserva) is None:
            return jsonify({
                "mensaje": f"La reserva con id '{id_reserva}' no fue encontrada",
                "status": "error"
            }), 404
        
        if reserva_actualizada.GetFechaSalida() <= reserva_actualizada.GetFechaLlegada():
           return jsonify({
                "mensaje": "La fecha de salida debe ser posterior a la fecha de llegada",
                "status": "error"
            }), 400
        
        resultado = reserva_repository.actualizar(reserva_actualizada)
        if resultado:
            return jsonify({
                "mensaje": f"La reserva con id {id_reserva} fue actualizada exitosamente",
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"La reserva con id {id_reserva} no fue encontrada",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500