from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import bolsonesModel
from datetime import datetime,timedelta


class BolsonPrevio(Resource):
    def get(self, id):

        bolsonPrevio = db.session.query(bolsonesModel).filter(bolsonesModel.fecha <= (datetime.now() - timedelta(days=7))).get_or_404(id)
        return bolsonPrevio.to_json()


class BolsonesPrevio(Resource):

    def get(self):
        bolsonesPrevio = db.session.query(bolsonesModel).filter(bolsonesModel.fecha <= (datetime.now() - timedelta(days=7))).all()
        return jsonify([bolsonesPrevio.to_json() for bolsonesPrevio in bolsonesPrevio])
