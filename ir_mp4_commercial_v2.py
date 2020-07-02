import time
import subprocess
import sys
import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)
 #GPIO 3 -> Green LED as output
IO.setup(14,IO.IN) 

moviepath = '/home/pi/video-ir/mondelez-innovation/oreo.mp4' 
moviepath2 = '/home/pi/video-ir/mondelez-innovation/cadbury.mp4'


def video1():
    global omxprocess
    omxprocess = subprocess.Popen(['omxplayer', moviepath, '-b'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)


def video2():
    global omxprocess    
    omxprocess = subprocess.Popen(['omxplayer', moviepath2, '-b'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)

    print("It’s time !")


if __name__ == "__main__":
    print("press ctrl-c to stop")
    loop_forever = True
    while loop_forever and IO.input(14)==True:
        video1()
        try:
            time.sleep(60)
            omxprocess.stdin.flush()
        except IO.input(14)==False:
            omxprocess.stdin.flush()
            loop_forever = False
    while not loop_forever:
        video2()
        try:
            time.sleep(60)
            omxprocess.stdin.flush()
        except IO.input(14)=True:
            omxprocess.stdin.flush()
            loop_forever = True        