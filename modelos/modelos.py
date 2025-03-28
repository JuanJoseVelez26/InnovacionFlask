# models.py
from servicios import APIClient

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

# Modelos específicos basados en los archivos proporcionados
class Usuario(BaseModel):
    def __init__(self):
        super().__init__("usuarios")

class Idea(BaseModel):
    def __init__(self):
        super().__init__("ideas")

class Innovacion(BaseModel):
    def __init__(self):
        super().__init__("innovacion")

class Oportunidad(BaseModel):
    def __init__(self):
        super().__init__("oportunidades")

class Perfil(BaseModel):
    def __init__(self):
        super().__init__("perfil")

class Solucion(BaseModel):
    def __init__(self):
        super().__init__("soluciones")

class Proyecto(BaseModel):
    def __init__(self):
        super().__init__("proyectos")

class Recurso(BaseModel):
    def __init__(self):
        super().__init__("recursos")

class Actividad(BaseModel):
    def __init__(self):
        super().__init__("actividades")

class Evaluacion(BaseModel):
    def __init__(self):
        super().__init__("evaluaciones")

class Comentario(BaseModel):
    def __init__(self):
        super().__init__("comentarios")

class Indicador(BaseModel):
    def __init__(self):
        super().__init__("indicadores")

class Meta(BaseModel):
    def __init__(self):
        super().__init__("metas")

class Rol(BaseModel):
    def __init__(self):
        super().__init__("roles")

class Permiso(BaseModel):
    def __init__(self):
        super().__init__("permisos")

class Notificacion(BaseModel):
    def __init__(self):
        super().__init__("notificaciones")
