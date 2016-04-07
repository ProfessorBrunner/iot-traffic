"""
Command to run this: ../../../spark/spark-1.5.0-bin-hadoop2.6/bin/spark-submit \
    --packages TargetHolding:pyspark-cassandra:0.3.5 \
    --conf spark.cassandra.connection.host="10.0.3.139" spark-cassandra.py
"""

import pyspark_cassandra
from pyspark_cassandra import streaming

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

# create SparkContext
conf = SparkConf().setAppName("Cassandra-Spark")
sc = CassandraSparkContext(conf=conf)

sc.cassandraTable("iot", "traffic") \
    .select("latitude", "longitude") \
    .collect()


print("got here")

"""
.cassandraTable("keyspace", "table") \
    .select("col-a", "col-b") \
    .where("key=?", "x") \
    .filter(lambda r: r["col-b"].contains("foo")) \
    .map(lambda r: (r["col-a"], 1)
    .reduceByKey(lambda a, b: a + b)
    .collect()
"""
