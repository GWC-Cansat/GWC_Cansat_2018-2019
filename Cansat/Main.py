#Import needed modules
import os, sys, glob, threading, time

#Import module for communications
import comms

#Define lists
sensors = []
packetBuffer = []
threads = []
failed = []

#Puts the Sensors directory into the path
sys.path.append(os.path.abspath("Sensors/"))

#Get all sensors in the Sensors directory and import them
for sensorFile in glob.glob("Sensors/*.py"):
	#Get just the filename
	sensorFile = os.path.basename(sensorFile)
	
	#Remove the .py from the sensorFile
	sensorFile = sensorFile[:sensorFile.find(".py")]
	
	#Import the sensor and append to list of sensors
	sensor = __import__(sensorFile)
	sensors.append(sensor)

#Run test to make sure all sensors work
print("-="*10+"-")
print("     RUNNING TEST")
print("-="*10+"-")
for sensor in sensors:
	if sensor.sensor.test():
		print(sensor.sensor.name + " "*(15-len(sensor.sensor.name)) + "OK")
	else:
		print(sensor.sensor.name + " "*(15-len(sensor.sensor.name)) + "FAIL")
		failed.append(sensors.index(sensor))
print("-="*10+"-")

#Remove sensors that have failed test
for index in failed:
	del sensors[index]

#Confirm if they still want to continue in case of failed sensors
if(input("CONTINUE? Y/N:").lower() != "y" ):
	quit()

#Sensor thread worker
def worker(sensor):
	while True:
		#Get data from sensor
		data = sensor.data()
		
		#Pack the data with struct
		packet = str(data)
		
		#Put the packed data into a buffer for sending
		packetBuffer.append(packed)
		time.sleep(0.0025)

#Loop through the sensors and create a thread for each
for sensor in sensors:
	#Create the thread and give it a sensor as an argument
	thread = threading.Thread(target=worker, args=(sensor.sensor,))
	
	#Make it a daemon so it dies on ctrl+c
	thread.daemon = True
	
	#Put it in the list of threads
	threads.append(thread)
	
	#Start the thread
	thread.start()

#Send data to base-station
while True:
	try:
		data = packetBuffer.pop(0)
		comms.send(data)
	except:
		pass