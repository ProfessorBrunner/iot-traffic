import geopy
import time
import math
import random
import sys
import uuid
from geopy.distance import great_circle
from geopy.distance import VincentyDistance
from geopy.point import Point

LocationsAlongI57 = [[41.723361, -87.625006],[41.569277, -87.741954],[40.121347, -88.310619],[39.168060, -88.509080],[38.689314, -88.979941],
					[36.907961, -89.347108]]
NumberOfSensors = [5,15,25,15,50]
ListOfSensors = []

class sensor:
    def __init__(self, latitude, longitude,sensor_id):
        self.latitude = latitude
        self.longitude = longitude
        self.sensor_id = sensor_id

#calculates the bearing between points on I-57
def calculate_bearing(locationOne, locationTwo):
    dLon = locationOne.longitude - locationTwo.longitude
    y = math.sin(dLon) * math.cos(locationTwo.latitude)
    x = math.cos(locationOne.latitude)*math.sin(locationTwo.latitude) - math.sin(locationOne.latitude)*math.cos(locationTwo.latitude)*math.cos(dLon);
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    return bearing

#calculates the next location from origin within a range of 10km - 20km
def next_location(origin, bearing):
  	d = random.randint(5,10)
  	origin_point = Point(origin.latitude,origin.longitude)
  	destination = VincentyDistance(kilometers=d).destination(origin_point,bearing)
	return (destination.latitude,destination.longitude)

#predicts the next location for a sensor 
def predict_next_location(origin, current):
    bearing = calculate_bearing(origin, current)
    #print(origin , current, bearing)
    current = next_location(current, bearing)
    return current

def main():

	starting_point = LocationsAlongI57[0]
	sensor_id = uuid.uuid1().hex
	sensor_at_starting_point = sensor(starting_point[0],starting_point[1],sensor_id)
	ListOfSensors.append(sensor_at_starting_point)

	for i in range(1,len(LocationsAlongI57)-1):
		end_point = LocationsAlongI57[i]
		sensor_id = uuid.uuid1().hex
		sensor_at_end_point = sensor(end_point[0],end_point[1],sensor_id)
		number_of_locations = NumberOfSensors[i-1]
		for j in range(0,number_of_locations):
			next_location = predict_next_location(sensor_at_starting_point,sensor_at_end_point)
			ListOfSensors.append(sensor(next_location[0],next_location[1],uuid.uuid1().hex))
			sensor_at_starting_point = sensor(next_location[0],next_location[1],uuid.uuid1().hex)
		starting_point = end_point
	index = len(LocationsAlongI57)-1
	ListOfSensors.append(sensor(LocationsAlongI57[index][0],
		LocationsAlongI57[index][1],uuid.uuid1().hex))
	# for i in range(0,len(ListOfSensors)):
	# 	print(ListOfSensors[i].sensor_id)
	return ListOfSensors
if __name__ == "__main__":
	main()
