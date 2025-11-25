from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Event Modifiers')
win.geometry('600x400+50+50')

def fun(e):
    showinfo('My Box', 'Event is generated')


e = Entry(win, bg='red', fg='yellow')
e.place(x=75, y=50, width=300, height=30)

e1 = Entry(win, bg='red', fg='yellow')
e1.place(x=75, y=90, width=300, height=30)

e.bind('<Double - Button>', fun)
e1.bind('<Double - Button>', fun)

win.mainloop()