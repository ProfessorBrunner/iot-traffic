import geo_utils as geo
import time

if __name__ == '__main__':
    start=time.time()

    point1 = (39.525498,89.534926)
    point2 = (39.498231,89.479093)
    point3 = (39.470964,89.42326) #(39.45178619542422, 89.4516830045628)

    nextPoint = geo.predict_next_location(point1, point2, 300, 300)
    print(nextPoint)
    timeToPoint = geo.calculate_time(point1, point3, .008)/60
    print(timeToPoint, " minutes")

    error = geo.error(nextPoint, point3)
    print("Error: ", error, " km")

    end=time.time()
    cost = end - start
    print("Cost: " , cost , " seconds")