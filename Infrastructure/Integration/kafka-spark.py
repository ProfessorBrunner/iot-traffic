"""
Spark streaming + Kafka integration
From http://spark.apache.org/docs/latest/streaming-kafka-integration.html
"""

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# create SparkContext
conf = SparkConf().setMaster("spark://10.0.3.70:7077").setAppName("Kafka-Spark").set("spark.driver.port", 8200).set("spark.cores.max", 10)
sc = SparkContext(conf=conf)

# create StreamingContext
ssc = StreamingContext(sc, 1)

# new approach (w/o receivers)
topic = "mytopic"
directKafkaStream = KafkaUtils.createDirectStream(ssc, topic, {"metadata.broker.list": brokers})