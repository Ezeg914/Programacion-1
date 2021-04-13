from flask_restful import Resource
from flask import request
from main.models import bolsonesModel


class bolson(Resource):
    def get(self, id):
        bolson = db.session.query(bolsonesModel).get_or_404(id)
        return bolsones.to_json()
        #if int(id) in BOLSONES:
        #    return BOLSONES[int(id)]
        #return '', 404


class bolsones(Resource):
    def get(self):
        bolsones = db.session.query(bolsonesModel).all()
        return jsonify([bolsones.to_json() for bolsones in bolsones])

