#coding: utf-8

import tkinter as tk

def func():
    label.config(text = 'Pushed')



def func_event(ev):
    label.config(text = 'Push Button')

def func_in_carsol(ev):
    label.config(text = 'Push???')

    
root = tk.Tk()

label = tk.Label(root, text = "Push Button",height = 5,width = 20)

button = tk.Button(root, text = "Push!", command = func)


label.pack()

button.pack()

button.bind('<Enter>' , func_in_carsol)


button.bind('<Leave>' , func_event)

root.mainloop()