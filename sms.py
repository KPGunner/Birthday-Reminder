from twilio.rest import Client
from twilioauth import *
from garrisonbdays import *


client = Client(account_sid, auth_token)
birthday_wish()


message = client.messages.create(
                              body=birthday_wish(),
                              from_='+11234567890',
                              to='+1098765432'
                          )

print(message.sid)
