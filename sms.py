from twilio.rest import Client
from twilioauth import *
from garrisonbdays import *


client = Client(account_sid, auth_token)
birthday_wish()


message = client.messages.create(
                              body=birthday_wish(),
                              from_='+12527729034',
                              to='+17608152442'
                          )

print(message.sid)