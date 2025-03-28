from servicios.API_client import APIClient

class BaseModel:
    def __init__(self, table_name):
        self.client = APIClient(table_name)

    def get_all(self, order_by=None, limit_clause=None, select_columns=None):
        return self.client.get_data(order_by=order_by, limit_clause=limit_clause, select_columns=select_columns)

    def get_by_condition(self, where_condition):
        return self.client.get_data(where_condition=where_condition)

    def insert(self, data):
        return self.client.insert_data(json_data=data)

    def update(self, where_condition, data):
        return self.client.update_data(where_condition=where_condition, json_data=data)

    def delete(self, where_condition):
        return self.client.delete_data(where_condition=where_condition)

# Generar clases dinámicamente en lugar de escribirlas manualmente
modelo_nombres = [
    "usuarios", "ideas", "innovacion", "oportunidades", "perfil", "soluciones",
    "proyectos", "recursos", "actividades", "evaluaciones", "comentarios",
    "indicadores", "metas", "roles", "permisos", "notificaciones"
]

# Crear las clases dinámicamente usando `type`
for nombre in modelo_nombres:
    globals()[nombre.capitalize()] = type(nombre.capitalize(), (BaseModel,), {"__init__": lambda self, n=nombre: super(self.__class__, self).__init__(n)})

