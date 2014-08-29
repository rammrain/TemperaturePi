#!/usr/bin/env python

from Sender import *
from Config import *
from Sensor import *
import os

os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

config = Config()
sender = Sender(config)

for dirname, dirnames, filenames in os.walk("/sys/bus/w1/devices"):
    for subdirname in dirnames:
        if subdirname != "w1_bus_master1":
            sensor = Sensor(subdirname)
            temp = sensor.get_temp()
            sender.send(temp, 1)
            
            print(sensor.get_temp())
            response = sender.send(temp, Config.sensorMap[subdirname])
            print(response.status_code)
