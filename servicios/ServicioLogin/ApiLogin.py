import requests

class APIConnectionError(Exception):
    """Excepción personalizada para errores de conexión con la API"""
    pass

class LoginAPIClient:
    BASE_URL = "http://190.217.58.246:5186/api/SGV/procedures/execute"  # URL de la API

    def __init__(self, table_name):
        self.table_name = table_name

    def _make_request(self, procedure, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        """Realiza una solicitud POST a la API con los parámetros dados"""
        url = self.BASE_URL
        payload = {
            "procedure": procedure,
            "parameters": {
                "table_name": self.table_name,
                "where_condition": where_condition,
                "order_by": order_by,
                "limit_clause": limit_clause,
                "json_data": json_data if json_data else {},
                "select_columns": select_columns
            }
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Lanza una excepción si hay error HTTP
            return response.json()
        except requests.exceptions.RequestException as e:
            raise APIConnectionError(f"Error de conexión con la API: {e}")

    def get_data(self, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        """Obtiene datos de la API con filtros opcionales"""
        result = self._make_request(
            procedure="select_json_entity",
            where_condition=where_condition,
            order_by=order_by,
            limit_clause=limit_clause,
            json_data=json_data,
            select_columns=select_columns
        )
        return result.get('outputParams', {}).get('result', [])

    def delete_data(self, where_condition=None):
        """Elimina registros de la API"""
        return self._make_request(procedure="delete_json_entity", where_condition=where_condition)

    def insert_data(self, json_data=None):
        """Inserta datos en la API"""
        return self._make_request(procedure="insert_json_entity", json_data=json_data)

    def update_data(self, where_condition=None, json_data=None):
        """Actualiza datos en la API"""
        return self._make_request(procedure="update_json_entity", where_condition=where_condition, json_data=json_data)
