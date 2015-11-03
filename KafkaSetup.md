Setting up Kafka on Ubuntu
==========================

To set up a two-broker Kafka cluster on two Ubuntu nodes (*node1* and *node2*), follow the steps below:

* `sudo apt-get update`
* `sudo apt-get install default-jre`
* `sudo apt-get install default-jdk`
* `mkdir ~/kafka`
* `wget kafka.tgz` (check https://www.apache.org/dyn/closer.cgi?path=/kafka/0.8.2.0/kafka_2.10-0.8.2.0.tgz for download mirrors)
* `cd ~/kafka`
* `tar -xzf ../kafka.tgz -- strip 1`
* `vi config/zookeeper.properties`
```
server.1=node1:2888:3888
server.2=node2:2888:3888
initLimit=5
syncLimit=2
```
* `mkdir /tmp/zookeeper`
* On *node1*:

	`echo "1" > /tmp/zookeeper/myid`
* On *node2*:

	`echo "2" > /tmp/zookeeper/myid`
* `vi config/server.properties`

On *node1*:

```
broker.id=0
zookeeper.connect=node1:2181,node2:2181
```
On *node2*:

```
broker.id=1
zookeeper.connect=node1:2181,node2:2181
```

* `cd ~/kafka`
* Start ZooKeeper on both nodes:

	`nohup bin/zookeeper-server-start.sh config/zookeeper.properties &`
* Start Kafka on both nodes:

	`nohup bin/kafka-server-start.sh config/server.properties &`
* On either node, create a Kafka topic:

	`bin/kafka-topics.sh --create --zookeeper node1:2181,node2:2181 --replication-factor 2 --partitions 1 --topic mytopic`
* On one node, start a Kafka producer:

	`bin/kafka-console-producer.sh --broker-list node1:9092,node2:9092 --topic mytopic`
* On the other node, start a consumer:

	`bin/kafka-console-consumer.sh --zookeeper node1:2181,node2:2181 --topic mytopic --from-beginning`

To send messages from the producer to the consumer, type in the producer terminal. Messages are newline-separated by default.