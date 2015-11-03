Setting up Kafka on Ubuntu
==========================

To set up a two-broker Kafka cluster on two Ubuntu nodes, follow the steps below:

On both nodes (*node1* and *node2*):

1. `sudo apt-get update`
2. `sudo apt-get install default-jre`
3. `sudo apt-get install default-jdk`
4. `mkdir ~/kafka`
5. `wget kakfa.tar.gz (check https://www.apache.org/dyn/closer.cgi?path=/kafka/0.8.2.0/kafka_2.10-0.8.2.0.tgz for download mirrors)
6. `cd ~/kafka`
7. `tar -xzf ../kafka.tar.gz -- strip 1`
8. `vi config/zookeeper.properties`
```
server.1=node1:2888:3888
server.2=node2:2888:3888
initLimit=5
syncLimit=2
```
9. `mkdir /tmp/zookeeper`
10. On node1: `echo “1” > /tmp/zookeeper/myid`
11. On node2: `echo “2” > /tmp/zookeeper/myid`
12. `vi config/server.properties`

On node1:
```
broker.id=0
zookeeper.connect=node1:2181,node2:2181
```
On node2:
```
broker.id=1
zookeeper.connect=node1:2181,node2:2181
```
13. `cd ~/kafka`
14. Start ZooKeeper on both nodes: `nohup bin/zookeeper-server-start.sh config/zookeeper.properties &`
15. Start Kafka on both nodes: `nohup bin/kafka-server-start.sh config/server.properties &`
16. On either node, create a Kafka topic: `bin/kafka-topics.sh —create —zookeeper node1:2181,node2:2181 --replication-factor 2 —partitions 1 --topic mytopic`
17. On one node, start a Kafka producer: `bin/kafka-console-producer.sh —broker-list node1:9092,node2:9092 --topic mytopic`
18. On the other node: `bin/kafka-console-consumer.sh --zookeeper node1:2181,node2:2181 --topic mytopic --from-beginning`

To send messages from the Producer to the Consumer, type in the Producer terminal.