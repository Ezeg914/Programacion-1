from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import usuariosModel



class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(usuariosModel).get_or_404(id)
        if cliente.role == 'cliente':
            return cliente.to_json()
        else:
            return '', 404

    
    def delete(self, id):
        cliente = db.session.query(usuariosModel).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return "", 204
     
        
    def put(self, id):
        cliente = db.session.query(usuariosModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json() , 201

class Clientes(Resource):
    def get(self):
        page = 1
        per_page = 10
        clientes = db.session.query(usuariosModel).filter(usuariosModel.role == 'cliente')
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        clientes = clientes.paginate(page, per_page, True, 30)
        return jsonify({'clientes': [cliente.to_json() for cliente in clientes.items],
                        'total': clientes.total,
                        'pages': clientes.pages,
                        'page': page
                        })


    def post(self):
        clientes = usuariosModel.from_json(request.get_json())
        db.session.add(clientes)
        db.session.commit()
        return clientes.to_json(), 201
        