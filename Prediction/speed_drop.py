import json
import time
import geo_utils as geo
import graphs

with open('../SyntheticData/src/data_for_sudden_dip.json') as json_data:
    data = json.load(json_data)[0]
    json_data.close()

    prev_point = None

    speeds = []
    for point in data:
        current = geo.Point(point['latitude'], \
            point['longitude'], \
            geo.convert_timestamp(point['time_stamp']), \
            point['car_id'] \
        )

        if prev_point != None:
            distance = geo.calculate_distance((current.latitude, current.longitude),(prev_point.latitude, prev_point.longitude))
            time = current.timestamp - prev_point.timestamp
            speed = geo.speed(distance, time)

            speeds.append(speed * 1000)

            print(distance)
        prev_point = current

    graphs.graph_speeds(speeds, 'm/s')


