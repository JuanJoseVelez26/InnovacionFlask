from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from servicios.servicioLogin.ApiLogin import LoginAPIClient 
from modelos.modeloLogin.modeloLogin import Usuario
from forms.formLogin import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = Usuario.authenticate(email, password)
        if user:
            session['user'] = user['email']  # Guardar en sesión
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('dashboard'))  # Redirigir a dashboard o página principal
        
        flash("Credenciales inválidas", "danger")
    
    return render_template('login/login.html', form=form)

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