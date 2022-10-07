import os
from twilio.rest import Client
import json
from getapi import create_message
def connecttwi():
  auth_token = os.environ['auth']
  account_sid = os.environ['sid']
  client = Client(account_sid, auth_token)
  messagebody=create_message()
  message = client.messages.create(
                       body=messagebody,
                       from_='+16477850248',
                       to='+16477850248'
                   )

  print(message.body)
  # Write message to json output file
  with open('outputfile.json', 'r') as output:
    json.dump(messagebody,output, indent=2)
  output.close()

