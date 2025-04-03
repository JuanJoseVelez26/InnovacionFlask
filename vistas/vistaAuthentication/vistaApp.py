from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modelos.modeloAuthentication import APIClient  # Asegúrate de que el modelo APIClient esté importado

auth_bp = Blueprint('auth', __name__)

# Función para cargar la página principal de la aplicación y mostrar notificaciones
@auth_bp.route('/app/')
def app():
    user_email = session.get('user_email')

    if not user_email:
        flash("Debes iniciar sesión para ver tus notificaciones.", "warning")
        return redirect(url_for('auth.login'))  # Ajusta la ruta según tu sistema

    api_client = APIClient(table_name="notificaciones")
    where_condition = f"usuario_email = '{user_email}'"
    notificaciones = api_client.get_data(where_condition=where_condition)

    print("Notificaciones recuperadas:", notificaciones)

    if not notificaciones or not isinstance(notificaciones, list):
        flash("No se pudieron cargar las notificaciones.", "warning")
        notificaciones = []

    notificaciones = sorted(notificaciones, key=lambda x: x.get('leida', True))
    return render_template('app.html', notificaciones=notificaciones)


# Función para marcar una notificación como leída
@auth_bp.route('/marcar_leida', methods=['POST'])
def marcar_leida():
    notificacion_id = request.form.get('id')
    
    if notificacion_id:
        api_client = APIClient(table_name="notificaciones")
        where_condition = f"id = {notificacion_id}"
        json_data = {"leida": True}
        response = api_client.update_data(where_condition=where_condition, json_data=json_data)
        
        if response:
            flash("Notificación marcada como leída.", "success")
        else:
            flash("No se pudo marcar como leída. Intenta nuevamente.", "error")
    else:
        flash("ID de notificación no válido.", "error")
    
    return redirect(url_for('auth.app'))


# Función para eliminar una notificación
@auth_bp.route('/eliminar_notificacion', methods=['POST'])
def eliminar_notificacion():
    notificacion_id = request.form.get('id')
    
    if notificacion_id:
        api_client = APIClient(table_name="notificaciones")
        where_condition = f"id = {notificacion_id}"
        response = api_client.delete_data(where_condition=where_condition)
        
        if response:
            flash("Notificación eliminada correctamente.", "success")
        else:
            flash("No se pudo eliminar la notificación. Intenta nuevamente.", "error")
    else:
        flash("ID de notificación no válido.", "error")
    
    return redirect(url_for('auth.app'))


# Función para listar proyectos
@auth_bp.route('/listar_proyectos')
def listar_proyectos():
    user_email = session.get('user_email')

    if not user_email:
        return redirect(url_for('auth.login'))
    try:
        client = APIClient('proyecto')
        proyectos = client.get_data()

        print(f"Proyectos obtenidos: {proyectos}")
        
        ideas = [p for p in proyectos if p['tipo_origen'] == 'idea']
        oportunidades = [p for p in proyectos if p['tipo_origen'] == 'oportunidad']
        soluciones = [p for p in proyectos if p['tipo_origen'] == 'solución']
        
        print(f"Ideas: {ideas}")
        print(f"Oportunidades: {oportunidades}")
        print(f"Soluciones: {soluciones}")
        
        return render_template('listar_proyectos.html', ideas=ideas, oportunidades=oportunidades, soluciones=soluciones)
    except Exception as e:
        print(f"Error al obtener los proyectos: {e}")
        return render_template('listar_proyectos.html', proyectos=[])
