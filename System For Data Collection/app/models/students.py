from app import db

class Students(db.Model):
    __tablename__ = "students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    special_needs = db.Column(db.String(4), nullable = False)
