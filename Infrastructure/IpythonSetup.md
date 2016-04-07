#Setting up Ipython Notebook connected with Spark on ACX
==========================

###Requirements
Continue with these steps after...

1. Launched an Ubunutu Instance (14.04 LTS used for this)
	* Ensure that you have a floating IP associated with this instance (with appropriate security settings)
2. Spark installed (1.5.0 used)
3. Python 2.7 installed
4. Pip installed (using verison 8.1.1) (curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python)

###Install packages
sudo apt-get update

sudo apt-get install ipython ipython-notebook

sudo pip install --upgrade ipython tornado

For this installation, I have ipython 1.2.1 and tornado 4.3

###Create Ipython profile
