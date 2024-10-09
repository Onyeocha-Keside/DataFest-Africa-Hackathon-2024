from flask import Flask, jsonify, request
from models.academics import Academics
from app import db

academics_blueprint = Blueprint("academics", __name__)

@academics_blueprint.route("/academics", methods = ["POST"])

def get_academics():
    data = request.get_json()
    academics = Academics(
        class_level = data["class_level"],
        midterm_score = data["midterm_score"],
        exam_score = data["exam_score"],
        improvments = data["improvments"],
        jamb_mock_score = data["jamb_mock_score"],
        weak_subjects = data["weak_subjects"]
    )

    db.session.add(academics)
    db.session.commit()

    return jsonify({"message": "parents data recorded successfully"}), 201
