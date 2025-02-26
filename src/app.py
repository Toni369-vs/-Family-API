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

# ENDPOINT PARA VER TODOS MIEMBRO

@app.route('/members', methods=['GET'])
def getAllMembers():
    members = jackson_family.get_all_members()
    if members:
        return jsonify(members), 200
    else:
        return jsonify("Ha ocurrido un error"), 400


 # ENDPOINT PARA VER UN MIEMBRO
@app.route("/member/<int:id>", methods=["GET"])
def getOneMember(id):
    member = jackson_family.get_member(id)

    if member == "No existe miembro":
        return jsonify("Ha ocurrido un error"), 400

    return jsonify(member), 200

# ENDPOINT PARA AGREGAR UN MIEMBRO
@app.route('/member', methods=['POST'])
def addMember():
 
    member = {
        "id": request.json.get("id"),
        "first_name": request.json.get("first_name"),
        "age": request.json.get("age"),
        "lucky_numbers": request.json.get("lucky_numbers")
    }

    response = jackson_family.add_member(member)
    if (response == True):
        return jsonify("Usuario creado"), 200
    else:
        return jsonify("Ocurrió un error al agregar el miembro de la familia"), 400


# ENDPOINT PARA ELIMINAR UN MIEMBRO
@app.route('/member/<int:id>', methods=['DELETE'])
def deleteOneMember(id):
    estado = jackson_family.delete_member(id)

    if estado == True:
        return jsonify({"done": True}), 200
    else:
        return jsonify("Ocurrió un error al eliminar el miembro"), 400



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=PORT, debug=True)