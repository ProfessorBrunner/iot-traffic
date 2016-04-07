#Setting up Ipython Notebook connected with Spark on ACX
==========================

###Requirements
Continue with these steps after...

1. Launched an Ubunutu Instance (14.04 LTS used for this)
	* Ensure that you have a floating IP associated with this instance (with appropriate security settings)
2. Python 2.7 installed
3. Hostname is set in the /etc/hosts

###Install Spark 1.5.0
Download and unpack spark:
```
wget http://d3kbcqa49mib13.cloudfront.net/spark-1.5.0-bin-hadoop2.6.tgz
tar -xvzf spark-1.5.0-bin-hadoop2.6.tgz
```

Add the spark_home path to the .bashrc (vi ~/.bashrc)
```
export SPARK_HOME="/home/ubuntu/spark/spark-1.5.0-bin-hadoop2.6"
```

Afterwards, reload the .bashrc file:
```source ~/.bashrc```

###Install packages for Pip and Ipython
Update Ubuntu and install packages for python and pip packages:
```
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo -H pip install --upgrade pip
```

Install ipython and dependencies
```
sudo apt-get install ipython-notebook
```

###Create Ipython profile
```
ipython profile create nbserver
```