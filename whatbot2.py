from flask import Flask
from flask import request
#from flask import *
#from requests import *
from twilio.twiml.messaging_response import MessagingResponse
import Batch_O2
from apscheduler.schedulers.blocking import BlockingScheduler
import time


app = Flask(__name__)
 

 
@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    
    msg = request.form.get('Body').lower() # Reading the message from the whatsapp
 
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()


    # Create reply
    if msg.lower() == "hi":
      reply.body('''Hello mate! Tell me which day you want to know the schedule for. 
      Just write the day and time (for example, Monday 1015) and you are good to go.
      ''')
    
    elif msg.lower() == "monday 8":
      reply.body(Batch_O2.mon800())
    elif msg.lower() == "monday 9":
      reply.body(Batch_O2.mon900())
    elif msg.lower() == "monday 1015":
      reply.body(Batch_O2.mon1015())
    elif msg.lower() == "monday 1115":
      reply.body(Batch_O2.mon1115())
    elif msg.lower() == "monday 115":
      reply.body(Batch_O2.mon115())
    elif msg.lower() == "monday 215":
      reply.body(Batch_O2.mon215())
    elif msg.lower() == "monday 330":
      reply.body(Batch_O2.mon330())
    elif msg.lower() == "monday 430":
      reply.body(Batch_O2.mon430())
    elif msg.lower() == "monday 530":
      reply.body(Batch_O2.mon530())

    elif msg.lower() == "tuesday 8":
      reply.body(Batch_O2.tues800())
    elif msg.lower() == "tuesday 9":
      reply.body(Batch_O2.tues900())
    elif msg.lower() == "tuesday 1015":
      reply.body(Batch_O2.tues1015())
    elif msg.lower() == "tuesday 1115":
      reply.body(Batch_O2.tues1115())
    elif msg.lower() == "tuesday 115":
      reply.body(Batch_O2.tues115())
    elif msg.lower() == "tuesday 215":
      reply.body(Batch_O2.tues215())
    elif msg.lower() == "tuesday 330":
      reply.body(Batch_O2.tues330())
    elif msg.lower() == "tuesday 430":
      reply.body(Batch_O2.tues430())
    elif msg.lower() == "tuesday 530":
      reply.body(Batch_O2.tues530())

    elif msg.lower() == "wednesday 8":
      reply.body(Batch_O2.wed800())
    elif msg.lower() == "wednesday 9":
      reply.body(Batch_O2.wed900())
    elif msg.lower() == "wednesday 1015":
      reply.body(Batch_O2.wed1015())
    elif msg.lower() == "wednesday 1115":
      reply.body(Batch_O2.mon1115())
    elif msg.lower() == "wednesday 115":
      reply.body(Batch_O2.wed115())
    elif msg.lower() == "wednesday 215":
      reply.body(Batch_O2.wed215())
    elif msg.lower() == "wednesday 330":
      reply.body(Batch_O2.wed330())
    elif msg.lower() == "wednesday 430":
      reply.body(Batch_O2.wed430())
    elif msg.lower() == "wednesday 530":
      reply.body(Batch_O2.wed530())

    elif msg.lower() == "thursday 8":
      reply.body(Batch_O2.thurs800())
    elif msg.lower() == "thursday 9":
      reply.body(Batch_O2.thurs900())
    elif msg.lower() == "thursday 1015":
      reply.body(Batch_O2.mon1015())
    elif msg.lower() == "thursday 1115":
      reply.body(Batch_O2.thurs1115())
    elif msg.lower() == "thursday 115":
      reply.body(Batch_O2.thurs115())
    elif msg.lower() == "thursday 215":
      reply.body(Batch_O2.thurs215())
    elif msg.lower() == "thursday 330":
      reply.body(Batch_O2.thurs330())
    elif msg.lower() == "thursday 430":
      reply.body(Batch_O2.thurs430())
    elif msg.lower() == "thursday 530":
      reply.body(Batch_O2.thurs530())

    elif msg.lower() == "friday 8":
      reply.body(Batch_O2.fri800())
    elif msg.lower() == "friday 9":
      reply.body(Batch_O2.fri900())
    elif msg.lower() == "friday 1015":
      reply.body(Batch_O2.fri1015())
    elif msg.lower() == "friday 1115":
      reply.body(Batch_O2.fri1115())
    elif msg.lower() == "friday 115":
      reply.body(Batch_O2.fri115())
    elif msg.lower() == "friday 215":
      reply.body(Batch_O2.fri215())
    elif msg.lower() == "friday 330":
      reply.body(Batch_O2.fri330())
    elif msg.lower() == "friday 430":
      reply.body(Batch_O2.fri430())
    elif msg.lower() == "friday 530":
      reply.body(Batch_O2.fri530())

    elif msg.lower() == "saturday 8":
      reply.body(Batch_O2.sat800())
    elif msg.lower() == "saturday 9":
      reply.body(Batch_O2.sat900())
    elif msg.lower() == "saturday 1015":
      reply.body(Batch_O2.sat1015())
    elif msg.lower() == "saturday 1115":
      reply.body(Batch_O2.sat1115())
    elif msg.lower() == "saturday 115":
      reply.body(Batch_O2.sat115())
    elif msg.lower() == "saturday 215":
      reply.body(Batch_O2.sat215())
    elif msg.lower() == "saturday 330":
      reply.body(Batch_O2.sat330())
    elif msg.lower() == "saturday 430":
      reply.body(Batch_O2.sat430())
    elif msg.lower() == "saturday 530":
      reply.body(Batch_O2.sat530())


    elif msg.lower() == "timetable":
      reply.body("https://drive.google.com/file/d/1ukqjfYCcshf1pbTEOPCCfpd6Q_hUKzkw/view?usp=share_link")
    
    else:
        reply.body(".")


    return str(resp)


    
if __name__ == "__main__":	
   app.run(debug=True)