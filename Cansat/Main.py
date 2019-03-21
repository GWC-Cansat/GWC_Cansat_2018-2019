#Import needed modules
import os, sys, glob, threading, time

#Import module for communications
import comms

#Define lists
sensors = []
packetBuffer = []
threads = []

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

#Sensor thread worker
def worker(sensor):
	while True:
		#Get data from sensor
		data = sensor.data()
		
		#Pack the data with struct
		packet = str(sensor.id) + str(data)
		
		#Put the packed data into a buffer for sending
		packetBuffer.append(packet)

#Loop through the sensors and create a thread for each
for sensor in sensors:
	#Create the thread and give it a sensor as an argument
	thread = threading.Thread(target=worker, args=(sensor,))
	
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
		time.sleep(0.1)
