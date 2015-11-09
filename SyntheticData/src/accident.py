import random
import sys
from time import strftime
import datetime
import uuid
import geolib as geo
import fileio as fio

EARTH_RADIUS = 6378.1						# Radius of earth
SEED_COORDINATE = (40.12009,-88.247681)		# Coordinate
SEED_VELOCITY = 10							# 10 miles/hour
SEED_TIME = 0.0833333						# 5 minutes converted to hour
SEED_DIRECTION = 90							# 90 degrees
SEED_VELOCITY_CRASHED = 5					# 5 miles/hour

def randomize_conditions(max_range):
	random_error = random.random()
	random_range = random.randint(0, max_range)
	velocity_change = random_range*random_error
	random_direction = random.randint(0, 1)
	random_dict = {}
	random_dict['velocity_change'] = velocity_change
	random_dict['direction'] = random_direction
	return random_dict
#end_def

def get_random_coordinates_with_accident(num_coordinates):
	current_velocity = SEED_VELOCITY
	current_coordinate = SEED_COORDINATE
	accident = random.randint(1, num_coordinates-1)
	has_crashed = False

	for x in xrange(1,num_coordinates):
		random_dict = randomize_conditions(5)
		if has_crashed:
			has_crashed = False
			current_velocity = SEED_VELOCITY_CRASHED
		if x == accident:
			has_crashed = True
			current_velocity = 0
			csv = str(current_coordinate[0]) + ',' + str(current_coordinate[1]) + ', Accident'
			print(csv)
			continue
		if random_dict['direction'] == 0:
			current_velocity = current_velocity - random_dict['velocity_change']
		elif random_dict['direction'] == 1:
			current_velocity = current_velocity + random_dict['velocity_change']
		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		csv = str(current_coordinate[0]) + ',' + str(current_coordinate[1]) + ' : ' + str(distance_travelled)
		print(csv)
#end_def
