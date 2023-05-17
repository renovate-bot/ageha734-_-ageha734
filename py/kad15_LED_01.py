import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

LED = 11

def sos():
        for num in range(3):
                GPIO.output(LED,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(LED,GPIO.LOW)
                time.sleep(0.2)
        for num in range(3):
                GPIO.output(LED,GPIO.HIGH)
                time.sleep(0.6)
                GPIO.output(LED,GPIO.LOW)
                time.sleep(0.2)
        for num in range(3):
                GPIO.output(LED,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(LED,GPIO.LOW)
                time.sleep(0.2)
        
       

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

try:
    while 1:
        sos()
        time.sleep(1.0)
    
            
except KeyboardInterrupt:
        pass
GPI0.cleanup()
            
            