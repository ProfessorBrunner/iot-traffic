class Vehicle:
	"""Class for Different Types of Vehicles"""
	def __init__(self, type):
		self.type = type
		self.speed_limit = speed_limit(type)
	def speed_limit(type):
		if type == "CAR":
			return 60
		elif type == "TRUCK":
			return 45
		else:
			return 40
