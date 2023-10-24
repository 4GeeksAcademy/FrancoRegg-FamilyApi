"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

##### Obtiene todos los miembros de la familia #####
@app.route('/members', methods=['GET'])
def handle_hello():
     # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200

##### Eliminar un miembro #####
@app.route('/member/<int:member_id>', methods = ['DELETE'])
def delete_member_id(member_id):
    member = jackson_family.delete_member(member_id)
        
    return jsonify(member),200

##### Obtener un miembro de la familia ##### 
@app.route('/member/<int:id>', methods=['GET'])
def get_member_id(id):
    member = jackson_family.get_member(id)
    
    return jsonify(member), 200

##### Añadir nuevo miembro #####
@app.route('/member', methods=['POST'])
def add_a_member():
    body = request.get_json(silent=True)   
    if body is None:
        return jsonify({'msg':'Debes enviar informacion en body'}), 400
    if 'first_name' not in body:
        return jsonify({'msg':'El campo first name es requerido'}), 400
    if 'age' not in body:
        return jsonify({'msg':'El campo age es requerido'}), 400
    if 'lucky_numbers' not in body:
        return jsonify({'msg':'El campo lucky numbers es requerido'}), 400
    
    #id_member = jackson_family._generateId()
    #if id_member in body:
    #    id_member = body['id_member']

    new_member = {'id': body['id'], 'first_name': body['first_name'], 'last_name': jackson_family.last_name, 'age': body['age'], 'lucky_numbers': body['lucky_numbers']}
    jackson_family.add_member(new_member)

    return jsonify({'new_member': new_member}), 200
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
