import pigpio, pynmea2

pi = pigpio.pi()

rx = 23
baud = 9600
bits = 8

pi.set_mode(rx, pigpio.INPUT)

pigpio.exceptions = False
pi.bb_serial_read_close(rx)
pigpio.exceptions = True

pi.bb_serial_read_open(rx, baud, bits)

name = "gps"
id = "G"

def data():
	data = ""
	while True:
		(count, char)= pi.bb_serial_read(rx)
		for i in range(count):
			if chr(char[i]) == "\n":
				return([data.replace("\r", "")])
			data += chr(char[i])
