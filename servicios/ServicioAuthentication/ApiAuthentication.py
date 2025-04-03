import requests

class APIClient:
    BASE_URL = "http://190.217.58.246:5186/api/SGV/procedures/execute"  # URL de la API

    def __init__(self, table_name):
        self.table_name = table_name

    def _make_request(self, procedure, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        """Realiza una solicitud a la API con los parámetros dados"""
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
            response.raise_for_status()  # Lanza un error si la solicitud falla
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"Error HTTP: {err}")
            print("Detalles de la respuesta:", response.text)
            return None
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            return None

    def get_data(self, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        """Obtiene datos de la API con una condición WHERE opcional"""
        response = self._make_request(
            procedure="select_json_entity",
            where_condition=where_condition,
            order_by=order_by,
            limit_clause=limit_clause,
            json_data=json_data,
            select_columns=select_columns
        )
        return response.get('outputParams', {}).get('result', []) if response else []

    def insert_data(self, json_data=None):
        """Inserta datos en la API"""
        return self._make_request(
            procedure="insert_json_entity", 
            json_data=json_data
        )

    def update_data(self, where_condition=None, json_data=None):
        """Actualiza los datos en la API usando la condición WHERE"""
        if not where_condition or not json_data:
            print("Faltan datos: where_condition o json_data son necesarios.")
            return None
        
        print(f"Condición WHERE: {where_condition}")
        print(f"Datos a actualizar: {json_data}")

        response = self._make_request(
            procedure="update_json_entity",
            where_condition=where_condition,
            json_data=json_data
        )

        if response:
            print(f"Respuesta de la API: {response}")
        else:
            print("No se recibió respuesta de la API.")
        
        return response

    def delete_data(self, where_condition=None):
        """Elimina datos de la API con una condición WHERE opcional"""
        return self._make_request(
            procedure="delete_json_entity",
            where_condition=where_condition
        )

    def auto_update_data(self, where_condition=None, json_data=None):
        """Actualiza automáticamente los datos en la API si han cambiado"""
        if not where_condition or not json_data:
            return None

        current_data = self.get_data(where_condition=where_condition)
        if not current_data:
            return None

        current_data = current_data[0]  # Tomamos el primer resultado si hay varios

        updated_data = {key: value for key, value in json_data.items() if current_data.get(key) != value}

        if updated_data:
            return self.update_data(where_condition=where_condition, json_data=updated_data)
        else:
            print("No hubo cambios en los datos.")
            return None