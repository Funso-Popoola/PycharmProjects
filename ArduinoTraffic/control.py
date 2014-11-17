__author__ = 'funso'

import glob
import serial
import time
from Tkinter import *

green = 0
yellow = 1
red = 2

led = []

canvas = None
color = ["green", "yellow", "red"]

def control(input):

    print(input)
    port_list = glob.glob1("/dev", "tty[A-z]*")
    print port_list

    for port in port_list:
        if ("ttyACM" in port):
            print "Got in..."
            try:
                s = serial.Serial("/dev/" + port, 9600)
                #s.setBaudrate(9600)
                s.write(input[0])
                print "Written to ", port
                s.close()
            except(OSError, "Unable to communicate with the Serial port"):
                pass
            break


def gui():
    root = Tk()
    canvas = Canvas(root, height="500", width="500", bg="cyan")


    diameter = 50

    for i in range(3):
        y1 = 30 + i * (diameter + 30)
        x = 400
        y2 = y1 + 50

        circle = canvas.create_oval(x, y1, x + diameter, y2, fill=color[i])
        led.append(circle)

    canvas.create_rectangle(x - 10, 20, x + diameter + 10, y2 + 10)
    b = Button(master=root, text="Green", anchor=NE, command=control("green"))
    b.pack()
    canvas.pack()
    root.mainloop()

def onLed(index):
    canvas.itemconfigure(led[index], fill=color[index])

def offLed(index):
    canvas.itemconfigure(led[index], fill="white")

"""
    def automatic():
        onLed(green)
        print "green is on"
        time.sleep(5000)
        canvas.update_idletasks()

        offLed(green)
        onLed(yellow)
        time.sleep(5000)
        canvas.update_idletasks()

        offLed(yellow)
        onLed(red)
        time.sleep(5000)
        canvas.update_idletasks()

        offLed(red)

    canvas.pack()
    root.mainloop()
    root.quit()
    #automatic()

"""


gui()
#control("red")