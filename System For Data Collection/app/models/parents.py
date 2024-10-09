from app import db

class Parents(db.Model):
    __tablename__ = "parents"
    parent_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.Foreign_key("students.student_id"))
    occupation = db.Column(db.String(30), nullable = False)
    education_level = db.Column(db.String(30), nullable = False)
    income_level = db.Column(db.String(30), nullable = False)
    digital_literacy = db.Column(db.String(5))
    