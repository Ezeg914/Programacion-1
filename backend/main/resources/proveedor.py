from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'Fenix'},
    2: {'nombre': 'Pepe mujica'},
}


class proveedor(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404
    
    def delete(self, id):
        if int(id) in BOLSONES:
            del BOLSONES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in BOLSONES:
            proveedor = BOLSONES[int(id)]
            data = request.get_json()
            proveedor.update(data)
            return proveedor, 201
        return '', 404


class proveedores(Resource):
    def get(self):
        return BOLSONES

    def post(self):
        proveedor = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = proveedor
        return BOLSONES[id], 201