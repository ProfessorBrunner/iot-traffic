import json
from pprint import pprint

def json_write_to_file(data, filename, display=False):
	if display is True:
		pprint(data)
	with open(filename, 'w+') as newfile:
		json.dump(data, newfile)
	return
#end_def

def json_read_from_file(filename, display=False):
	with open(filename) as data_file:
		data = json.load(data_file)
	if display is True:
		pprint(data)
	return data
