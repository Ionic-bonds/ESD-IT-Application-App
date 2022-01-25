import os
from os import environ
from flask_sqlalchemy import SQLAlchemy


from twilio.rest import Client
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS, cross_origin

import json
import pika
import amqp_setup

monitorBindingKey='#'

def receiveNotificationLog():
    amqp_setup.check_setup()
        
    queue_name = 'Notification_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.
    
def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived Notification log by " + __file__)
    processNotificationLog(json.loads(body))

    print() # print a new line feed

def processNotificationLog(message):
    print("Recording a Notification log:")
    print("Congratulations "+message['developer_name']+", your interest for job: "+message['title']+' has been accepted!')
    # Your Account SID from twilio.com/console
    account_sid = "AC95908466a608c45e160f10a3ae48d05d"
    # Your Auth Token from twilio.com/console
    auth_token  = "afeaf9bf58b01a785f51a5a39be5d04d"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+6597123748", 
        from_="+18322415377",
        body= "Congratulations "+message['developer_name']+", your interest for job: "+message['title']+' has been accepted!')


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveNotificationLog()