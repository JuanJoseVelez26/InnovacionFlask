import json
import os

# Obtener la ruta absoluta del directorio de configuración
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Esto ya apunta a 'configuracion'
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")  # Agregar 'config.json'

# Cargar configuración desde el archivo JSON
with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

# Variables globales
SECRET_KEY = config["SECRET_KEY"]
DEBUG = config["DEBUG"]
SQLALCHEMY_DATABASE_URI = config["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
API_URL = config["API_URL"]