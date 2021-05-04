from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import proveedoresModel


class Proveedor(Resource):
    def get(self, id):
        proveedor = db.session.query(proveedoresModel).get_or_404(id)
        return proveedor.to_json()

    def delete(self, id):
        proveedor = db.session.query(proveedoresModel).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204

    def put(self, id):
        proveedor = db.session.query(proveedoresModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json() , 201


class Proveedores(Resource):
    def get(self):
        proveedores = db.session.query(proveedoresModel).all()
        return jsonify([proveedores.to_json() for proveedores in proveedores])

    def post(self):
        proveedores = proveedoresModel.from_json(request.get_json())
        db.session.add(proveedores)
        db.session.commit()
        return proveedores.to_json(), 201