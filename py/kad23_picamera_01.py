import picamera

import time

with picamera.PiCamera() as camera:

    res = int(input('Resolution(1:320x240,2:640x480,3:1024x768)?'))

    if res == 3:
        camera.Resolution = (1024,768)
    elif res == 2:
        camera.Resolution = (640,480)
    else:
        camera.Resolution = (320,240)

    filename = input('File Name?')

    camera.start_preview()

    time.sleep(1)

    camera.stop_preview()
    camera.capture(filename + '.jpg')