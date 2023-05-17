import tkinter as tk

root = tk.Tk()


c = tk.Canvas(root,width = 500,height = 500)


c.pack()

c.create_line(0,0,50,50)

c.create_rectangle(100,100,150,150,fill = 'red')

c.create_oval(100,200,150,250,fill = 'blue')

# c.create_ploygon(250,200,350,200,400,250,400,350,350,400,250,400,200,350,200,250,fill = 'green')
c.reate_ploygon(250,200,350,200,400,250,400,350,350,400,250,400,200,350,200,250,fill = 'green')
root.mainloop()