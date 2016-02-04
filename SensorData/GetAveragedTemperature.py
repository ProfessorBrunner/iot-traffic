from urllib2 import Request, urlopen, URLError
import json
import sys

temperature_list=[]

#timestamp = month:day:year:hours:mins:seconds
def create_url(timestamp,latitude,longitude):
	broken_string = timestamp.split(':')
	month = broken_string[0] 
	day = broken_string[1]
	year = broken_string[2]
	hours = broken_string[3]
	mins = broken_string[4]
	seconds = broken_string[5]
	url = 'http://api.wunderground.com/api/c711451f1ecbc357/history_'+year+month+day+'/q/'+latitude+','+longitude+'.json'
	return url

def get_response(timestamp,latitude,longitude):
	request = Request(create_url(timestamp,latitude,longitude))
	try:
		response = urlopen(request)
		response = response.read()
	except URLError, e:
		print e
 	return response

def parse_response(timestamp,latitude,longitude):
	response = get_response(timestamp,latitude,longitude)
	j = json.loads(response)
	j = j['history']['observations']

	broken_string = timestamp.split(':')
	hours = broken_string[3]

	for i in range(0,len(j)):
		temp = j[i]
		temp_hour = temp['date']['hour']
		if temp_hour == hours: 
			temperature = temp['tempm']
			temperature_list.append(temperature)

#averages out the temperature for that day and time over the last 5 years 
def main(argv):
	timestamp = sys.argv[1]
	latitude = sys.argv[2]
	longitude = sys.argv[3]

	broken_string = timestamp.split(':')
	requested_month = broken_string[0] 
	requested_day = broken_string[1]
	requested_year = broken_string[2]
	requested_hours = broken_string[3]
	requested_mins = broken_string[4]
	requested_seconds = broken_string[5]
	
	year = int(requested_year) - 1 
	for i in range(0,4):
		timestamp_new = requested_month+':'+requested_day+':'+str(year)+':'+requested_hours+':'+requested_mins+':'+requested_seconds
		parse_response(timestamp_new,latitude,longitude)
		year = str(int(year)-1)

	average_temperature = 0
	for i in range(0,len(temperature_list)):
		average_temperature = float(average_temperature) + float(temperature_list[i])
	average_temperature = average_temperature/float(5)
	
	print average_temperature
	return average_temperature

if __name__ == "__main__":
	main(sys.argv[1:])