from flask import Flask, jsonify, request, session, redirect, url_for, render_template
import json
from routes.rutaAuthentication import auth_bp
from routes.rutaIdeas import ideas_bp
from routes.rutaOportunidades import oportunidades_bp
from routes.rutaSoluciones import soluciones_bp
from routes.rutaPerfil import perfil_bp
from configuracion.config import Config
from flask_session import Session

app = Flask(__name__)  

# Cargar configuración desde la clase Config
app.config.from_object(Config)

# Inicializar la extensión de sesiones
Session(app)

# Ruta raíz
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

# Registrar Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(ideas_bp, url_prefix='/ideas')
app.register_blueprint(oportunidades_bp, url_prefix='/oportunidades')
app.register_blueprint(soluciones_bp, url_prefix='/soluciones')
app.register_blueprint(perfil_bp, url_prefix='/perfil')

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])