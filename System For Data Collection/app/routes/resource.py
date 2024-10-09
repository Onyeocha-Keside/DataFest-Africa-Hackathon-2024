from flask import Flask, request, jsonify
from models.resources import Resources
from app import db

resource_blueprint = Blueprint("resources", __name__)
@resource_blueprint.route("/resources", methods = ["POST"])
def get_resources():
    data = request.get_json()
    resorces = Resources(
        library_usage_freq = data["library_usage_freq"],
        computer_usage_freq = data["computer_usage_freq"],
        learning_material_access = data["learning_material_accesss"]
    )

    db.session.add(resorces)
    db.commit()

    return jsonify({"message": "Resource allocation data collected successfully"})