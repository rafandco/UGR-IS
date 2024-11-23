from flask import Flask, request, jsonify
app = Flask(__name__)

tareas = [
    {'id': 1, 'nombre': 'Recoger habitación'},
    {'id': 2, 'nombre': 'Formatear PC'},
    {'id': 3, 'nombre': 'Hacer la compra'}
]

def obtener_tarea_por_id(tarea_id):
    for tarea in tareas:
        if tarea['id'] == int(tarea_id):
            return tarea
    return None

def actualizar_tarea_por_id(tarea_id, data):
    for tarea in tareas:
        if tarea['id'] == int(tarea_id):
            tarea['nombre'] = data['nombre']
            return True
    return False

def eliminar_tarea_por_id(tarea_id):
    for tarea in tareas:
        if tarea['id'] == int(tarea_id):    
            tareas.remove(tarea)
            return True
    return False

# Rutas para las acciones CRUD    
@app.route('/tareas/<tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    # Aquí puedes acceder al ID de la tarea desde la URL
    # Recupera la tarea con el ID proporcionado
    tarea = obtener_tarea_por_id(tarea_id)
    if tarea is not None:
    # Devuelve la tarea encontrado, por ejemplo, en formato JSON
        return jsonify(tarea)
    else:
    # Devuelve una respuesta de error si la tarea no se encuentra
        return jsonify({'error': 'Recurso no encontrado'}), 404

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    # Aquí puedes acceder a los datos enviados por el cliente a través de request
    data = request.json # Suponiendo que los datos se envían en formato JSON
    # Procesa los datos y crea el nuevo recurso
    tareas.append({'id': data['id'], 'nombre': data['nombre']})
    # Devuelve una respuesta adecuada, por ejemplo, un código 201 (Created)
    return jsonify({'mensaje': 'Tarea creada correctamente',
                    "data": data}), 201

@app.route('/tareas/<tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    # Aquí puedes acceder al ID de la tarea desde la URL
    # Accede a los datos enviados por el cliente a través de request
    data = request.json # Suponiendo que los datos se envían en formato JSON
    # Actualiza la tarea con el ID proporcionado
    actualizado = actualizar_tarea_por_id(tarea_id, data)
    if actualizado:
        return jsonify({'mensaje': 'Tarea actualizada correctamente'})
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404

@app.route('/tareas/<tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    # Aquí puedes acceder al ID de la tarea desde la URL
    # Elimina la tarea con el ID proporcionado
    eliminado = eliminar_tarea_por_id(tarea_id)
    if eliminado:
        return jsonify({'mensaje': 'Tarea eliminada correctamente'})
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
if __name__ == '__main__':
    app.run()