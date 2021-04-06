from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'Fenix'},
    2: {'nombre': 'Pepe mujica'},
}


class producto(Resource):
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
            producto = BOLSONES[int(id)]
            data = request.get_json()
            producto.update(data)
            return producto, 201
        return '', 404

class productos(Resource):
    def get(self):
        return BOLSONES

    def post(self):
        producto = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = producto
        return BOLSONES[id], 201