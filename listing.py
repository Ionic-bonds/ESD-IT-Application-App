#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/listing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Listing(db.Model):
    __tablename__ = 'listing'

    ListingID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(255), nullable=True)
    DateTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    Title = db.Column(db.VARCHAR(255), nullable=False)
    ProgrammingLanguage = db.Column(db.VARCHAR(255), nullable=False)
    ListingDescription = db.Column(db.VARCHAR(255), nullable=False)
    Status = db.Column(db.VARCHAR(255), nullable=False ,default='Open')
    Price = db.Column(db.DECIMAL(asdecimal=False), nullable=False)

 

    def json(self):
        return {'ListingID': self.ListingID, 'Name': self.Name, 'DateTime': self.DateTime, 'Title': self.Title, 'ProgrammingLanguage': self.ProgrammingLanguage,'ListingDescription': self.ListingDescription, 'Status': self.Status,'Price': self.Price}



@app.route("/listing") #change/check route (URL)
def get_all():
    listings = Listing.query.all()
    if len(listings):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "listings": [listing.json() for listing in listings]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no listings."
        }
    ), 404


@app.route("/listing/<string:Title>") #change/check route (URL)
def find_by_title(Title):
    listing = Listing.query.filter_by(Title=Title).first()
    if listing:
        return jsonify(
            {
                "code": 200,
                "data": listing.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Listing not found."
        }
    ), 404


@app.route("/listing", methods=['POST']) #change/check route (URL)
def create_listing():
    Title = request.json.get('Title')
    ProgrammingLanguage = request.json.get('ProgrammingLanguage')
    ListingDescription = request.json.get('ListingDescription')
    Price = request.json.get('Price')
    print(Price)
    listing = Listing(Title=Title, ProgrammingLanguage=ProgrammingLanguage, ListingDescription=ListingDescription, Price=Price)

    try:
        db.session.add(listing)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the listing. " + str(e)
            }
        ), 500
    
    #print(json.dumps(listing.json(), default=str)) # convert a JSON object to a string and print
    #print()

    return jsonify(
        {
            "code": 201,
            "data": listing.json()
        }
    ), 201


# @app.route("/listing/<string:Title>", methods=['PUT']) #change/check route (URL)
# def update_listing(Title):
#     listing = Listing.query.filter_by(Title=Title).first()
#     if listing:
#         data = request.get_json()
#         if data['Name']:
#             listing.Name = data['Name']
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": listing.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "Title": Title
#             },
#             "message": "Listing not found."
#         }
#     ), 404

#update listing with developer name after employer accept interest
@app.route('/update_listing/<string:developer_name>/<int:listing_id>', methods=['POST'])
def update_listing(developer_name,listing_id):
    listing = Listing.query.filter_by(ListingID=listing_id).first()
    if listing:
        listing.Name = developer_name
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": listing.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "listing_id": listing_id
            },
            "message": "Listing not found."
        }
    ), 404


#update listing status as paid after payment is complete
@app.route('/update_status/<string:listing_id>', methods=['POST'])
def update_status(listing_id):
    print(listing_id)
    listing = Listing.query.filter_by(ListingID=listing_id).first()
    if listing:
        listing.Status = 'Paid'
        print(listing.Status)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": listing.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "listing_id": listing_id
            },
            "message": "Listing not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
