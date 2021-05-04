from .. import db

class ProductosBolsones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productoid = db.Column(db.Integer, nullable=False)
    bolsonid = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return '<productosBolsones: %r %r >' % (self.productoid, self.bolsonid)

    def to_json(self):
        productosBolsones_json = {
            'id': self.id,
            'productoid': self.productoid,
            'bolsonid': self.bolsonid,

        }
        return productosBolsones_json
    @staticmethod

    def from_json(productosBolsones_json):
        id = productosBolsones_json.get('id')
        productoid = productosBolsones_json.get('productoid')
        bolsonid = productosBolsones_json.get('bolsonid')
        return ProductosBolsones(id=id,
                    productoid=productoid,
                    bolsonid=bolsonid,
                    )
