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
app.register_blueprints(students_blueprint)
app.register_blueprints(academics_blueprint)
app.register_blueprints(curricular_blueprint)
app.register_blueprints(parents_blueprint)
app.register_blueprints(resource_blueprint)

if __name__ == "__main__":
    app.run(debug = True)