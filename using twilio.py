# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = 'I removed this'
auth_token = 'I removed this too'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='i\'ll just give up on this thing abeg',
    from_='+19136756299',
    to='+2349017741269'
)

print(message.sid)
