"""
Spark streaming + Kafka integration
From http://spark.apache.org/docs/latest/streaming-kafka-integration.html

command to run: ./spark/spark-1.5.0-bin-hadoop2.6/bin/spark-submit --master spark://10.0.3.70:7077 --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.0 spark-kafka-complete.py
"""

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# create SparkContext
conf = SparkConf().setAppName("Kafka-Spark")
sc = SparkContext(conf=conf)

# create StreamingContext
ssc = StreamingContext(sc, 1)

# new approach (w/o receivers)
topic = ["mytopic"]
brokers =  "141.142.236.172:9092,141.142.236.194:9092"
directKafkaStream = KafkaUtils.createDirectStream(ssc, topic, {"metadata.broker.list": brokers})

print("finished this")
print(ssc)
#print(directKafkaStream)
