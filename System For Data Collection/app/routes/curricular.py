from flask import Flask, request, jsonify
from app import db
from models.curricular import Curricular

curricular_blueprint = Blueprint("curricular", __name__)

@curricular_blueprint.route("/curricular", methods = ["POST"])
def get_curricular():
    data = request.get_json()
    curricular = Curricular(
        activity = data["activity"],
        activity_hour_per_day = data["activity_hour_per_day"],
        leadership_role = data["leadership_role"]
    )

    db.session.add(curricular)
    db.session.commit()

    return jsonify({"message": "curricular data successfully stored"}), 201