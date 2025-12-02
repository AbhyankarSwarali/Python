from tkinter import *
from tkinter.font import *

win = Tk()
win.title('Counter')
win.geometry('600x400+50+50')

def clicked(): 
    l['text'] += 1
    # var.set(var.get() + 1)

fnt = Font(family='Arial', size=15)

# var = IntVar(value=0)
# l = Label(win, textvariable=var, font=fnt)
l = Label(win, text=0, font=fnt)
l.pack(pady=10)

b = Button(win, text='Click to count', font=fnt, command=clicked)
b.pack()


win.mainloop()