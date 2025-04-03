import jwt
from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, flash
from functools import wraps
from werkzeug.security import generate_password_hash
from servicios.servicioLogin.ApiLogin import LoginAPIClient
from modelos.modeloLogin.modeloLogin import Usuario
from forms.formLogin import LoginForm
from configuracion.config import SECRET_KEY  # Se recomienda manejar las configuraciones en config.py

auth_bp = Blueprint('auth', __name__)

# Definir el decorador dentro del controlador
def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({'error': 'Token no proporcionado'}), 401
        
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = payload.get("user")  
        except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return jsonify({'error': 'Token inválido o expirado'}), 401

        return view_func(*args, **kwargs)
    
    return _wrapped_view

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = Usuario.authenticate(email, password)
        if user:
            session['user'] = user['email']
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('auth.app'))
        
        flash("Credenciales inválidas", "danger")
    
    return render_template('templatesLogin/Login.html', form=form)

@auth_bp.route('/logout/', methods=['GET'])
def logout():
    session.pop('user', None)
    flash("Sesión cerrada", "info")
    return redirect(url_for('auth.login'))

@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = generate_password_hash(data.get('password'))
        
        usuario_client = LoginAPIClient('usuario')
        result = usuario_client.insert_data(json_data={"email": email, "password": password})
        
        if result:
            flash("Registro exitoso", "success")
            return jsonify({"message": "Registro exitoso"}), 201
        
        flash("Error al registrar usuario", "danger")
        return jsonify({"error": "Error al registrar usuario"}), 400
    
    return render_template('register/register.html')

@auth_bp.route('/perfil/', methods=['GET'])
@jwt_required
def perfil():
    return jsonify({"message": "Bienvenido al perfil"}), 200

@auth_bp.route('/app/')
@jwt_required
def app():
    return render_template('templatesAuthentication/app.html')
