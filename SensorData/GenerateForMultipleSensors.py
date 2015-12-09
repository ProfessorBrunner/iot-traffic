import sys
import datetime
import uuid
import json
from random import randint
from kafka import SimpleProducer, KafkaClient
import GenerateForOneSensor as one_sensor

SEED_BROKER = '141.142.236.172:9092'

def main(argv):
#argv[1] = time interval; argv[2] = number of days; argv[3]=json file to write to; argv[4]=number of sensors 
	data_points = (24*60*int(sys.argv[2]))/int(sys.argv[1])
	data_for_multiple_sensors=[]
	for i in range(0,int(sys.argv[4])):
		sensor_id = uuid.uuid1().hex
		data_set = one_sensor.generate_for_one_sensor(sys.argv[1],sys.argv[2],data_points,sensor_id)
		data_for_multiple_sensors.append(data_set)
	with open(sys.argv[3], 'w') as outfile:
	 	json.dump(data_for_multiple_sensors, outfile)
	
	#Kafka
	kafka = KafkaClient(SEED_BROKER)
	producer = SimpleProducer(kafka, async=True)
	for item in data_for_multiple_sensors:
		for obj in item:
			message_str = str(obj['sensor_id'])+' , '+str(obj['timestamp'])+' , '+str(obj['surface_temp'])
			encoded = message_str.encode()
			producer.send_messages('mytopic',encoded)

if __name__ == "__main__":
	main(sys.argv[1:])
