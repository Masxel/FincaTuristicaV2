from datetime import datetime
import json
from flask import Blueprint, jsonify, request
from Repository.FacturaRepository import FacturaRepository
from Models.Factura import Factura
from Helper.FacturaHelper import reservaHelper

facturas_bp = Blueprint('facturas', __name__)

@facturas_bp.route('/api/facturas', methods=["GET"])
def obtener_facturas():
    try:
        datos_facturas = FacturaRepository().consultar()
        lista_facturas = []
        
        if datos_facturas:
            for dato in datos_facturas:
                factura_dict = {
                    "id": dato[0],
                    "fecha_factura": str(dato[1]),
                    "total": dato[2],
                    "fecha_llegada": str(dato[5]) if len(dato) > 5 else None,
                    "fecha_salida": str(dato[6]) if len(dato) > 6 else None,
                    "cliente_nombre": dato[7] if len(dato) > 7 else None,
                    "cliente_apellido": dato[8] if len(dato) > 8 else None,
                    "tipo_habitacion": dato[9] if len(dato) > 9 else None,
                    "precio_habitacion": dato[10] if len(dato) > 10 else None,
                    "metodo_pago": dato[11] if len(dato) > 11 else None
                }
                lista_facturas.append(factura_dict)
                
            return jsonify({
                "facturas": lista_facturas,
                "cantidad_total": len(lista_facturas),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "facturas": [],
                "cantidad_total": 0,
                "status": "success"
            }), 200
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@facturas_bp.route('/api/facturas/<int:id>', methods=["GET"])
def obtener_factura_por_id(id):
    try:
        dato_factura = FacturaRepository().consultar(id)
        
        if dato_factura:
            dato = dato_factura[0] if isinstance(dato_factura, list) else dato_factura
            
            factura_dict = {
                "id": dato[0],
                "fecha": str(dato[1]),
                "total": dato[2],
                "idreserva": dato[3],
                "idmetodopago": dato[4],
                "fecha_llegada": str(dato[5]) if len(dato) > 5 else None,
                "fecha_salida": str(dato[6]) if len(dato) > 6 else None,
                "cliente_nombre": dato[7] if len(dato) > 7 else None,
                "cliente_apellido": dato[8] if len(dato) > 8 else None,
                "tipo_habitacion": dato[9] if len(dato) > 9 else None,
                "precio_habitacion": dato[10] if len(dato) > 10 else None,
                "metodo_pago": dato[11] if len(dato) > 11 else None
            }
            
            return jsonify({
                "factura": factura_dict,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"La factura con id {id} no fue encontrada",
                "status": "error"
            }), 404
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@facturas_bp.route('/api/facturas', methods=["POST"])
def crear_factura():
    try:
        datos = request.get_json()
        nueva_factura = Factura()
        nueva_factura.SetIdReserva(datos.get("idreserva"))
        nueva_factura.SetIdMetodoPago(datos.get("idmetodopago"))
        nueva_factura.SetFecha(datetime.now()) 
        
        _reservaHelper = reservaHelper()
        total_calculado = _reservaHelper.calcular_total_reserva(nueva_factura)
        
        if total_calculado == 0:
            return jsonify({
                "mensaje": _reservaHelper.getMensaje(),
                "status": "error"
            }), 400
        
        nueva_factura.SetTotal(total_calculado)
        
        factura_id = FacturaRepository().insertar(nueva_factura)
        
        if factura_id > 0:
            return jsonify({
                "mensaje": f"Factura creada exitosamente con id {factura_id}",
                "id_factura": factura_id,
                "status": "success"
            }), 201
        else:
            return jsonify({
                "mensaje": "Error al crear la factura",
                "status": "error"
            }), 500
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
