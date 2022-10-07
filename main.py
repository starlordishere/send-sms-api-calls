from flask import render_template,flash,request,redirect
import time
from app import app
from twi import create_message
# default page
@app.route('/')
def send_message():
  return render_template('sendmessage.html')
# 
@app.route('/sendmessage', methods=['GET'])
def successfull_message():
  message="Message sent successfully"
  if request.method == 'GET':
    # This function sends the message
      create_message()
    # flash the message
      flash(message)
    #delay the time by 3 seconds
      time.sleep(3)
  return redirect('/')
app.run(host='0.0.0.0', port=8080)
