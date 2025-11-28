from tkinter import *

win = Tk()
win.title('Insertion Cursor')
win.geometry('600x400+50+50')

t = Text(win, insertbackground='red', insertwidth=10, insertborderwidth=5, 
         insertofftime=70, insertontime=70, cursor='heart')
t.pack()



win.mainloop()