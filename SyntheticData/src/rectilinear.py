"""
	Randomizer could be better - Work on Randomizer
	Functions:
		- N car motion for random coordinates
		- Speed drop data for non varying speeds
		- Speed drop data for varying speeds
"""
import random
import sys
from time import strftime
import datetime
import uuid
import geolib as geo

EARTH_RADIUS = 6378.1						# Radius of earth
SEED_COORDINATE = (40.12009,-88.247681)		# Coordinate
SEED_VELOCITY = 20							# 10 miles/hour
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

def get_n_car_motion_for_random_coordinates(num_coordinates, num_cars):
	result = []
	current_velocity = SEED_VELOCITY
	current_coordinate = SEED_COORDINATE
	time_stamp = datetime.datetime.now()
	first_stamp = time_stamp
	unique_id = uuid.uuid4()
	first_car_data = []

	for i in range(num_coordinates):
		random_error = random.random()
		random_range = random.randint(0, 5)
		velocity_change = random_range*random_error
		random_direction = random.randint(0, 1)
		if random_direction == 0:
			current_velocity = current_velocity - velocity_change
		elif random_direction == 1:
			current_velocity = current_velocity + velocity_change

		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")

		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)
	result.append(first_car_data)
	for i in range(num_cars-1):
		secondary_car_data = get_car_motion_for_coordinates(first_car_data, first_stamp)
		result.append(secondary_car_data)
	return result
#end_def

def get_car_motion_for_coordinates(data, first_stamp):
	json_data = []
	temp_object = data[0]
	time_stamp = first_stamp
	current_velocity = SEED_VELOCITY
	unique_id = uuid.uuid4()
	for item in data:
		distance = geo.distance_between_two_coordinates((temp_object['latitude'], temp_object['longitude']),(item['latitude'], item['longitude']))	# stays constant
		random_dict = randomize_conditions(6)
		if random_dict['direction'] == 0:
			current_velocity = current_velocity - random_dict['velocity_change']
		elif random_dict['direction'] == 1:
			current_velocity = current_velocity + random_dict['velocity_change']
		time_taken = distance/current_velocity
		temp_object['car_id'] = str(unique_id)
		temp_object['latitude'] = item['latitude']
		temp_object['longitude'] = item['longitude']
		time_stamp = time_stamp + datetime.timedelta(0, time_taken)
		temp_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		json_data.append(temp_object)
		temp_object = item
	return json_data
#end_def

"""
	Try to improve randomness so that it never reaches negative 0 but remains in some bounds
"""
def get_random_coordinates_positive_acceleration(num_coordinates):
	current_velocity = SEED_VELOCITY
	current_coordinate = SEED_COORDINATE
	for i in range(num_coordinates):
		random_error = random.random()
		random_range = random.randint(0, 5)
		velocity_change = random_range*random_error
		current_velocity = current_velocity + velocity_change
		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		csv = str(next_coordinate[0]) + ',' + str(next_coordinate[1])
		print(csv)
#end_def

"""
	Get sudden dip with varying velocities
"""
def get_random_coordinates_sudden_dip_varying(num_coordinates):
	result = []
	current_coordinate = SEED_COORDINATE
	time_stamp = datetime.datetime.now()
	first_stamp = time_stamp
	unique_id = uuid.uuid4()
	first_car_data = []
	current_velocity = SEED_VELOCITY

	for i in range(num_coordinates/3):
		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)
		random_dict = randomize_conditions(2)
		print(i, current_velocity)
		if random_dict['direction'] == 1:
			current_velocity = current_velocity + random_dict['velocity_change']
		if random_dict['direction'] == 0:
			if current_velocity + random_dict['velocity_change'] > 10:
			 	current_velocity = current_velocity - random_dict['velocity_change']

	current_velocity = current_velocity - 8
	for i in range(num_coordinates/3):
		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)
		random_dict = randomize_conditions(2)
		print(i, current_velocity)
		if random_dict['direction'] == 1:
			current_velocity = current_velocity + random_dict['velocity_change']
		if random_dict['direction'] == 0:
			if current_velocity + random_dict['velocity_change'] > 6:
			 	current_velocity = current_velocity - random_dict['velocity_change']

	current_velocity = current_velocity + 8
	for i in range(num_coordinates/3):
		distance_travelled = current_velocity * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)
		random_dict = randomize_conditions(2)
		print(i, current_velocity)
		if random_dict['direction'] == 1:
			current_velocity = current_velocity + random_dict['velocity_change']
		if random_dict['direction'] == 0:
			if current_velocity + random_dict['velocity_change'] > 10:
			 	current_velocity = current_velocity - random_dict['velocity_change']
	result.append(first_car_data)
	return result


"""
	Get sudden dip
"""
def get_random_coordinates_sudden_dip(num_coordinates):
	result = []
	current_coordinate = SEED_COORDINATE
	time_stamp = datetime.datetime.now()
	first_stamp = time_stamp
	unique_id = uuid.uuid4()
	first_car_data = []

	for i in range(num_coordinates/3):
		distance_travelled = SEED_VELOCITY * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)

	for i in range(num_coordinates/3):
		distance_travelled = (SEED_VELOCITY-10) * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)

	for i in range(num_coordinates/3):
		distance_travelled = SEED_VELOCITY * SEED_TIME
		next_coordinate = geo.predict_next_coordinate(current_coordinate, distance_travelled, SEED_DIRECTION)
		current_coordinate = next_coordinate
		json_object = {}
		json_object['car_id'] = str(unique_id)
		json_object['latitude'] = current_coordinate[0]
		json_object['longitude'] = current_coordinate[1]
		json_object['time_stamp'] = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
		first_car_data.append(json_object)
		time_stamp = time_stamp + datetime.timedelta(0, 300)
	result.append(first_car_data)
	return result
