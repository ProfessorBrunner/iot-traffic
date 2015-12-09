import geopy
import time
import math
from geopy.distance import great_circle
from geopy.distance import VincentyDistance


class Point:
    def __init__(self, latitude, longitude, timestamp, car_id, hazard=None):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.car_id = car_id
        self.hazard = hazard


"""Convert String timestamp in file to time variable
"""
def convert_timestamp(timestamp):
    #2015-11-13 14:34:54.963036
    stamp = time.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    result = time.mktime(stamp)
    return result



"""Simple formula for speed
Conventional units will be km/s
"""
def speed(distance, time):
    return distance/time



"""Simple formula for distance between 2 geo points
locationOne and locationTwo will be coordinates
Conventional units will be km
"""
def calculate_distance(locationOne, locationTwo):
    distance = great_circle(locationOne, locationTwo).kilometers
    return distance



def calculate_bearing(locationOne, locationTwo):
    dLon = locationOne[1] - locationTwo[1];
    y = math.sin(dLon) * math.cos(locationTwo[0]);
    x = math.cos(locationOne[0])*math.sin(locationTwo[0]) - math.sin(locationOne[0])*math.cos(locationTwo[0])*math.cos(dLon);
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    return bearing



def next_location(origin, speed, interval, bearing):
    #print("The speed of the vehicle is: " + str(speed) + " km/s")
    d = speed*interval
    #print("In " + str(interval) + " seconds the vehicle will travel " + str(d) + " km")
    destination = VincentyDistance(kilometers=d).destination(origin, bearing)
    return (destination.latitude, destination.longitude)



"""origin and current are two geopy.Point objects
This method will use these points to establish a speed and bearing
in order to predict the vehicles next Location
"""
def predict_next_location(origin, current, time, interval, steps=1):
    distance = calculate_distance(origin, current)
    #print("The distance between the two points is: " + str(distance) + " km")
    bearing = calculate_bearing(origin, current)
    #print("The bearing of the two points is: " + str(bearing) + " degrees")
    for step in range(steps):
        current = next_location(current, speed(distance, time), interval, bearing)
    return current



def calculate_time(origin, destination, speed):
    distance = calculate_distance(origin, destination)
    return distance/speed




def error(predicted, actual):
    return calculate_distance(predicted, actual)