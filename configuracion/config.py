import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Exportar SECRET_KEY directamente para compatibilidad
SECRET_KEY = os.getenv("SECRET_KEY")

class Config:
    # Seguridad
    SECRET_KEY = SECRET_KEY
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Directorios
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
    
    # Crear directorio de datos si no existe
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Base de Datos
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(DATA_DIR, 'db.sqlite3')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de sesiones
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hora
    SESSION_FILE_DIR = os.path.join(DATA_DIR, "flask_sessions")
    
    # Crear directorio de sesiones si no existe
    os.makedirs(SESSION_FILE_DIR, exist_ok=True)
    
    # Archivos estáticos y multimedia
    STATIC_FOLDER = "static"
    UPLOAD_FOLDER = os.path.join(DATA_DIR, "media")
    
    # Crear directorio de medios si no existe
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Configuración de API externa
    API_URL = os.getenv("API_URL")
    
    # Configuración de autenticación y hashing de contraseñas
    PASSWORD_HASH_METHOD = "pbkdf2:sha256"
    PASSWORD_SALT = os.getenv("PASSWORD_SALT")
    
    # Configuración de seguridad
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = SECRET_KEY
    
    # Configuración de JWT
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hora
    
    # Internacionalización y zona horaria
    LANGUAGE_CODE = "es"
    TIMEZONE = "UTC"
