from app import db

class Academics(db.Models):
    __tablename__ = "academics"
    parent_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.Foreign_key("students.student_id"))
    class_level = db.Column(db.String(10), nullable = False)
    midterm_score = db.Column(db.Float, nullable = False)
    exam_score = db.Column(db.Float, nullable = False)
    improvments = db.Column(db.String, nullable = False)
    jamb_mock_score = db.Column(db.Integer)
    weak_subjects = db.Column(db.String, nullable = False)