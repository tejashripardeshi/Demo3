#button demo
from tkinter import *
m = Tk()
m.geometry("700x400")

def printevent():
    print("print click")
def submitevent():
    print("submit click")
def clearevent():
    print("clear click")
def deleteevent():
    print("delete click")

f1 = Frame(m,bg='grey',borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1 = Button(f1,fg="red",text="Print",command=printevent)
b1.pack(side=LEFT,padx=25)
b2 = Button(f1,fg="red",text="Print",command=submitevent)
b2.pack(side=LEFT,padx=25)
b3 = Button(f1,fg="red",text="Print",command=clearevent)
b3.pack(side=LEFT,padx=25)
b4 = Button(f1,fg="red",text="Print",command=deleteevent)
b4.pack(side=LEFT,padx=25)
m.mainloop()
