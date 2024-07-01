from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://master:master1234@localhost/pdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    radius = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)

    def __init__(self, name, distance, radius, mass):
        self.name = name
        self.distance = distance
        self.radius = radius
        self.mass = mass

@app.route("/")
def index():
    planets = Planet.query.all()
    return render_template('index.html', planets=planets)

if __name__ == "__main__":
    app.run(debug=True)
