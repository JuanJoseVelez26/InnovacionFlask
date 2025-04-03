import requests
import os

class APIClient:
    BASE_URL = os.getenv("API_URL", "http://default-api-url.com")  # Usa una URL por defecto si no está definida

    def __init__(self, table_name):
        self.table_name = table_name

    def _make_request(self, procedure, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
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
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Lanza una excepción si la solicitud falla
        return response.json()

    def get_data(self, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        return self._make_request(
            procedure="select_json_entity",
            where_condition=where_condition,
            order_by=order_by,
            limit_clause=limit_clause,
            json_data=json_data,
            select_columns=select_columns
        ).get('outputParams', {}).get('result', [])

    def delete_data(self, where_condition=None):
        return self._make_request(
            procedure="delete_json_entity",
            where_condition=where_condition
        )

    def insert_data(self, json_data=None):
        return self._make_request(
            procedure="insert_json_entity",
            json_data=json_data
        )

    def update_data(self, where_condition=None, json_data=None):
        return self._make_request(
            procedure="update_json_entity",
            where_condition=where_condition,
            json_data=json_data
        )
