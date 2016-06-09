
from __future__ import print_function

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# create SparkContext
conf = SparkConf().setAppName("Kafka-Spark")
sc = SparkContext(conf=conf)

# create StreamingContext
ssc = StreamingContext(sc, 30)

# new approach (w/o receivers)
topic = ["mytopic"]
brokers =  "141.142.236.172:9092,141.142.236.194:9092"
directKafkaStream = KafkaUtils.createDirectStream(ssc, topic, {"metadata.broker.list": brokers})

lines = directKafkaStream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
ssc.awaitTermination()

print("finished this")