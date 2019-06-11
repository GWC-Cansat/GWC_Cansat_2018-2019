#Decode the data from the cansat into a usable format
import json, pynmea2

#Gps decoder
def gps(data):
	data = pynmea2.parse(data[0])
        return((data.latitude, data.longitude))

#BME680 decoder
def bme(data):
    class bme:
        temp = data[0] #Temperature
        pres = data[1] #Pressure
        hum = data[2] #Humidity
    return(bme)

#9Dof decoder
def dof(data):
	return(data)

#Sensor id to decode function
senToFunc = {
    "G": gps,
    "B": bme,
    "D": dof
}

#Main function
def decode(data):
	try:
		#Get the first character as it is an id and remove it from the data
		id = data[0]
		data = data[1:]

		#Turn data into list
		data = json.loads(data.replace("'","\""))

		#Decode the data based on sensor id
		func = senToFunc[id]
		return([id, func(data)])
	except:
		return(-1)
