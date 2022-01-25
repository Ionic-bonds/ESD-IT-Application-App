from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/developer' #change/check db URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Developer(db.Model):
    __tablename__ = 'developer'

    Name = db.Column(db.String(64), primary_key=True)
    Phone = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(64))

    def __init__(self, Name, Phone, Address):
        self.Name = Name
        self.Phone = Phone
        self.Address = Address

    def json(self):
        return {"Name": self.Name, "Phone": self.Phone, "Address": self.Address}


@app.route("/developer") #change/check route (URL)
def get_all():
    devList = Developer.query.all()
    if len(devList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "developer": [developer.json() for developer in devList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no developers."
        }
    ), 404


@app.route("/developer/<string:Name>") #change/check route (URL)
def find_by_Name(Name):
    dev = Developer.query.filter_by(Name=Name).first()
    if dev:
        return jsonify(
            {
                "code": 200,
                "data": dev.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Developer not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
