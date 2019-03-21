import bme680

#Setup the sensor
try:
	BMEsensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
	BMEsensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

#Setup sensor settings
BMEsensor.set_humidity_oversample(bme680.OS_2X)
BMEsensor.set_pressure_oversample(bme680.OS_4X)
BMEsensor.set_temperature_oversample(bme680.OS_8X)
BMEsensor.set_filter(bme680.FILTER_SIZE_3)

BMEsensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
BMEsensor.set_gas_heater_temperature(320)
BMEsensor.set_gas_heater_duration(150)
BMEsensor.select_gas_heater_profile(0)


name = "bme680"
id = "B"

def data():
	#Return data
	while not BMEsensor.get_sensor_data():
		continue
	return([BMEsensor.data.temperature, BMEsensor.data.pressure, BMEsensor.data.humidity])
