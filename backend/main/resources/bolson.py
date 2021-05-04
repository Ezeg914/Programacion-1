from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import bolsonesModel


class Bolson(Resource):
    def get(self, id):
        bolson = db.session.query(bolsonesModel).get_or_404(id)
        return bolson.to_json()


class Bolsones(Resource):
    def get(self):
        bolsones = db.session.query(bolsonesModel).all()
        return jsonify([bolsones.to_json() for bolsones in bolsones])

