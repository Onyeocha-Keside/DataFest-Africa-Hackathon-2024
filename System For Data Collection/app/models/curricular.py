from app import db

class Curricular(db.Models):
    __tablename__ = "curriculars"
    curricular_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.Foreign_key("students.student_id"))
    activity = db.Column(db.String, nullable = True)
    curricular_studey_per_week = db.Column(db.Integer, nullable = True)
    leadership_role = db.Column(db.String(5), nullable = True)