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
        page = 1
        per_page = 10
        bolsonesPrevio = db.session.query(bolsonesModel).filter(bolsonesModel.fecha <= (datetime.now() - timedelta(days=7))).all()
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        bolsonesPrevio = bolsonesPrevio.paginate(page, per_page, True, 30)
        return jsonify({'bolsones previos': [bolsonPrevio.to_json() for bolsonPrevio in bolsonesPrevio.items],
                        'total': bolsonesPrevio.total,
                        'pages': bolsonesPrevio.pages,
                        'page': page
                        })