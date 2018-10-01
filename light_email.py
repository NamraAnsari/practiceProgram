import json, time, email_conf
from boltiot import Bolt, Email
min_limit = 1
max_limit = 3
mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
e_mail = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)
while True:
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	try:
		sensor_value = int(data['value'])
		print(sensor_value)
		if sensor_value > max_limit or sensor_value < min_limit:
			response = e_mail.send_email("Attention!","Your light sensor value is " +str(sensor_value))
	except Exception as e:
		print("Error!",e)
	time.sleep(10)
