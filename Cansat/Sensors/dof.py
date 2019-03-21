from nxp_imu import IMU
import time

#Setup the sensor
IMUsensor = IMU(gs=4, dps=2000)

name = "9dof"
id = "D"

def data():
	#Return data
	a, m, g = IMUsensor.get()
	a = list(a)
	m = list(m)
	g = list(g)
	time.sleep(0.1)
	return([a, m, g])
