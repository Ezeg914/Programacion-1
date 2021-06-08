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
        page = 1
        per_page = 10
        bolsonesPendientes = db.session.query(bolsonesModel).filter(bolsonesModel.aprobado == 0)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        bolsonesPendientes = bolsonesPendientes.paginate(page, per_page, True, 30)
        return jsonify({'bolsones pendientes': [bolsonPendiente.to_json() for bolsonPendiente in bolsonesPendientes.items],
                        'total': bolsonesPendientes.total,
                        'pages': bolsonesPendientes.pages,
                        'page': page
                        })
    
    
    def post(self):
        bolsonPendiente = bolsonesModel.from_json(request.get_json())
        try:
            db.session.add(bolsonPendiente)
            db.session.commit()
        except Exception as error:
            return 'Formato no correcto', 400
        return bolsonPendiente.to_json(), 201
    