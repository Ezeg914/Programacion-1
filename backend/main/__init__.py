import os
from flask import Flask
from dotenv import load_dotenv

from flask_restful import Api

import main.resources as resources

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()

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
    