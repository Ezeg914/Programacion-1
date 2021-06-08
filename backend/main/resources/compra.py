from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import compraModel


class Compra(Resource):
    def get(self, id):
        compra = db.session.query(compraModel).get_or_404(id)
        return compra.to_json()
    
    def delete(self, id):
        compra = db.session.query(compraModel).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204

    def put(self, id):
        compra = db.session.query(compraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
        db.session.add(compra)
        db.session.commit()
        return compra.to_json() , 201

class Compras(Resource):
    def get(self):
        page = 1
        per_page = 10
        compras = db.session.query(compraModel).all()
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        compras = compras.paginate(page, per_page, True, 30)
        return jsonify({'compras': [compra.to_json() for compra in compras.items],
                        'total': compras.total,
                        'pages': compras.pages,
                        'page': page
                        })

    def post(self):
        compra = compraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201