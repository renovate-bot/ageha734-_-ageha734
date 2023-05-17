#coding: utf-8

import tkinter as tk
import random 


root = tk.Tk()

def func(ev):
    
    if num1 + num2 == int(e.get()):
        label.config(text = str(num1) + '+' + str(num2) + '=' + e.get() + '  ok')
        return
    label.config(text = str(num1) + '+' + str(num2) + '=' + e.get() + '  mistake')

    
num1 = random.randrange(10**2,999)
num2 = random.randrange(10**2,999)

msg = str(num1) + '+' + str(num2) + '=?'
    
label = tk.Label(root, text = msg)

label.pack()

e = tk.Entry(root)

e.pack()

e.bind('<Return>' ,func)

root.mainloop()
