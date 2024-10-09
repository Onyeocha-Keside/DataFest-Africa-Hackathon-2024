from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.students import students_blueprint
from routes.academics import academics_blueprint
from routes.curricular import curricular_blueprint
from routes.parents import parents_blueprint
from routes.resource import resource_blueprint

app = Flask(__name__)

app.config.from_object("config.Config")

#initialize database
db = SQLAlchemy(app)

#register blueprints for different routes
app.register_blueprint(students_blueprint)
app.register_blueprint(academics_blueprint)
app.register_blueprint(curricular_blueprint)
app.register_blueprint(parents_blueprint)
app.register_blueprint(resource_blueprint)

if __name__ == "__main__":
    app.run(debug = True)