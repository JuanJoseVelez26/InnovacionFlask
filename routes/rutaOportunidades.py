from flask import Blueprint, jsonify

oportunidades_bp = Blueprint('oportunidades', __name__, url_prefix='/oportunidades')

@oportunidades_bp.route('/list/')
def list_oportunidades():
    return jsonify({"message": "Listado de oportunidades"})

@oportunidades_bp.route('/create/', methods=['POST'])
def create_oportunidad():
    return jsonify({"message": "Oportunidad creada"})

@oportunidades_bp.route('/update/<int:pk>/', methods=['POST'])
def update_oportunidad(pk):
    return jsonify({"message": f"Oportunidad {pk} actualizada"})

@oportunidades_bp.route('/delete/<int:pk>/', methods=['POST'])
def delete_oportunidad(pk):
    return jsonify({"message": f"Oportunidad {pk} eliminada"})

@oportunidades_bp.route('/detail/<int:pk>/')
def detail_oportunidad(pk):
    return jsonify({"message": f"Detalle de la oportunidad {pk}"})
