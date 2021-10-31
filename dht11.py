from machine import Pin
from time import sleep
import ujson
import dht 

sensor = dht.DHT11(Pin(14))
# THis function will collect the details from the sensor and add it to the data text file
def temp_func():
	while True:
		try:
			sleep(10)
			sensor.measure()
			temp = sensor.temperature()
			hum = sensor.humidity()
			print('Temperature: %.2f C' %temp)
			print('Humidity: %.2f ' %hum)
			d = {"temp":temp, "hum":hum}
			file = open("data.txt","a")
			ujson.dump(d, file)
			file.write("\n")
			file.close()
		except OSError as e:
			print('Failed to read sensor.')

