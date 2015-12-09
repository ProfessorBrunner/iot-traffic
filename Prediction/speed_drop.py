import json
import time
import geo_utils as geo
import graphs


def predictions(points, hazards = [], hazard_decrease = .5):
    count = 0
    prev_point = None

    speeds = []
    next_locations = []
    for point in points:
        if prev_point != None:
            l1 = (point.latitude, point.longitude)
            l2 = (prev_point.latitude, prev_point.longitude)

            distance = geo.calculate_distance(l1,l2)
            time = point.timestamp - prev_point.timestamp
            speed = geo.speed(distance, time)

            predict = geo.predict_next_location(l2, l1, time, time)
            error = geo.error(l2,predict)

            speeds.append(speed * 1000)
            next_locations.append(predict)
            print(error)
        prev_point = point
        count += 1

    return speeds, next_locations

if __name__ == '__main__':
    json_data = open('../SyntheticData/src/data_for_sudden_dip.json')
    data = json.load(json_data)[0]
    json_data.close()

    #add all points to an array
    points = []
    for point in data:
        current = geo.Point(point['latitude'], \
            point['longitude'], \
            geo.convert_timestamp(point['time_stamp']), \
            point['car_id'] \
        )
        points.append(current)

    #create road hazard
    road_hazard = [(250,500)]
    hazard_decrease = .5


    speeds, next_locations = predictions(points, road_hazard, hazard_decrease)

    graphs.graph_speeds(speeds, 'm/s')