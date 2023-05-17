import RPi.GPIO as GPIO

import subprocess


import time

GPIO.setmode(GPIO.BOARD)


cmd = "lxterminal &"

flagPush = True

SW = 7
LED = 11

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(SW,GPIO.IN)

try:
    while 1:
        key_in = GPIO.input(SW)

        if key_in == 1:
            if flagPush :
                subprocess.call(cmd , shell=True)
                flagPush = False
            print("SWが押された")
        else:
            if not flagPush:
                flagPush = True
            print("SW 離れた")
        time.sleep(0.2)

except KeyboardInterrupt:
    pass
GPIO.cleanup()















