from flask import Blueprint, jsonify

soluciones_bp = Blueprint('soluciones', __name__, url_prefix='/soluciones')

@soluciones_bp.route('/list/')
def list_soluciones():
    return jsonify({"message": "Listado de soluciones"})

@soluciones_bp.route('/create/', methods=['POST'])
def create_solucion():
    return jsonify({"message": "Solución creada"})

@soluciones_bp.route('/update/<int:pk>/', methods=['POST'])
def update_solucion(pk):
    return jsonify({"message": f"Solución {pk} actualizada"})

@soluciones_bp.route('/delete/<int:pk>/', methods=['POST'])
def delete_solucion(pk):
    return jsonify({"message": f"Solución {pk} eliminada"})

@soluciones_bp.route('/detail/<int:pk>/')
def detail_solucion(pk):
    return jsonify({"message": f"Detalle de la solución {pk}"})
