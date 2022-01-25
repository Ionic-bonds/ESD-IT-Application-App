# Complex microservice
import os, sys
from flask import Flask, jsonify, request, jsonify
from invokes import invoke_http
from flask_cors import CORS
from os import environ
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import requests
import amqp_setup
import pika

import json

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or  'mysql+mysqlconnector://root@localhost:3306/listing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

notification_URL = environ.get('notification_URL')  or "http://localhost:5101/notification"
listing_URL = environ.get('listing_URL') or 'http://localhost:5001/update_listing' 

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


@app.route("/notify_developer", methods=['POST'])
def notify_developer():
    if request.is_json:
        developer_name = request.json.get('dev_name', None)#from listingwebpage
        listing_id = request.json.get('listing_id',None)#from listingwebpage
        title = request.json.get('title',None)
        update_URL = listing_URL+'/'+developer_name+'/'+listing_id
        result = invoke_http(update_URL, method='POST') #update developer name in listing db

        #notify = invoke_http(notification_URL, method='GET')#############
        
        ## AMQP send request to notification microservice
        fire_and_forget = send_notification({'developer_name':developer_name, 'title':title})

        if result['code']: ##return response
            return result



def send_notification(body):
    message = json.dumps(body)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="notification_log",body=message)
 

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for making payment...")
    app.run(host='0.0.0.0', port=5100, debug=True)

# @app.route("/place_order", methods=['POST'])
# def notify_dev():
#     # Simple check of input format and data of the request are JSON
#     if request.is_json:
#         try:
#             order = request.get_json()
#             print("\nReceived a listing in JSON:", listing)

#             result = processNotifyDev(listing)
#             print('\n------------------------')
#             print('\nresult: ', result)
#             return jsonify(result), result["code"]
#         except:
#             pass


#     # if reached here, not a JSON request.
#     return jsonify({
#         "code": 400,
#         "message": "Invalid JSON input: " + str(request.get_data())
#     }), 400


# def processNotifyDev(listing):
#     # 2. Send the order info {cart items}
#     # Invoke the order microservice
#     print('\n-----Invoking listing microservice-----')
#     listing_result = invoke_http(notification_URL, method='POST', json=listing)
#     print('listing_result:', listing_result)
  
#     # Check the order result; if a failure, send it to the error microservice.
#     code = listing_result["code"]
#     message = json.dumps(listing_result)

#     # 4. Record new order
#     # record the activity log anyway
#     #print('\n\n-----Invoking activity_log microservice-----')
#     print('\n\n-----Publishing the (order info) message with routing_key=order.info-----')        

    

#     # 7. Return created order, shipping record
#     return {
#         "code": 201,
#         "data": {
#             "listing_result": listing_result,
#             "shipping_result": shipping_result
#         }
#     }

# def updateListing(listing):

#     print('\n-----Invoking listing microservice-----')
#     listing_result = invoke_http(listing_URL, method='POST', json=listing)
#     print('listing_result:', listing_result)

#     code = listing_result["code"]


# @app.route("/notify_dev", methods=['POST'])
# def get_notification():
#     if request.is_json:
#         try:
#             update_listing = request.get_json()
#             result = invoke_http(payment_URL,method='POST',json=payment_details)
#             try:
#                 if result['id']:
#                     print('hello')
#                     message = json.dumps(payment_details)
#                     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="payment.log",body=message)
#                     print(message)
#             except Exception as e:
#                 pass
#             return result
#         except Exception as e:
#             print('ERROR')






