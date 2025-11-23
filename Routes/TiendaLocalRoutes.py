from flask import Blueprint, jsonify, request
from Repository.TiendaLocalRepository import TiendaLocalRepository 
from Models.TiendaLocal import TiendaLocal


tiendalocal_bp = Blueprint('tiendalocal_bp', __name__)
@tiendalocal_bp.route('/api/tiendalocal', methods=['GET'])
def obtener_lstTiendalocal():
    try:
        _repository = TiendaLocalRepository()
        tiendalocalrepository = _repository.obtenerLstProductosTiendaLocal()
        
        if tiendalocalrepository is None or tiendalocalrepository == []:
            return jsonify({
                "message": f"No existen tiendas locales registradas en el sistema",
                "status": "error"
        }), 404
        
        lst_TiendaLocal = []
        
        for tiendalocalData in tiendalocalrepository:
            dict_tiendalocal = {
                "id": tiendalocalData[0],
                "nombre": tiendalocalData[1],
                "descripcion": tiendalocalData[2],
                "precio": tiendalocalData[3],
                "cantidadDisponible": tiendalocalData[4],
            }
            lst_TiendaLocal.append(dict_tiendalocal)
                                
        return jsonify({
            "lstTiendasLocales": lst_TiendaLocal,
            "status": "success"
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@tiendalocal_bp.route('/api/tiendalocal/<int:id>', methods=['GET'])
def obtener_tiendalocal_por_id(id):
    try:
        _repository = TiendaLocalRepository()
        tiendalocalData = _repository.obtenerProductoTiendaLocal_Id(id)
        
        dict_tiendalocal = {
            "id": tiendalocalData[0],
            "nombre": tiendalocalData[1],
            "descripcion": tiendalocalData[2],
            "precio": tiendalocalData[3],
            "cantidaddisponible": tiendalocalData[4],
        }
                                
        return jsonify({
            "tiendaLocal": dict_tiendalocal,
            "status": "success"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@tiendalocal_bp.route('/api/tiendalocal', methods=['POST'])
def crear_tiendalocal():
    try:
        data = request.get_json()
        tiendaLocalProductos = TiendaLocal()
        tiendaLocalProductos.SetNombre(data.get('nombre'))
        tiendaLocalProductos.SetDescripcion(data.get('descripcion'))
        tiendaLocalProductos.SetPrecio(data.get('precio'))
        tiendaLocalProductos.SetCantidadDisponible(data.get('cantidaddisponible'))
        
        _repository = TiendaLocalRepository()
        respuesta = _repository.insertar(tiendaLocalProductos)
        
        if respuesta == 0:
            return jsonify({
                "message": f"Error al crear el producto '{tiendaLocalProductos.nombre}' en la tienda local",
                "status": "error"
            }), 500
        else:
            return jsonify({
                "message": f"Producto {tiendaLocalProductos.nombre} en la tienda local fue creado exitosamente",
                "status": "success"
            }), 201
                       
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

@tiendalocal_bp.route('/api/tiendalocal/<int:id>', methods=['PUT'])
def actualizar_tiendalocal(id):
    try:
        data = request.get_json()
        tiendaLocalProductos = TiendaLocal()
        
        tiendaLocalProductos.SetId(id)
        tiendaLocalProductos.SetNombre(data.get('nombre'))
        tiendaLocalProductos.SetDescripcion(data.get('descripcion'))
        tiendaLocalProductos.SetPrecio(data.get('precio'))
        tiendaLocalProductos.SetCantidadDisponible(data.get('cantidaddisponible'))
        
        _repository = TiendaLocalRepository()
        respuesta = _repository.actualizar(tiendaLocalProductos)
        
        if respuesta == 0:
            return jsonify({
                "message": f"Error al actualizar el producto con id '{tiendaLocalProductos.GetId()}' en la tienda local",
                "status": "error"
            }), 500
        else:
            return jsonify({
                "message": f"Producto con id '{tiendaLocalProductos.id}' en la tienda local fue actualizado exitosamente",
                "status": "success"
            }), 200
                       
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
        
@tiendalocal_bp.route('/api/tiendalocal/<int:id>', methods=['DELETE'])
def eliminar_tiendalocal(id):
    try:
        _repository = TiendaLocalRepository()
        respuesta = _repository.eliminar(id)
        
        if respuesta == 0:
            return jsonify({
                "message": f"Error al eliminar el producto con id '{id}' en la tienda local",
                "status": "error"
            }), 500
        else:
            return jsonify({
                "message": f"Producto con id '{id}' en la tienda local fue eliminado exitosamente",
                "status": "success"
            }), 200
                       
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500