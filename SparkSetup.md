Setting up Spark on Ubuntu
==========================

To set up a Spark cluster, follow the steps below:

On all nodes -

* `sudo apt-get update`
* `sudo apt-get install default-jdk`
* `mkdir ~/spark`
* `wget spark.tgz` (check http://www.apache.org/dyn/closer.lua/spark/spark-1.5.1/spark-1.5.1-bin-hadoop2.6.tgz for download mirrors)
* `cd ~/spark`
* `tar -xzf ../spark.tgz`
* `cd spark-1.5.1-bin-hadoop2.6/conf`
* `cp spark-env.sh.template spark-env.sh`
* `vi spark-env.sh`
```
SPARK_MASTER_IP=$master_ip
```
* Ensure that an entry for `$master_ip` exists in `/etc/hosts`.

On the master -

* To ensure that the workers can connect to the master, open port `7077`. On Azure, this can be done from the *Endpoints* tab on the dashboard.
* If you'd like the Spark Master Web UI to be visible externally, open port `8080`. 
* Start the Spark master:

	```
	cd ~/spark
	./sbin/start-master.sh
	```

The Spark Web UI should now be visible at *$external_master_ip:8080*.

On the workers -

* Start the worker process:

	```
	cd ~/spark
	./sbin/start-slave.sh spark://$master_ip:7077
	```

The Web UI should now show the workers as *ALIVE*.