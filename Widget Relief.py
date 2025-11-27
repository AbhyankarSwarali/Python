from tkinter import *

win = Tk()
win.title('Widget Relief')
win.geometry('600x400+50+50')

b = Button(win, text='Python', relief=RIDGE, overrelief=SUNKEN)
b.pack()

win.mainloop()