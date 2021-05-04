from .. import db

class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<proveedores: %r %r >' % (self.nombre, self.telefono)

    def to_json(self):
        proveedores_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'telefono': str(self.telefono),

        }
        return proveedores_json
    @staticmethod

    def from_json(proveedores_json):
        id = proveedores_json.get('id')
        nombre = proveedores_json.get('nombre')
        telefono = proveedores_json.get('telefono')
        return Proveedores(id=id,
                    nombre=nombre,
                    telefono=telefono,
                    )
