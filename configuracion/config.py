import os

# Exportar SECRET_KEY directamente
SECRET_KEY = os.getenv("django-insecure-#1!vjo3l)hf!zh+kzob43t2-f)ssp9z3k-b2@j(@&w9+@6l21@", "clave-segura")

class Config:
    # Seguridad
    SECRET_KEY = SECRET_KEY  # Usa la variable exportada
    DEBUG = os.getenv("DEBUG", "True") == "True"

    # Directorios
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Base de Datos
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de sesiones
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_FILE_DIR = os.path.join(BASE_DIR, "flask_sessions")

    # Archivos estáticos y multimedia
    STATIC_FOLDER = "static"
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "media")

    # Configuración de API externa
    API_URL = os.getenv("API_URL", "http://190.217.58.246:5186/api/SGV/procedures/execute")

    # Configuración de autenticación y hashing de contraseñas
    PASSWORD_HASH_METHOD = "pbkdf2:sha256"
    PASSWORD_SALT = os.getenv("PASSWORD_SALT", "un-salt-seguro")

    # Internacionalización y zona horaria
    LANGUAGE_CODE = "es"
    TIMEZONE = "UTC"

    # Extensiones como Flask-WTF (Formularios)
    WTF_CSRF_ENABLED = True
