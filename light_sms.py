import conf, time, json
from boltiot import Bolt, Sms
maximum_limit = 200
minimum_limit = 100
mybolt = Bolt(conf.API_KEY,conf.DEVICE_ID)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print(data['value'])
	try:
		sensor_value = int(data['value'])
		print(sensor_value)
		if sensor_value > maximum_limit or sensor_value < minimum_limit:
			response = sms.send_sms("Your light sensor value is " +str(sensor_value))
	except Exception as e:
		print("Error",e)
	time.sleep(10)
