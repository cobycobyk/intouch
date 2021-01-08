import os
from twilio.rest import Client 
import environ
environ.Env()
environ.Env.read_env()

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)
message = client.messages.create(
  to='+13035212561',
  from_='+14693789344',
  body='hello'
  )
print(message.sid) 