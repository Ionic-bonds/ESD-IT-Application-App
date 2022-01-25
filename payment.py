import os
from os import environ
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime

import stripe
# This is your real test secret API key.
stripe.api_key = 'sk_test_51IYQWqCCMJF8A5myTSc4kZJ6yUep8nFA0gFf7FvQxfFQqpIHGxFnQpUYNfhTokkIR0kKRPJJn4WDqWheqO4DpTrw00TW8IzxfE'

app = Flask(__name__,
            static_url_path='',
            static_folder='.')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or  'mysql+mysqlconnector://root@localhost:3306/payment_log'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

YOUR_DOMAIN = 'http://localhost/Final_bryan_120421' #CHANGE TO YOUR OWN LINK

class payment_log(db.Model):
    __tablename__ = 'payment_log'

    payment_log_id = db.Column(db.Integer, primary_key=True)
    developer_name = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False,
                         default=datetime.now, onupdate=datetime.now)

    def json(self):
        dto = {
            'payment_log_id': self.payment_log_id,
            'developer_name': self.developer_name,
            'name': self.name,
            'price': self.price,
            'time': self.datetime
        }
        return dto


@app.route("/make-payment", methods=['POST'])
def make_payment():
    if request.is_json:
        payment_details = request.get_json()
        print(payment_details['name'])
        price = int(payment_details['price'])
        listingID = payment_details['listingID']
        try:
            checkout_session = stripe.checkout.Session.create(
                customer_email= payment_details['customer_email'],
                submit_type='pay',
                billing_address_collection='auto',
                shipping_address_collection={
                'allowed_countries': ['US', 'CA'],
                },
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'sgd',
                            'unit_amount': price*100,
                            'product_data': {
                                'name': payment_details['name'],
                                'images': [],
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html?'+'listingID='+listingID,
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )
            if checkout_session.id: #write to payment_log db
                    Payment_log = payment_log(developer_name = payment_details['developer_id'], name = payment_details['name'], price = payment_details['price'])
                    try:
                        db.session.add(Payment_log)
                        db.session.commit()
                    except Exception as e:
                        return jsonify(
                            {
                                "code": 500,
                                "message": "An error occurred while creating the order. "
                            }
                        ), 500
            return jsonify({'id': checkout_session.id})
        except Exception as e:
            return jsonify(error="unable to retrieve session id"), 403
       
#display transaction history
@app.route("/", methods=['GET'])
def get_transaction_history():
    history = payment_log.query.all()
    if len(history):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "transactions": [record.json() for record in history]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no history."
        }
    ), 404



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for making payment...")
    app.run(host='0.0.0.0',port=4241, debug=True)