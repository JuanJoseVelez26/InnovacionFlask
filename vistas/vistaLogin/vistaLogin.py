from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from modelos.modeloLogin import Usuario
from servicios.servicioLogin.ApiLogin import AuthenticationError

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            user = Usuario.authenticate(email, password)
            if not user:
                raise AuthenticationError("Correo electrónico o contraseña inválidos.")

            profile = Usuario.get_profile_data(email)
            if not profile:
                raise AuthenticationError("No se encontraron datos de perfil para el usuario.")

            fecha_nacimiento = profile.get('fecha_nacimiento', '')
            if fecha_nacimiento:
                try:
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").strftime("%d/%m/%Y")
                except ValueError:
                    fecha_nacimiento = None

            session['user_email'] = user['email']
            session['user_name'] = profile.get('nombre', '')
            session['user_role'] = profile.get('rol', '')
            session['user_birthdate'] = fecha_nacimiento
            session['user_address'] = profile.get('direccion', '')
            session['user_description'] = profile.get('descripcion', '')
            session['user_area_expertise'] = profile.get('area_expertise', '')
            session['user_info_adicional'] = profile.get('info_adicional', '')

            return redirect(url_for('authentication.app'))

        except AuthenticationError as e:
            flash(str(e), 'danger')
            return render_template('login/login.html')

    return render_template('login/login.html')
