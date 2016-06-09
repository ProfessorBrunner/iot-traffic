##Road Segments

class Segment:
    def __init__(self, latitude, longitude,\
     landmark_time, identification):
        self.latitude = latitude
        self.longitude = longitude
        self.landmark = landmark_time
        self.current_time = landmark_time
        self.id = identification
        self.obs = 0
        self.X = 0
        self.Y = 0
        self.speed = 0
        
segments = [Segment(47.1,47.1,0, 0),...]

##Dynamic Map Matching Algorithm
import math

#Distance in kilometers between two latitude and longitude locations
def distance(obsLoc, segmentLoc):
    lat1, lon1 = obsLoc
    lat2, lon2 = segmentLoc
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2)\
     + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), \
        math.sqrt(1-a))
    d = radius * c

    return d

#match an observation to a road segment (within .25 km of a road segment)
def findSegment(latitude, longitude):
    obsLoc = (latitude,longitude)
    
    closest = None
    for segment in segments:
        segmentLoc = (segment.latitude, \
            segment.longitude)
        dist = distance(obsLoc, segmentLoc)
        if closest == None or \
            dist <= closest:
            if dist <= .25:
                closest = segment
    return segment


##Time Decay Model

def f(time):
    return time

def g(velocity):
    return (velocity ** 2)

def update(lat, longitude, \
    velocity, time):
    #dynamic map matching algorithm
    seg = findSegment(lat,longitude)
    
    #weight time and velocity
    wtime = f(time-self.landmark)
    wvel = g(velocity)
    
    #produce X and Y for this observation
    #and add these to the segment speed
    X = wtime*wvel*velocity
    Y = wtime*wvel
    seg.X += X
    seg.Y += Y
    seg.speed = seg.X/seg.Y
    seg.obs += 1
    seg.current_time = time


%%writefile timedecaykafka.py

import pyspark
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import\
 StreamingContext
from pyspark.streaming.kafka\
 import KafkaUtils

# create SparkContext
conf = SparkConf().setAppName("Kafka-Spark")
sc = SparkContext(conf=conf)

# create StreamingContext
ssc = StreamingContext(sc, 30)

# new approach (w/o receivers)
topic = ["traffic", "weather"]
brokers =  "141.142.236.172:9092,\
    141.142.236.194:9092"
directKafkaStream = \
    KafkaUtils.createDirectStream(ssc,topic\
    , {"metadata.broker.list": brokers})

ssc.start()
ssc.awaitTermination()