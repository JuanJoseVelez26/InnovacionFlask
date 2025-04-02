from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from werkzeug.security import check_password_hash, generate_password_hash
import requests
from servicios.servicioLogin.ApiLogin import LoginAPIClient

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Iniciar Sesión')

    def validate_user(self):
        """Validar usuario con la API"""
        usuario_client = LoginAPIClient('usuario')
        users = usuario_client.get_data(where_condition=f"email = '{self.email.data}'", select_columns="email, password")

        if not users:
            raise ValueError("Usuario no encontrado.")

        user = users[0]  # Primer usuario encontrado
        if not check_password_hash(user['password'], self.password.data):  # Comparar contraseña encriptada
            raise ValueError("Contraseña incorrecta.")

        return user  # Devuelve el usuario si la validación es correcta
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password1', message='Las contraseñas no coinciden.')])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired(), Length(max=255)])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    area_expertise = StringField('Área de Expertise', validators=[Length(max=100)])
    informacion_adicional = TextAreaField('Información Adicional')
    submit = SubmitField('Registrar')

    def save_user(self):
        """Guarda el usuario en la API"""
        usuario_client = LoginAPIClient('usuario')
        hashed_password = generate_password_hash(self.password1.data)
        user_data = {
            "email": self.email.data,
            "password": hashed_password,
            "nombre": self.nombre.data,
            "fecha_nacimiento": str(self.fecha_nacimiento.data),
            "direccion": self.direccion.data,
            "descripcion": self.descripcion.data,
            "area_expertise": self.area_expertise.data,
            "informacion_adicional": self.informacion_adicional.data
        }
        result = usuario_client.insert_data(json_data=user_data)
        return result
   