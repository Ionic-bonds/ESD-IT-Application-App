from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/interest' #change/check db URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Interest(db.Model):
    __tablename__ = 'interest'

    IntID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(64), nullable=False)
    Name = db.Column(db.String(64), nullable=False)
    ListingID = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(64), default='Open')

    

    def json(self):
        return {"IntID": self.IntID, "Title": self.Title, "Name": self.Name, "ListingID": self.ListingID, "Status": self.Status}


@app.route("/interest") #change/check route (URL)
def get_all():
    intList = Interest.query.all()
    if len(intList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "interest": [interest.json() for interest in intList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no interest logs."
        }
    ), 404


@app.route("/interest", methods=['POST']) #change/check route (URL)
def create_interest():
    Title = request.json.get('Title')
    ListingID = request.json.get('ListingID')
    Name = request.json.get('Name')
    interest = Interest(Title=Title, ListingID=ListingID, Name=Name)

    try:
        db.session.add(interest)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the interest. "
            }
        ), 500
    
    #print(json.dumps(interest.json(), default=str)) # convert a JSON object to a string and print
    #print()

    return jsonify(
        {
            "code": 201,
            "data": interest.json()
        }
    ), 201

@app.route('/interest/<string:listing_id>', methods=['POST'])
def update_status(listing_id):
    print(listing_id)
    interests = Interest.query.filter_by(ListingID=listing_id).all()
    print(interests)
    for interest in interests:
        print(interest)
        interest.Status = 'Closed'
        print(interest.Status)
    db.session.commit()
    return jsonify(
        {
            "code": 200,
            "data": interest.json()
        }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "listing_id": listing_id
            },
            "message": "Interest not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
