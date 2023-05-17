import RPi.GPIO as GPIO

import tkinter as tk

import time

GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED,GPIO.OUT,initial = GPIO.LOW)

def func():
    GPIO.output(LED,not GPIO.input(LED))

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
                
    
root = tk.Tk()

label = tk.Label(root,text="press button")

label.pack()

button = tk.Button(root,text='LED',command=sos)

button.pack()

root.mainloop()

GPIO.cleanup()