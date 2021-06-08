from .. import db
from datetime import datetime

class Bolsones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    aprobado = db.Column(db.Boolean, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now())
    compra = db.relationship("Compra", back_populates="bolson",cascade="all, delete-orphan")
    productoBolsones = db.relationship("ProductosBolsones", back_populates="bolson",cascade="all, delete-orphan")

    
    def __repr__(self):
        return '<bolsones: %r %r %r >' % (self.nombre, self.aprobado, self.fecha)

    def to_json(self):
        bolsones_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'aprobado': (self.aprobado),
            'fecha': self.fecha.strftime('%Y-%m-%d'),

        }
        return bolsones_json
    
    @staticmethod
    def from_json(bolsones_json):
        id = bolsones_json.get('id')
        nombre = bolsones_json.get('nombre')
        aprobado = bolsones_json.get('aprobado')
        fecha = bolsones_json.get('fecha')
        return Bolsones(id=id,
                    nombre=nombre,
                    aprobado=aprobado,
                    fecha=fecha,
                    )
