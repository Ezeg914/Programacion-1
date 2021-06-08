from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import productosModel

class Producto(Resource):
    def get(self, id):
        producto = db.session.query(productosModel).get_or_404(id)
        return producto.to_json()
    
    def delete(self, id):
        producto = db.session.query(productosModel).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204
        

    def put(self, id):
        producto = db.session.query(productosModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        db.session.add(producto)
        db.session.commit()
        return producto.to_json() , 201

class Productos(Resource):
    def get(self):
        page = 1
        per_page = 10
        productos = db.session.query(productosModel).all()
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        productos = productos.paginate(page, per_page, True, 30)
        return jsonify({'productos': [producto.to_json() for producto in productos.items],
                        'total': productos.total,
                        'pages': productos.pages,
                        'page': page
                        })
    def post(self):
        productos = productosModel.from_json(request.get_json())
        db.session.add(productos)
        db.session.commit()
        return productos.to_json(), 201