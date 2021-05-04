from .. import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    proveedorid = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return '<productos: %r %r >' % (self.nombre, self.proveedorid)

    def to_json(self):
        productos_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'proveedorid': self.proveedorid,

        }
        return productos_json
    @staticmethod

    def from_json(productos_json):
        id = productos_json.get('id')
        nombre = productos_json.get('nombre')
        proveedorid = productos_json.get('proveedorid')
        return Productos(id=id,
                    nombre=nombre,
                    proveedorid=proveedorid,
                    )
