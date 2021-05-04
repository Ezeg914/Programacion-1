from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import bolsonesModel
from datetime import datetime,timedelta



class BolsonVenta(Resource):
    def get(self, id):
        bolsonPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 1).filter(olsonesModel.fecha >= (datetime.now() - timedelta(days=7))).get_or_404(id)
        return bolsonPendiente.to_json()

class BolsonesVenta(Resource):
    def get(self):
        bolsonesPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 1).filter(bolsonesModel.fecha >= (datetime.now() - timedelta(days=7))).all()
        return jsonify([bolsonesPendiente.to_json() for bolsonesPendiente in bolsonesPendiente])