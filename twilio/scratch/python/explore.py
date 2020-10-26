from twilio.rest import Client
 
account_sid = 'ACa08b15886b9eb363f2c61279fe0da394' 
auth_token = '9aa9d1cc6f7fd7564af6b650a8db1cf2' 
client = Client(account_sid, auth_token) 
 

for msg in client.messages.list():
	print(f"deleting {msg.body}")
	msg.delete()

# msg = client.messages.create(
# 		to= "+919285276039",
# 		from_ = "+12058593998",
# 		body = "hello from python",

# 	)

# print("Created a new message: " + msg.sid)