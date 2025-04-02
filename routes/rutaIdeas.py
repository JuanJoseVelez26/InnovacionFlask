from flask import Blueprint, request, jsonify, render_template

ideas_bp = Blueprint('ideas', __name__, url_prefix='/ideas')

@ideas_bp.route('/list/')
def list_ideas():
    return jsonify({"message": "Listado de ideas"})

@ideas_bp.route('/create/', methods=['GET', 'POST'])
def create_idea():
    if request.method == 'POST':
        return jsonify({"message": "Idea creada"})
    return render_template('create_idea.html')

@ideas_bp.route('/update/<int:pk>/', methods=['GET', 'POST'])
def update_idea(pk):
    return jsonify({"message": f"Idea {pk} actualizada"})

@ideas_bp.route('/delete/<int:pk>/', methods=['POST'])
def delete_idea(pk):
    return jsonify({"message": f"Idea {pk} eliminada"})

@ideas_bp.route('/detail/<int:codigo_idea>/')
def detail_idea(codigo_idea):
    return jsonify({"message": f"Detalle de la idea {codigo_idea}"})

@ideas_bp.route('/confirmar/<int:codigo_idea>/')
def confirmar_idea(codigo_idea):
    return jsonify({"message": f"Idea {codigo_idea} confirmada"})
