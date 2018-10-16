from nxp_imu import IMU

#Setup the sensor
sensor = IMU()

class sensor:
	name = "9dof"
	
	def data():
		#Return data
		a, m, g = sensor.get()
		return([a, m, g])
	
	def test():
		#Self test
		return True