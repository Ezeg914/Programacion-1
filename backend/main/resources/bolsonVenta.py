from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import bolsonesModel
from datetime import datetime,timedelta



class BolsonVenta(Resource):
    def get(self, id):
        bolsonVenta = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 1).filter(bolsonesModel.fecha >= (datetime.now() - timedelta(days=7))).get_or_404(id)
        return bolsonVenta.to_json()

class BolsonesVenta(Resource):
    def get(self):
        page = 1
        per_page = 10
        bolsonesVentas= db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 1).filter(bolsonesModel.fecha >= (datetime.now() - timedelta(days=7))).all()
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        bolsonesVentas = bolsonesVentas.paginate(page, per_page, True, 30)
        return jsonify({'bolsonesVentas': [bolsonVenta.to_json() for bolsonVenta in bolsonesVentas.items],
                        'total': bolsonesVentas.total,
                        'pages': bolsonesVentas.pages,
                        'page': page
                        })