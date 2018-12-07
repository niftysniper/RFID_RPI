import RPi.GPIO as GPIO 
import SimpleMFRC522

import requests
import datetime

reader = SimpleMFRC522.SimpleMFRC522()
server = 'htpp://httpbin.org/post'
while True:

	try:
		ts = datetime.datetime.utcnow()
		UID, text = reader.read()
		print("UID found")
		print(UID)

		payload = {
			'UID' : UID,
			'timeStamp' : ts
		}

		r = requests.get(server, params = payload)
		print(r.url)
	
	finally:
		GPIO.cleanup()

