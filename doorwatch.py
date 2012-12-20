#!/usr/bin/python
import os
import serial
import time
import httplib
import urllib

import config

conn = httplib.HTTPConnection(config.server)


headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
os.getpid()
open('/var/run/watchd.pid', 'w').write(str(os.getpid()))
ser = serial.Serial(config.serialport, 9600)
time.sleep(1)

while 1:
  x = int(ser.read())
  if x == 1:
    os.system("./warn.sh " + config.localmac + " &");
    params = urllib.urlencode({'type': 'movement'})
    conn.request("POST", config.loglocation, params, headers )
    print "movement"
  if x == 2:
    os.system("./screenback.sh " + config.localmac + " &")
    os.system("amixer sset Master on >/dev/null 2>&1")
    print "door closed"
    params = urllib.urlencode({'type': 'doorclosed'})
    conn.request("POST", config.loglocation, params, headers )
  if x == 3:
    os.system("./killscreen.sh " + config.localmac + " &")
    os.system("amixer sset Master off >/dev/null 2>&1")
    print "door opened"
    params = urllib.urlencode({'type': 'dooropened'})
    conn.request("POST", config.loglocation, params, headers )
  resp=conn.getresponse()

