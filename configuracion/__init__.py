import json
import os

# Cargar configuración desde el archivo JSON
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

# Variables globales
SECRET_KEY = config["SECRET_KEY"]
DEBUG = config["DEBUG"]
SQLALCHEMY_DATABASE_URI = config["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
API_URL = config["API_URL"]