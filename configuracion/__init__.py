from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cargar configuración desde JSON
    with open("configuracion/config.json") as config_file:
        config = json.load(config_file)
        app.config.update(config)

    db.init_app(app)

    # Crear directorios si no existen
    if not os.path.exists(app.config["MEDIA_ROOT"]):
        os.makedirs(app.config["MEDIA_ROOT"])

    return app