from twilio.rest import Client
 
account_sid = 'ACa08b15886b9eb363f2c61279fe0da394' 
auth_token = '9aa9d1cc6f7fd7564af6b650a8db1cf2' 
client = Client(account_sid, auth_token) 
 

message = client.messages.create( 
                              from_='+12058593998',
                              body='This is a python sms',        
                              to='+919285276039' 
                          ) 
 
print(message.sid)
print(message.account_sid)
print(message.subresource_uris.media)
print("Succesfull")