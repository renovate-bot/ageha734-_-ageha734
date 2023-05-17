import spidev

import tkinter as tk
import time 

spi = spidev.SpiDev()

spi.open(0,0)
spi.max_speed_hz=1000000

spi.bits_per_word = 8

dummy = 0xff

start = 0x47

sgl = 0x20

ch0 = 0x00

ch1 = 0x10

msbf = 0x08

def measure(ch):
    ad = spi.xfer2([(start + sgl + ch + msbf), dummy])
    val = (((ad[0] & 0x03) << 8) + ad[1] ) -512
    return val

pre_ch0 = measure(ch0)

pre_ch1 = measure(ch1)

root = tk.Tk()

c = tk.Canvas(root,width = 500,heigh = 500)

c.pack()

# cc = c.create_oval(200,200,220,220,fill = 'blue')
cc = c.create_oval(pre_ch0,pre_ch1,pre_ch0 + 20,pre_ch1 + 20,fill = 'blue')

def check_AD():
    global pre_ch0
    global pre_ch1
    mes_ch0 = (measure(ch0)+512)/2
    mes_ch1 = (measure(ch1)+512)/2
    print('ch0 = %2.0f' % mes_ch0,',ch1 = %2.0f' % mes_ch1)

    diff = [ (mes_ch0-pre_ch0),(mes_ch1 - pre_ch1)]
    pre_ch0,pre_ch1 = mes_ch0,mes_ch1
    print(diff)
    return diff

def draw():
    diff = check_AD()
    c.move(cc,diff[0],diff[1])

    root.after(50,draw)

draw()

root.mainloop()
