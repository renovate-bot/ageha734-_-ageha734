import tkinter as tk


root = tk.Tk()


c = tk.Canvas(root,width = 200,height = 200)


c.pack()


cc = c.create_oval(50,50,200,200,fill = '')

def func():
    print("func")
    c.itemconfig(cc,fill="red")

def func_leave(ev):
    print("func_leave")
    c.itemconfig(cc,fill="")



button = tk.Button(root, text = "Push!",command=func)

button.bind('<Leave>',func_leave)



button.pack()


root.mainloop()