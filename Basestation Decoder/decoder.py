#Decode the data from the cansat into a usable format
import json

#Gps decoder
def gps(data):
        return(''.join(str(x) for x in data))

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
        data = json.loads(data)

        #Decode the data based on sensor id
        func = senToFunc[id]
        return([id, func(data)])
    except:
        return(-1)