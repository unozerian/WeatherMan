import json
import matplotlib.pyplot as plt

file = open("temp.txt","r")
data = file.readlines()
humx = []
humy = []
tempx = []
tempy = []
for i in range(len(data)):
	humy.append((json.loads(data[i])).get("hum"))
	tempy.append((json.loads(data[i])).get("temp"))

for i in range(1,3044):
	humx.append(i)
	tempx.append(i)
	
plt.plot(humx, humy)
plt.title('Humidity & Temperature(5AM - 5PM)')
plt.xlabel('Time')
plt.ylabel('Humidity, Temperature')

plt.plot(tempx, tempy)
plt.xlabel('Time')
plt.legend(['Humidity', 'Temperature'], loc=4)
plt.show()
