from .. import db
from datetime import datetime
from . import clientesModel
from . import bolsonesModel

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    retirado = db.Column(db.Boolean, nullable=False)
    fechaCompra = db.Column(db.DateTime, default=datetime.now())
    clienteid =  db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    cliente = db.relationship('Clientes',back_populates="compra")
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolsones.id'), nullable=False)
    bolson = db.relationship('Bolsones',back_populates="compra")

    
    def __repr__(self):
        return '<compra: %r %r %r  >' % (self.nombre, self.retirado, self.fechaCompra,)

    def to_json(self):
        self.cliente = db.session.query(clientesModel).get_or_404(self.clienteid)
        self.bolson = db.session.query(bolsonesModel).get_or_404(self.bolsonid)
        compra_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'retirado': (self.retirado),
            'fechaCompra': self.fechaCompra.strftime('%Y-%m-%d'),
            'cliente': self.cliente.to_json(),
            'bolson': self.bolson.to_json()

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
        return Compra(id=id,
                    nombre=nombre,
                    retirado=retirado,
                    fechaCompra=fechaCompra,
                    clienteid=clienteid,
                    bolsonid=bolsonid
                    )
