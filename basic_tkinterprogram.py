#Tejashri Pardeshi
#tkinter
#blank from
##import tkinter
##win = tkinter.Tk()
##win.mainloop()


##from tkinter import *
##m = Tk()
##m.geometry("800x600")
###to set the minimum size
##m.minsize(200,800)
###set the maximum size
##m.maxsize(1000,800)
##m.mainloop()


#label example
##from tkinter import *
##m = Tk()
##m.geometry("800x600")
###Label(m,text="This is the Label").pack()
##l1 = Label(m,text="This is the Label")
##l1.pack()
##m.mainloop()


#display png image
##from tkinter import *
##m = Tk()
##m.geometry("800x600")
##photo = PhotoImage(file= "C:\\Users\\TEJASHRI\\Pictures\\Screenshots\\Screenshot (3).png")
##Label(m,image=photo).pack()
##m.mainloop()


#display jpg image
##from tkinter import *
##from PIL import Image,ImageTK
##m = Tk()
##m.geometry("800x600")
##photo = Image.open("C:\Users\TEJASHRI\Desktop\htmlncss\\flower.jpg")
##image = photo.resize((200,200))
##img = ImageTk.PhotoImage(image)
##Label(m,image=img).pack()
##m.mainloop()

#Label Properties
from tkinter import *
m = Tk()
m.geometry("800x600")
l1 = Label(text="This is the Babel Property",
           font=('Arial',20,"bold"),
           bg= 'red',
           fg = 'white',
           padx=45,
           pady=45,
           borderwidth=15,
           relief=RIDGE
           )
l1.pack()
m.mainloop()
