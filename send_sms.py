import os
from twilio.rest import Client 

account_sid = "AC292d2c9173bcaf7f3c8af14b009f672d"
auth_token = "ba02dd39685a6775efaec15e692235c5"
client = Client(account_sid, auth_token)
message = client.messages.create(
  to='+13035212561',
  from_='+14693789344',
  body='hello'
  )
print(message.sid)