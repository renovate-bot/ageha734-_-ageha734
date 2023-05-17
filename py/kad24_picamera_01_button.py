import picamera
import time 

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

SW = 7
LED = 11

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(SW,GPIO.IN)
i = 1
try:
    while 1:
        key_in = GPIO.input(SW)

        if key_in == 1:
            print("SWが押された")

            with picamera.PiCamera() as camera:
                res = camera.resolution = (320,240)

                filename = "pict"

                camera.capture(filename + str(i) + '.jpeg')
                i += 1
        else:
            print("SW 離れた")
        time.sleep(0.2)

except KeyboardInterrupt:
    pass
GPIO.cleanup()

