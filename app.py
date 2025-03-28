from flask import Flask
from routes import app as routes_blueprint  # Importamos las rutas desde routes.py
import json

app = Flask(__name__)

# Cargar configuración desde JSON
with open('config.json') as config_file:
    config = json.load(config_file)

# Actualizar la configuración de Flask con los valores del JSON
app.config.update(config)

# Registrar las rutas importadas
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])