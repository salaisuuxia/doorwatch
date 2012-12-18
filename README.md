doorwatch
=========

arduino based alerting of motion/switch operation to a remote server and local command execution

requires:
cdc_acm kernel module
python2-pyserial
python2-httplib

a server with mysql, http with php (for logging)

this script is designed to be run on a linux box, but triggers commands over SSH to a mac.

to use:

upload 'doorwatch.ino' to your arduino

configure 'config.py' to have your logging server's address, serial port of arduino, log URL and mac IP/DNS

create a user in MySQL with the rights to create a database or create the database and grant rights to that user.

configure 'homelog/submit.php' to have that MySQL username and password

upload the 'homelog' directory into the webserver's root

add the ssh public key of the linux box to the authorized keys file on the mac

run doorwatch.py
