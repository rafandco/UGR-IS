from flask import Flask, request, jsonify
app = Flask(__name__)

info = [
    {'id': 1, 'nombre': 'Recurso 1'},
    {'id': 2, 'nombre': 'Recurso 2'},
    {'id': 3, 'nombre': 'Recurso 3'}
]

def obtener_recurso_por_id(recurso_id):
    for recurso in info:
        if recurso['id'] == int(recurso_id):
            return recurso
    return None

def actualizar_recurso_por_id(recurso_id, data):
    for recurso in info:
        if recurso['id'] == int(recurso_id):
            recurso['nombre'] = data['nombre']
            return True
    return False

def eliminar_recurso_por_id(recurso_id):
    for recurso in info:
        if recurso['id'] == int(recurso_id):    
            info.remove(recurso)
            return True
    return False
@app.route('/recuperar/<recurso_id>', methods=['GET'])
def obtener_recurso(recurso_id):
# Aquí puedes acceder al ID del recurso desde la URL
# Recupera el recurso con el ID proporcionado
    recurso = obtener_recurso_por_id(recurso_id)
    if recurso is not None:
# Devuelve el recurso encontrado, por ejemplo, en formato JSON
        return jsonify(recurso)
    else:
# Devuelve una respuesta de error si el recurso no se encuentra
        return jsonify({'error': 'Recurso no encontrado'}), 404

@app.route('/crear', methods=['POST'])
def crear_recurso():
    # Aquí puedes acceder a los datos enviados por el cliente a través de request
    data = request.json # Suponiendo que los datos se envían en formato JSON
    # Procesa los datos y crea el nuevo recurso
    info.append({'id': data['id'], 'nombre': data['nombre']})
    # Devuelve una respuesta adecuada, por ejemplo, un código 201 (Created)
    return jsonify({'mensaje': 'Recurso creado correctamente',
                    "data": data}), 201

@app.route('/actualizar/<recurso_id>', methods=['PUT'])
def actualizar_recurso(recurso_id):
    # Aquí puedes acceder al ID del recurso desde la URL
    # Accede a los datos enviados por el cliente a través de request
    data = request.json # Suponiendo que los datos se envían en formato JSON
    # Actualiza el recurso con el ID proporcionado
    actualizado = actualizar_recurso_por_id(recurso_id, data)
    if actualizado:
        return jsonify({'mensaje': 'Recurso actualizado correctamente'})
    else:
        return jsonify({'error': 'Recurso no encontrado'}), 404

@app.route('/eliminar/<recurso_id>', methods=['DELETE'])
def eliminar_recurso(recurso_id):
    # Aquí puedes acceder al ID del recurso desde la URL
    # Elimina el recurso con el ID proporcionado
    eliminado = eliminar_recurso_por_id(recurso_id)
    if eliminado:
        return jsonify({'mensaje': 'Recurso eliminado correctamente'})
    else:
        return jsonify({'error': 'Recurso no encontrado'}), 404
    
if __name__ == '__main__':
    app.run()