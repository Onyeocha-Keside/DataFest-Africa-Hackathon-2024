from app import db

class Resources(db.Models):
    __tablename__ = "reesources"
    resource_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.Foreign_key("students.student_id"))
    library_usage_freq = db.Column(db.String, nullable = True)
    computer_usage_freq = db.Column(db.String, nullable = True)
    learning_material_access = db.Column(db.String, nullable = True)