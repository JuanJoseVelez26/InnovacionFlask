import requests
from werkzeug.security import check_password_hash
from servicios.servicioLogin.ApiLogin import LoginAPIClient

class Usuario:
    @staticmethod
    def authenticate(email, password):
        """Autentica a un usuario verificando la contraseña"""
        usuario_client = LoginAPIClient('usuario')
        users = usuario_client.get_data(where_condition=f"email = '{email}'", select_columns="email, password")

        if users:
            user = users[0]  # Primer usuario encontrado
            if check_password_hash(user['password'], password):  # Comparar contraseña encriptada
                return user
        return None

    @staticmethod
    def get_profile_data(email):
        """Obtiene el perfil de usuario, incluyendo información adicional y área de expertise"""
        perfil_client = LoginAPIClient('perfil')
        profile_data = perfil_client.get_data(where_condition=f"usuario_email = '{email}'",
                                              select_columns="nombre, rol, fecha_nacimiento, direccion, descripcion")
        
        profile_data = profile_data[0] if profile_data else {}

        # Obtener información adicional
        info_client = LoginAPIClient('informacion_adicional')
        info_result = info_client.get_data(where_condition=f"usuario_email = '{email}'", select_columns="info")
        profile_data['info_adicional'] = info_result[0]['info'] if info_result else ''

        # Obtener área de expertise
        expertise_client = LoginAPIClient('areas_expertise')
        expertise_result = expertise_client.get_data(where_condition=f"usuario_email = '{email}'", select_columns="area")
        profile_data['area_expertise'] = expertise_result[0]['area'] if expertise_result else ''

        return profile_data if profile_data else None