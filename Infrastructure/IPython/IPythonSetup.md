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
sudo pip install ipython==3.2.1
sudo pip install jsonschema terminado
```

###Create Ipython profile (no password added but might wanna change this in the future)
Create the profile for the ipython server
```
ipython profile create nbserver
```

Add the following lines to "/home/ubuntu/.ipython/profile_nbserver/ipython_config.py":
```
c = get_config()

# IPython PySpark
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
```

###Start Ipython server (in nohup mode)
```
nohup ipython notebook --profile=nbserver
```

###Stopping ipython server
Type in command and note the ***pid*** listed:
```lsof nohup.out```

Kill that pid:
```kill pid```