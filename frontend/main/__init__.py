import os
from flask import Flask
from dotemv impor load_dotemv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    return app