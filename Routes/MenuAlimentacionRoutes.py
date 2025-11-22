from flask import Blueprint, jsonify, request
from Repository.MenuAlimentacionRepository import MenuAlimentacionRepository 
from Models.MenuAlimentacion import MenuAlimentacion

menualimentacion_bp = Blueprint('menualimentacion_bp', __name__)

@menualimentacion_bp.route('/api/menualimentacion', methods=['GET'])
def obtener_menualimentacion():
    try:
        _repository = MenuAlimentacionRepository()
        menualimentacionrepository = _repository.consultar_lstMenuAlimentacion()
        
        if menualimentacionrepository is None or menualimentacionrepository == []:
            
            return jsonify({
                "message": f"No existen menús de alimentación registradas en el sistema",
                "status": "error"
        }), 404
        
        lst_MenuAlimentacion = []
        
        for menualimentacionData in menualimentacionrepository:
            dict_menualimentacion = {
                "id": menualimentacionData[0],
                "dia": menualimentacionData[1],
                "platoprincipal": menualimentacionData[2],
                "acompanamiento": menualimentacionData[3],
                "postre": menualimentacionData[4]
            }
            lst_MenuAlimentacion.append(dict_menualimentacion)
                                
        return jsonify({
            "lstMenusAlimentacion": lst_MenuAlimentacion,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e)
            }), 500
        
@menualimentacion_bp.route('/api/menualimentacion', methods=['POST'])
def crear_menu_alimentacion():
    try:
        datos = request.get_json()
        
        menualimentacion = MenuAlimentacion()
        menualimentacion.SetDia(datos.get('dia'))
        menualimentacion.SetPlatoPrincipal(datos.get('platoprincipal'))
        menualimentacion.SetAcompanamiento(datos.get('acompanamiento'))
        menualimentacion.SetPostre(datos.get('postre'))
        
        repository = MenuAlimentacionRepository()
        resultado = repository.insertar(menualimentacion)
        
        if resultado:
            return jsonify({
                "mensaje": "Menú de alimentación creado exitosamente",
                "menu_alimentacion": {
                    "id": menualimentacion.get_id(),
                    "dia": menualimentacion.get_dia(),
                    "platoprincipal": menualimentacion.get_platoprincipal(),
                    "acompanamiento": menualimentacion.get_acompanamiento(),
                    "postre": menualimentacion.get_postre()
                }
            }), 201
        else:
            return jsonify({
                "mensaje": "Error al crear el menú de alimentación",
                "status": "error"
            }), 500
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@menualimentacion_bp.route('/api/menualimentacion/<int:id>', methods=['GET'])
def obtener_menu_alimentacion_por_id(id): 
    try:
        dato = MenuAlimentacionRepository().consultar_menu_alimentacion_por_id(id)
        
        if dato:
            menualimentacion = MenuAlimentacion()
            menualimentacion.SetId(dato[0])
            menualimentacion.SetDia(dato[1])
            menualimentacion.SetPlatoPrincipal(dato[2])
            menualimentacion.SetAcompanamiento(dato[3])
            menualimentacion.SetPostre(dato[4])

            menualimentacion_dict = {
                "id": menualimentacion.GetId(),
                "dia": menualimentacion.GetDia(),
                "platoprincipal": menualimentacion.GetPlatoPrincipal(),
                "acompanamiento": menualimentacion.GetAcompanamiento(),
                "postre": menualimentacion.GetPostre()
            }
            return jsonify({
                "menualimentacion": menualimentacion_dict,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": f"Menú de alimentación con ID '{id}' no encontrado",
                "status": "error"
            }), 404
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
        
@menualimentacion_bp.route('/api/menualimentacion/<int:id>', methods=['PUT'])
def actualizar_menu_alimentacion(id):
    try:
        data = request.get_json()
        menu_actualizado = MenuAlimentacion()
        menu_actualizado.SetId(id)
        menu_actualizado.SetDia(data.get('dia'))
        menu_actualizado.SetPlatoPrincipal(data.get('plato_principal'))
        menu_actualizado.SetAcompanamiento(data.get('acompanamiento'))
        menu_actualizado.SetPostre(data.get('postre'))
        
        repository = MenuAlimentacionRepository()
        resultado = repository.actualizar(menu_actualizado)
        
        if resultado:
            return jsonify({
                'mensaje': f'El menú de alimentación con id {id} fue actualizado exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al actualizar el menú de alimentación',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500
        
@menualimentacion_bp.route('/api/menualimentacion/<int:id>', methods=['DELETE'])
def eliminar_menu_alimentacion(id):
    try:
        repository = MenuAlimentacionRepository()
        resultado = repository.eliminar(id)
        
        if resultado:
            return jsonify({
                'mensaje': f'El menú de alimentación con id {id} fue eliminado exitosamente',
                'status': 'success'
            }), 200
        else:
            return jsonify({
                'mensaje': 'Error al eliminar el menú de alimentación',
                'status': 'error'
            }), 400
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500