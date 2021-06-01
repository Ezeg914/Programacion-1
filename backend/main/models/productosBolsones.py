from .. import db

class ProductosBolsones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolsones.id'), nullable=False)
    bolson = db.relationship('Bolsones',back_populates="productoBolsones")
    productoid = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    producto = db.relationship('Productos',back_populates="productoBolsones")


    
    def __repr__(self):
        return '<productosBolsones: %r %r >' % (self.productoid, self.bolsonid)

    def to_json(self):
        self.bolson = db.session.query(bolsonesModel).get_or_404(self.bolsonid)
        self.producto = db.session.query(productosModel).get_or_404(self.productoid)
        productosBolsones_json = {
            'id': self.id,
            'productoid': self.productoid,
            'bolson': self.bolson.to_json()

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
