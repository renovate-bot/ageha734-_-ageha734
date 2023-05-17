#coding: utf-8

import tkinter as tk


root = tk.Tk()

def func1():
    label.config(text = sel.get())
def func2():
    label.config(text = sel.get())
    
sel = tk.IntVar()

sel.set(1)

label = tk.Label(root,text = "Select Button")

label.pack()

rb1 = tk.Radiobutton(root,text = "Button 1",variable = sel,value = 1,command = func1)

rb1.pack()

rb2 = tk.Radiobutton(root , text = 'Button 2' , variable = sel,value = 2,command = func2)

rb2.pack()

root.mainloop
root.mainloop()