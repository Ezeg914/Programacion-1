from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'Fenix'},
    2: {'nombre': 'Pepe mujica'},
}

class bolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404

class bolsonesVenta(Resource):
    def get(self):
       return BOLSONES
