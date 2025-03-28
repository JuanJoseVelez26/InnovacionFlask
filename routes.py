from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Authentication Routes ---
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/app/')
def app_view():
    return render_template('app.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/notificaciones/marcar_leida/', methods=['POST'])
def marcar_leida():
    return jsonify({"message": "Notificación marcada como leída"})

@app.route('/notificaciones/eliminar/', methods=['POST'])
def eliminar_notificacion():
    return jsonify({"message": "Notificación eliminada"})

@app.route('/proyectos/')
def listar_proyectos():
    return jsonify({"message": "Listado de proyectos"})

# --- Ideas Routes ---
@app.route('/ideas/list/')
def list_ideas():
    return jsonify({"message": "Listado de ideas"})

@app.route('/ideas/create/', methods=['GET', 'POST'])
def create_idea():
    if request.method == 'POST':
        return jsonify({"message": "Idea creada"})
    return render_template('create_idea.html')

@app.route('/ideas/update/<int:pk>/', methods=['GET', 'POST'])
def update_idea(pk):
    return jsonify({"message": f"Idea {pk} actualizada"})

@app.route('/ideas/delete/<int:pk>/', methods=['POST'])
def delete_idea(pk):
    return jsonify({"message": f"Idea {pk} eliminada"})

@app.route('/ideas/detail/<int:codigo_idea>/')
def detail_idea(codigo_idea):
    return jsonify({"message": f"Detalle de la idea {codigo_idea}"})

@app.route('/ideas/confirmar/<int:codigo_idea>/')
def confirmar_idea(codigo_idea):
    return jsonify({"message": f"Idea {codigo_idea} confirmada"})

# --- Oportunidades Routes ---
@app.route('/oportunidades/list/')
def list_oportunidades():
    return jsonify({"message": "Listado de oportunidades"})

@app.route('/oportunidades/create/', methods=['POST'])
def create_oportunidad():
    return jsonify({"message": "Oportunidad creada"})

@app.route('/oportunidades/update/<int:pk>/', methods=['POST'])
def update_oportunidad(pk):
    return jsonify({"message": f"Oportunidad {pk} actualizada"})

@app.route('/oportunidades/delete/<int:pk>/', methods=['POST'])
def delete_oportunidad(pk):
    return jsonify({"message": f"Oportunidad {pk} eliminada"})

@app.route('/oportunidades/detail/<int:pk>/')
def detail_oportunidad(pk):
    return jsonify({"message": f"Detalle de la oportunidad {pk}"})

# --- Soluciones Routes ---
@app.route('/soluciones/list/')
def list_soluciones():
    return jsonify({"message": "Listado de soluciones"})

@app.route('/soluciones/create/', methods=['POST'])
def create_solucion():
    return jsonify({"message": "Solución creada"})

@app.route('/soluciones/update/<int:pk>/', methods=['POST'])
def update_solucion(pk):
    return jsonify({"message": f"Solución {pk} actualizada"})

@app.route('/soluciones/delete/<int:pk>/', methods=['POST'])
def delete_solucion(pk):
    return jsonify({"message": f"Solución {pk} eliminada"})

@app.route('/soluciones/detail/<int:pk>/')
def detail_solucion(pk):
    return jsonify({"message": f"Detalle de la solución {pk}"})

# --- Perfil Routes ---
@app.route('/perfil/')
def perfil():
    return jsonify({"message": "Perfil del usuario"})

@app.route('/perfil/update/', methods=['POST'])
def update_perfil():
    return jsonify({"message": "Perfil actualizado"})

@app.route('/perfil/delete/', methods=['POST'])
def delete_perfil():
    return jsonify({"message": "Perfil eliminado"})

# --- Configurar la ejecución de la aplicación ---
if __name__ == "__main__":
    app.run(debug=True)
