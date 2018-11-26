import spidev

spi = spidev.SpiDev()
spi.open(0,0)

class sensor:
	name = "gps"
	id = "G"
	
	def data():
		#Return data
		byte = spi.read(1)
		data = []
		while byte != '\n':
			data.append(byte[0])
			byte = spi.read(1)
		return(data)
	
	def test():
		#Self test
		return True