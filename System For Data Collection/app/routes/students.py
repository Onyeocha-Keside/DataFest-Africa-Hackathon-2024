from flask import jsonify, request, Blueprint
from models.students import Students
from app import db

students_blueprint = Blueprint("students", __name__)

@students_blueprint.route("/students", methods = ["POST"])
def add_student():
    data = request.get_json()
    new_student = Students(
        name=data["name"],
        age=data["age"], 
        gender=data["gender"], 
        special_needs = data["special_needs"]
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "student has been recorded successfully"}), 201

