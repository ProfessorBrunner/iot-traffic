import fileio as fio
import rectilinear as rect
import accident as accident
import sys
from kafka import SimpleProducer, KafkaClient

SEED_BROKER = '141.142.236.172:9092'

def generate_and_populate_rect_data_for_n_cars(data_points, num_cars):
    res = rect.get_n_car_motion_for_random_coordinates(data_points, num_cars)
    text_file_name = 'data_for_'+str(num_cars)+'_cars.json'
    fio.json_write_to_file(res, text_file_name)
    # Kafka
    kafka = KafkaClient(SEED_BROKER)
    producer = SimpleProducer(kafka, async=True)
    for item in res:
         for obj in item:
             message_str = obj['car_id'] +','+ str(obj['latitude'])+','+str(obj['longitude'])+','+ obj['time_stamp']
             encoded = message_str.encode()
             producer.send_messages(b'mytopic', encoded)

def generate_rect_data_speed_dip():
    res = rect.get_random_coordinates_sudden_dip(750)
    text_file_name = 'data_for_sudden_dip.json'
    fio.json_write_to_file(res, text_file_name)

if __name__ == '__main__':
    #generate_and_populate_rect_data_for_n_cars(100, 1)
    generate_rect_data_speed_dip()
