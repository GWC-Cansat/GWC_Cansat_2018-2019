import serial

#Gps serial port
port = "/dev/ttyUSB0"

#Setup sensor
sensor = serial.Serial(port)

class sensor:
	name = "gps"
	
	def data():
		#Return data
		return(sensor.readline())
	
	def test():
		#Self test
		return True