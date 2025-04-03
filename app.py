from flask import Flask, jsonify, request, session, redirect, url_for
import json
from routes.rutaAuthentication import auth_bp
from routes.rutaIdeas import ideas_bp
from routes.rutaOportunidades import oportunidades_bp
from routes.rutaSoluciones import soluciones_bp
from routes.rutaPerfil import perfil_bp

app = Flask(__name__)  

# Cargar configuración desde JSON
with open('configuracion/config.json') as config_file:
    config = json.load(config_file)

# Actualizar la configuración de Flask con los valores del JSON
app.config.update(config)

# Registrar las rutas importadas
#app.register_blueprint(routes_blueprint)

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(ideas_bp)
app.register_blueprint(oportunidades_bp)
app.register_blueprint(soluciones_bp)
app.register_blueprint(perfil_bp)

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])