import math
import random
import sys
from time import strftime
import datetime
import uuid
from math import atan2, degrees, pi
import json

EARTH_RADIUS = 6378.1						# Radius of earth

def predict_next_coordinate(current_coordinate, distance, direction):
	R = EARTH_RADIUS	#Radius of the Earth
	bearing = math.radians(direction)
	lat_1 = math.radians(current_coordinate[0])
	lon_1 = math.radians(current_coordinate[1])
	lat_2 = math.asin(math.sin(lat_1)*math.cos(distance/R) + math.cos(lat_1)*math.sin(distance/R)*math.cos(bearing))
	lon_2 = lon_1 + math.atan2(math.sin(bearing)*math.sin(distance/R)*math.cos(lat_1), math.cos(distance/R)-math.sin(lat_1)*math.sin(lat_2))
	final_lat = math.degrees(lat_2)
	final_lon = math.degrees(lon_2)
	return (final_lat, final_lon)
#end_def

def distance_between_two_coordinates(source_coordinate, destination_coordinate):
	phi1 = math.radians(90.0 - source_coordinate[0])
	phi2 = math.radians(90.0 - destination_coordinate[0])
	theta1 = math.radians(source_coordinate[1])
	theta2 = math.radians(destination_coordinate[1])
	cosine = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
	arc = math.acos(cosine)
	standardized_arc = EARTH_RADIUS * arc
	return standardized_arc
#end_def

def turn_detection(x1, x2, y1, y2):
	dx = x2 - x1
	dy = y2 - y1
	rads = atan2(-dy,dx)
	rads %= 2*pi
	degs = degrees(rads)
	return degs
#enddef