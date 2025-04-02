from flask import Blueprint, jsonify

perfil_bp = Blueprint('perfil', __name__, url_prefix='/perfil')

@perfil_bp.route('/')
def perfil():
    return jsonify({"message": "Perfil del usuario"})

@perfil_bp.route('/update/', methods=['POST'])
def update_perfil():
    return jsonify({"message": "Perfil actualizado"})

@perfil_bp.route('/delete/', methods=['POST'])
def delete_perfil():
    return jsonify({"message": "Perfil eliminado"})
