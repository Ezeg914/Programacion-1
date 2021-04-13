from .. import db

class compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    fechaCompra = db.Column(db.DateTime, nullable=False)
    clienteid = db.Column(db.Integer, nullable=False)
    bolsonid = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return '<compra: %r %r %r %r %r >' % (self.nombre, self.retirado, self.fechaCompra, self.clienteid, self.bolsonid)

    def to_json(self):
        compra_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'retirado': (self.retirado),
            'fechaCompra': str(self.fechaCompra),
            'clienteid': self.clienteid,
            'bolsonid': self.bolsonid,

        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        nombre = compra_json.get('nombre')
        retirado = compra_json.get('retirado')
        fechaCompra = compra_json.get('fechaCompra')
        clienteid = compra_json.get('clienteid')
        bolsonid = compra_json.get('bolsonid')
        return Professor(id=id,
                    nombre=nombre,
                    retirado=retirado,
                    fechaCompra=fechaCompra,
                    clienteid=clienteid,
                    bolsonid=bolsonid,
                    )
