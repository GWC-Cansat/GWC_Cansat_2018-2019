#For interfacing with HC-12
import serial

#Raspi serial port
port = "/dev/ttyS0"

#Setup uart connection
uart = serial.Serial(port)

def send(data):
	print(data)
	uart.write(data + "\r\n")
