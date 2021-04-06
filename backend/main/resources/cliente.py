from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'Fenix'},
    2: {'nombre': 'Pepe mujica'},
}


class cliente(Resource):
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
            cliente = BOLSONES[int(id)]
            data = request.get_json()
            cliente.update(data)
            return cliente, 201
        return '', 404

class clientes(Resource):
    def get(self, id):
        return BOLSONES

    def post(self):
        cliente = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = cliente
        return BOLSONES[id], 201