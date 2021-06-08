from .. import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    compra = db.relationship('Compra', back_populates='cliente', cascade='all, delete-orphan')
    productos = db.relationship('Productos', back_populates='proveedor', cascade='all, delete-orphan')



    def __repr__(self):
        return '<Usuario: %r %r %r %r %r >' % (self.nombre, self.apellido, self.telefono, self.email)

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'telefono': str(self.telefono),
            'email': str(self.email),
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        email = usuario_json.get('email')
        return Usuario(id=id,
                           nombre=nombre,
                           apellido=apellido,
                           telefono=telefono,
                           email=email,
                           )
