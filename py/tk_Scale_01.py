#coding: utf-8

import tkinter as tk


root = tk.Tk()

val = tk.IntVar()

val.set(0)

def func(scl):
    label.config(text = 'Value %d' % int(scl))

label = tk.Label(root, text = 'Value %d' % val.get())

label.pack()

s = tk.Scale(root , label = 'Scale' ,orient = 'h' , from_ = 0,to = 255, showvalue =
             False , variable = val,command = func)

s.pack()

root.mainloop()