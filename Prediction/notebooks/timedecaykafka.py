
##Spark Kafka
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# create SparkContext
conf = SparkConf().setAppName("Kafka-Spark")
sc = SparkContext(conf=conf)

# create StreamingContext (updates every 30 seconds)
ssc = StreamingContext(sc, 30)

topic = ["mytopic"]
brokers =  "141.142.236.172:9092,141.142.236.194:9092"
directKafkaStream = KafkaUtils.createDirectStream(ssc, topic, {"metadata.broker.list": brokers})

ssc.start()
ssc.awaitTermination()