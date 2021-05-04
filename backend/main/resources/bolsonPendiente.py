from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import bolsonesModel


class BolsonPendiente(Resource):
    def get(self, id):
        bolsonPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 0).get_or_404(id)
        return bolsonPendiente.to_json()
    
    def delete(self, id):
        bolsonPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 0).get_or_404(id)
        db.session.delete(bolsonPendiente)
        db.session.commit()
        return "", 204

    def put(self, id):
        bolsonPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 0).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(bolsonPendiente, key, value)
        db.session.add(bolsonPendiente)
        db.session.commit()
        return BolsonPendiente.to_json() , 201

class BolsonesPendiente(Resource):
    def get(self):
        bolsonesPendiente = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 0).all()
        return jsonify([bolsonesPendiente.to_json() for bolsonesPendiente in bolsonesPendiente])

    def post(self):
        bolsonesPendiente = bolsonesModel.from_json(request.get_json())
        db.session.add(bolsonesPendiente)
        db.session.commit()
        return bolsonesPendiente.to_json(), 201
