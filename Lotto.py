import random
from tkinter import *

def Lotto_No():
    ci = random.sample(range(1, 50), 6)
    num1.set(ci[0])
    num2.set(ci[1])
    num3.set(ci[2])
    num4.set(ci[3])
    num5.set(ci[4])
    num6.set(ci[5])
    return

Lottery = Tk()
Lottery.geometry('800x360')
frame = Frame(Lottery)
frame.pack()

Lottery.title("Lottery Number Generator")

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Numbers Generate")
frame1 = Frame(Lottery)
frame1.pack(side=TOP)
label = Label(frame1, textvariable=var, font=("Arial", 48), width = 24)
label.pack(side=TOP)
label = Label(frame1, textvariable="", width = 24)
label.pack(side=TOP)
label = Label(frame1, textvariable="", width = 24)
label.pack(side=TOP)

frame2 = Frame(Lottery)
frame2.pack(side=TOP)
txtDisplay = Entry(frame2, textvariable=num1, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num2, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num3, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num4, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num5, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num6, bd=20, insertwidth=1, font=("Arial", 30), justify="center", width=4)
txtDisplay.pack(side=LEFT)

frame3 = Frame(Lottery)
frame3.pack(side=TOP)
label = Label(frame3, textvariable="", height = 2)
label.pack(side=TOP)
button1 = Button(frame3, padx=8, width=18, pady=8, bd=8, font=("Arial", 26), text  = "Lotter Number Generator", bg="powder blue", command=Lotto_No)
button1.pack(side=TOP)



Lottery.mainloop()