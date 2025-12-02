from tkinter import *
from tkinter.font import *

win = Tk()
win.title('Scale')
win.geometry('600x400+50+50')

def size(e): 
    f = Font(size=str(sc.get()))
    ent['font'] = f

var = StringVar(value='Python')
ent = Entry(win, textvariable=var)
ent.pack()

sc = Scale(win, from_=1, to=20, resolution=5, tickinterval=5, 
           showvalue=False, sliderlength=20, command=size)
sc.pack()


win.mainloop()