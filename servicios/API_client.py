# api_client.py
import requests

class APIClient:
    BASE_URL = "http://190.217.58.246:5186/api/SGV/procedures/execute"

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

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud API: {e}")
            return None

    def get_data(self, where_condition=None, order_by=None, limit_clause=None, select_columns=None):
        response = self._make_request("select_json_entity", where_condition, order_by, limit_clause, select_columns=select_columns)
        return response.get('outputParams', {}).get('result', []) if response else []

    def insert_data(self, json_data=None):
        return self._make_request("insert_json_entity", json_data=json_data)

    def update_data(self, where_condition=None, json_data=None):
        return self._make_request("update_json_entity", where_condition=where_condition, json_data=json_data)

    def delete_data(self, where_condition=None):
        return self._make_request("delete_json_entity", where_condition=where_condition)

