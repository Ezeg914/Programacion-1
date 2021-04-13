import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    
    import main.resources as resources


    api.add_resource(resources.bolsonesResource, '/bolsones')
    api.add_resource(resources.bolsonResource, '/bolson/<id>')
    
    api.add_resource(resources.bolsonesPendienteResource, '/bolsones-pendiente')
    api.add_resource(resources.bolsonPendienteResource, '/bolson-pendiente/<id>')
    
    api.add_resource(resources.bolsonesPrevioResource, '/bolsones-previo')
    api.add_resource(resources.bolsonPrevioResource, '/bolson-previo/<id>')
    
    api.add_resource(resources.bolsonesVentaResource, '/bolsones-venta')
    api.add_resource(resources.bolsonVentaResource, '/bolson-venta/<id>')
    
    api.add_resource(resources.clientesResource, '/clientes')
    api.add_resource(resources.clienteResource, '/cliente/<id>')
    
    api.add_resource(resources.comprasResource, '/compras')
    api.add_resource(resources.compraResource, '/compra/<id>')
   
    api.add_resource(resources.productosResource, '/productos')
    api.add_resource(resources.productoResource, '/producto/<id>')
    
    api.add_resource(resources.proveedoresResource, '/proveedores')
    api.add_resource(resources.proveedorResource, '/proveedor/<id>')

    api.init_app(app)
    return app
    