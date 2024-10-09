from flask import Flask, jsonify, request
from models.parents import Parents
from app import db

parents_blueprint = Blueprint("parents", __name__)

@parents_blueprint.routes("/parents", methods = ["POST"])
def add_parents():
    data = request.get_json()
    new_parent = Parents(
        student_id = data["student_id"],
        occupation = data["occupation"],
        education_level = data["education_level"],
        income_level = data["income_level"],
        digital_literacy = data["digital literacy"]
    )

    db.session.add(new_parent)
    db.session.commit()
    return jsonify({"message": "Parent data added succesfully"}), 201
