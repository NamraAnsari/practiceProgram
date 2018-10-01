import email_conf, json, time
from boltiot import Email, Bolt
minimum_limit = 300
maximum_limit = 600
mybolt = Bolt(email_conf.API_KEY,email_conf.DEVICE_ID)
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)
while True:
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print(data['value'])
	try:
		sensor_value = int(data['value'])
		temperature = (sensor_value*100)/1024
		print(temperature)
		if sensor_value > maximum_limit or sensor_value < minimum_limit:
			response = mailer.send_email("Alert!", "The Current temperature sensor value is " +str(temperature))
	except Exception as e:
		print("Error",e)
	time.sleep(10)

