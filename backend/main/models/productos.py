from .. import db
from .proveedores import Proveedores as proveedoresModel

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    productoBolsones = db.relationship("ProductosBolsones", back_populates="producto",cascade="all, delete-orphan")
    proveedorid = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    proveedor = db.relationship('Proveedores',back_populates="producto")

    
    def __repr__(self):
        return '<productos: %r %r >' % (self.nombre)

    def to_json(self):
        self.proveedor = db.session.query(proveedoresModel).get_or_404(self.proveedorid)
        productos_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'proveedor': self.proveedor.to_json()

        }
        return productos_json
    @staticmethod

    def from_json(productos_json):
        id = productos_json.get('id')
        nombre = productos_json.get('nombre')
        proveedorid = productos_json.get('proveedorid')
        return Productos(id=id,
                    nombre=nombre,
                    proveedorid=proveedorid
                    )
