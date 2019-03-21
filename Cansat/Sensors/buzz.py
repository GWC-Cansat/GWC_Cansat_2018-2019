import pigpio, time

pi = pigpio.pi()
pi.set_mode(26, pigpio.OUTPUT)

def data():
	time.sleep(120)
	pi.set_PWM_dutycycle(13, 128)
	tone = [8000, 4000, 2000, 1600, 1000, 800, 500, 400, 320, 250, 200]

	while True:
		for i in tone[1:]:
			time.sleep(0.1)
			pi.set_PWM_frequency(13, i)
		tone = tone[::-1]
