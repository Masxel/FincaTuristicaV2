from flask import Blueprint, jsonify, request
from Repository.MetodoPagoRepository import MetodoPagoRepository 
from Models.MetodoPago import MetodoPago
    
metodopago_bp = Blueprint('metodopago_bp', __name__)

@metodopago_bp.route('/api/metodopago', methods=['GET'])
def obtener_lstmetodopago():
    try:
        _repository = MetodoPagoRepository()
        metodopagorepository = _repository.consultarMetodosPago()
        
        if metodopagorepository is None or metodopagorepository == []:
            return jsonify({
                "message": f"No existen métodos de pago registradas en el sistema",
                "status": "error"
        }), 404
        
        lst_MetodoPago = []
        
        for metodopagoData in metodopagorepository:
            dict_metodopago = {
                "id": metodopagoData[0],
                "descripcion": metodopagoData[1],
            }
            lst_MetodoPago.append(dict_metodopago)
                                
        return jsonify({
            "lstMetodosPago": lst_MetodoPago,
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@metodopago_bp.route('/api/metodopago/<int:id>', methods=['GET'])
def obtener_metodopago_por_id(id):
    try:
        _repository = MetodoPagoRepository()
        metodopagoData = _repository.obtenerMetodosPago_Id(id)
        
        dict_metodopago = {
            "id": metodopagoData[0],
            "descripcion": metodopagoData[1],
        }
                                
        return jsonify({
            "metodoPago": dict_metodopago,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@metodopago_bp.route('/api/metodopago', methods=['POST'])
def crear_metodopago():
    try:
        data = request.get_json()
        nuevo_metodopago = MetodoPago()
        nuevo_metodopago.SetDescripcion(data.get('descripcion'))
        
        metodopagoRepository = MetodoPagoRepository()
        resultado = metodopagoRepository.insertar(nuevo_metodopago)
        
        if resultado > 0:
            return jsonify({
                'mensaje': f'El método de pago con id {nuevo_metodopago.GetDescripcion()} fue creado exitosamente',
                'status': 'success'
            }), 201
        else:
            return jsonify({
                'mensaje': 'Error al crear el método de pago',
                'status': 'error'
            }), 500
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500