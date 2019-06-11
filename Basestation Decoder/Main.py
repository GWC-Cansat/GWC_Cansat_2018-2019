import decoder, serial

#InfluxDB connection
from influxdb import InfluxDBClient

client = InfluxDBClient("localhost", 8086)
client.switch_database("data")

#HC-12
#s = serial.Serial("/dev/ttyUSB0")
oof = open("data_rev", "r").readlines()

#while True:
for x in oof:
	#Get the data
	data = decoder.decode(x)

	#If it couldn't be decoded ignore it
	if data == -1:
		continue

	#BME680
	if data[0] == "B":
		try:
			print("BME680", data[1].temp, data[1].pres/68.9476, data[1].hum)
			values = {"temp": data[1].temp, "pres": data[1].pres, "hum": data[1].hum}
			client.write_points([{"measurement": "bme", "fields": values}])
		except:
			pass

	elif data[0] == "G" and data[1] != (0.0, 0.0):
		try:
			print("GPS", data[1])
			values = {"latitude": float(data[1][0]), "longitude": float(data[1][1])}
			client.write_points([{"measurement": "gps", "fields": values}])
		except:
			pass

	elif data[0] == "D":
		try:
			print("9DOF", data[1])
			values = {"a1":data[1][0][0], "a2":data[1][0][1], "a3":data[1][0][2], "m1":data[1][1][0], "m2":data[1][1][1], "m3":data[1][1][2], "g1":data[1][2][0], "g2":data[1][2][1], "g3":data[1][2][2]}
			client.write_points([{"measurement": "9dof", "fields": values}])
		except:
			pass
