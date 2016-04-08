import csv
import sys
from geopy.distance import vincenty
import calendar

def weather_conditions(argv):
	latitude = argv[0]
	longitude = argv[1]
	date = argv[2]
	month = date[4:6]
	month_name = str(calendar.month_name[int(month)])
	day = date[6:]
	required_days = []
	year = 2005

	wind_velocity = 0.0

	point_location = (latitude,longitude)
	minimum_distance = 10000
	closest_station = "USW00014806" #temp value
	with open("stationList_Final.csv") as station_file:
		station_list = csv.reader(station_file)
		for row in station_list:
			station_location = (row[len(row)-2],row[len(row)-1])
			distance = float(vincenty(point_location, station_location).miles)
			if distance < minimum_distance:
				minimum_distance = distance
				closest_station = row[0]

	for i in range(0,11):
		filename = str(year)+"USTemp.csv"
		with open(filename) as f:
			yearData = csv.reader(f)
			for row in yearData:
				if (row[1][4:6] == month) and (row[1][6:] == day) and row[0]==closest_station:
					required_days.append(row)
					break;
		year += 1

	with open("WindVelocity.csv") as f:
		wind_data = csv.reader(f)
		for row in wind_data:
			if row[0]==month_name:
				wind_velocity = float(row[1])

	tmin_average = []
	snow_average = []
	prcp_average = []
	for i in range(0,len(required_days)):
		data = required_days[i]
	 	if "TMIN" in data:
	 		index = data.index("TMIN")
	 		tmin_average.append(float(data[index+1]))
	 	 
	 	if "SNWD" in data:
	 		index = data.index("SNWD")
	 		snow_average.append(float(data[index+1]))

	 	if "PRCP" in data:
	 		index = data.index("PRCP")
	 		prcp_average.append(float(data[index+1]))

	tmin = sum(tmin_average)/len(tmin_average)
	snow = sum(snow_average)/len(snow_average)
	prcp = sum(prcp_average)/len(prcp_average)

	result = {}
	result['tmin'] = tmin
	result['snow'] = snow
	result['prcp'] = prcp
	result['wind'] = wind_velocity
	print(tmin,snow,prcp,wind_velocity)
	return result

