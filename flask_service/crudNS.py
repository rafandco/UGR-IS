from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Información',
    description='Una API simple para gestionar información',
)

# Namespace para Información
info_ns = api.namespace('info', description='Operaciones de información')

info_model = info_ns.model('Info', {
    'id': fields.Integer(readOnly=True, description='Identificador único de la información'),
    'nombre': fields.String(required=True, description='Nombre de la información'),
})

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

@info_ns.route('/recuperar/<int:recurso_id>')
class RecuperarRecurso(Resource):
    @info_ns.marshal_with(info_model)
    def get(self, recurso_id):
        recurso = obtener_recurso_por_id(recurso_id)
        if recurso is not None:
            return recurso
        else:
            return {'error': 'Recurso no encontrado'}, 404

@info_ns.route('/crear')
class CrearRecurso(Resource):
    @info_ns.expect(info_model)
    @info_ns.marshal_with(info_model, code=201)
    def post(self):
        data = request.json
        nuevo_recurso = {'id': len(info) + 1, 'nombre': data['nombre']}
        info.append(nuevo_recurso)
        return nuevo_recurso, 201

@info_ns.route('/actualizar/<int:recurso_id>')
class ActualizarRecurso(Resource):
    @info_ns.expect(info_model)
    @info_ns.marshal_with(info_model)
    def put(self, recurso_id):
        data = request.json
        actualizado = actualizar_recurso_por_id(recurso_id, data)
        if actualizado:
            return data
        else:
            return {'error': 'Recurso no encontrado'}, 404

@info_ns.route('/eliminar/<int:recurso_id>')
class EliminarRecurso(Resource):
    def delete(self, recurso_id):
        eliminado = eliminar_recurso_por_id(recurso_id)
        if eliminado:
            return {'mensaje': 'Recurso eliminado correctamente'}
        else:
            return {'error': 'Recurso no encontrado'}, 404

if __name__ == '__main__':
    app.run(debug=True)