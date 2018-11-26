#For interfacing with HC-12
import serial

#Raspi serial port
port = "/dev/ttyUSB0"

#Setup uart connection
uart = serial.Serial(port)

def send(data):
	uart.write(data)