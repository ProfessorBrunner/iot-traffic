import sys
import datetime
import uuid
import json
from random import randint

def generate_for_one_sensor(time_interval,time_period,data_points,sensor_id): 
	data_set=[]
	# format = "%a %b %d %H:%M:%S %Y"
	format = "%Y-%m-%d %H:%M:%S"
	now = datetime.datetime.now()
	time_interval_integer = int(time_interval)
	#temp ranges : between 11 am to 4 pm - 18 to 25, between 4 pm to midnight - 8 to 18, midnight to 11 am - -5 to 8
	for i in range(0,data_points):
		now = now + datetime.timedelta(minutes=time_interval_integer)
		if(now.hour>=11) and (now.hour<=16):
			temp = randint(64,77)
		if(now.hour>16) and (now.hour<=23):
			temp = randint(46,64)
		if(now.hour>=0) and (now.hour<11):
			temp = randint(23,46)
		data = {}
		data['sensor_id'] = sensor_id
		data['timestamp'] = now.strftime(format)
		data['surface_temp'] = temp
		data_set.append(data)
	return data_set