Setting up Storm on Ubuntu
==========================

### First set up ZooKeeper on one node (*zoo*)

* `sudo apt-get update`
* `sudo apt-get install default-jre`
* `sudo apt-get install default-jdk`
* `mkdir ~/zookeeper`
* `wget zookeeper.tgz` (check http://storm.apache.org/downloads.html for download mirrors)
* `cd ~/zookeeper`
* `tar -xzf ../zookeeper.tgz --strip 1`
* `mkdir /tmp/zookeeper`
* `cd conf`
* `cp zoo_sample.cfg zoo.cfg`
* `vi zoo.cfg`
    ```
    server.1=$zoo:2888:3888
	```
* `echo "1" > /tmp/zookeeper/myid`
* `cd ~/zookeeper`
* Start ZooKeeper:

	`bin/zkServer.sh start`

### Set up Storm on three Ubuntu nodes (*master*, *worker1* and *worker2*)

* `sudo apt-get update`
* `sudo apt-get install default-jre`
* `sudo apt-get install default-jdk`
* Install Python if it's not installed already.
* `mkdir ~/storm`
* `mkdir /tmp/storm`
* `wget storm.tgz` (check http://storm.apache.org/downloads.html for download mirrors)
* `cd ~/storm`
* `tar -xzf ../storm.tgz --strip 1`
* `vi conf/storm.yaml`
	```
	storm.zookeeper.servers:
    	 - "$zoo"
	nimbus.host: "$master"
	storm.local.dir: "/tmp/storm"
	```
* `cd ~/storm`
* Start *Nimbus* (master) on `master`:

	`nohup bin/storm nimbus &`
* Start *Supervisor* (workers) on `worker1` and `worker2`:

	`nohup bin/storm supervisor &`
* Start the UI on `master`:

	`nohup bin/storm ui &`

The Storm UI will be at `$master:8080`. Open port `8080` to access the Storm UI externally.

### References 

* http://zookeeper.apache.org/doc/r3.3.3/zookeeperStarted.html#sc_InstallingSingleMode
* http://storm.apache.org/documentation/Setting-up-a-Storm-cluster.html