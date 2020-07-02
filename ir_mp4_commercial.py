#!/usr/bin/python
import subprocess
import time
import sys
import RPi.GPIO as IO
from threading import Event

#import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.OUT) #GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input

res = "800x480"

image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "white", "-g", res, "/home/pi/Downloads/MONDELEZ-INTERNATIONAL.png"])

def loadVideo( value ):	
	switcher = {
        1: "/home/pi/video-ir/mondelez-innovation/oreo.mp4",
        2: "/home/pi/video-ir/mondelez-innovation/cadbury.mp4",
        3: "/home/pi/video-ir/mondelez-innovation/tiger.mp4",
        4: "/home/pi/video-ir/mondelez-innovation/toblerone.mp4",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: ""
    }

    image.terminate()
    image.kill()
    omxprocess1 = subprocess.Popen(['omxplayer', switcher.get(value), '-b'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
    time.sleep(42)
    image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "white", "-g", res, "/home/pi/Downloads/MONDELEZ-INTERNATIONAL.png"])
	return;

def cleanAndExit():
	print "Cleaning..."
	GPIO.cleanup()
	print "Bye!"
	sys.exit()

while True:
    try:
	 if(IO.input(14)==True):
		loadVideo(1)
	 else: 
		loadVideo(2)

	except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


