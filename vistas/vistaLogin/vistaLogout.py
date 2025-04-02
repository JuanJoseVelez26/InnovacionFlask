from flask import Blueprint, session, redirect, url_for

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout_view():
    # Limpiar la sesión del usuario
    session.clear()
    return redirect(url_for('login.login_view'))  # Redirige a la página de inicio de sesión