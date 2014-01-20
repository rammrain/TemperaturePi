from Sender import *
from Config import *
import os

os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

config = Config()
sender = Sender(config)

for dirname, dirnames, filenames in os.walk("/sys/bus/w1/devices"):
    for subdirname in dirnames:
        print(subdirname)



#sender.send(12.175, 1)
