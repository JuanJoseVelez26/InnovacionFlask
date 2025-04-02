from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from servicios.servicioLogin import loginAPIClient
from forms.formLogin import RegisterForm

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def registro_usuario():
    form = RegisterForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        # Extraer datos del formulario
        email = form.email.data
        contrasena = form.password1.data
        nombre = form.nombre.data
        rol = 'Usuario'  # Rol por defecto
        fecha_nacimiento = form.fecha_nacimiento.data
        direccion = form.direccion.data
        descripcion = form.descripcion.data
        area_expertise = form.area_expertise.data
        informacion_adicional = form.informacion_adicional.data

        # Encriptar contraseña
        contrasena_encriptada = generate_password_hash(contrasena)

        # Datos del usuario
        usuario_data = {
            "email": email,
            "password": contrasena_encriptada,
            "is_active": False,
            "is_staff": False,
            "is_superuser": False,
            "last_login": None
        }

        # Crear usuario
        usuario_client = loginAPIClient('usuario')
        usuario_response = usuario_client.insert_data(json_data=usuario_data)
        
        if usuario_response and 'outputParams' in usuario_response:
            # Datos del perfil
            perfil_data = {
                "usuario_email": email,
                "nombre": nombre,
                "rol": rol,
                "fecha_nacimiento": str(fecha_nacimiento),
                "direccion": direccion,
                "descripcion": descripcion
            }

            perfil_client = loginAPIClient('perfil')
            perfil_response = perfil_client.insert_data(json_data=perfil_data)

            if perfil_response and 'outputParams' in perfil_response:
                # Registro de áreas de expertise
                if area_expertise:
                    area_client = loginAPIClient('areas_expertise')
                    area_data = {"usuario_email": email, "area": area_expertise}
                    area_client.insert_data(json_data=area_data)
                
                # Registro de información adicional
                if informacion_adicional:
                    info_client = loginAPIClient('informacion_adicional')
                    info_data = {"usuario_email": email, "info": informacion_adicional}
                    info_client.insert_data(json_data=info_data)
                
                flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
                return redirect(url_for('login.login_view'))
            else:
                flash("Error al crear el perfil.", "danger")
        else:
            flash("Error al crear el usuario.", "danger")

    return render_template('login/register.html', form=form)