from tkinter import *

win = Tk()
win.title('Widget Style')
win.geometry('600x400+50+50')

b1 = Button(win, text='Button 1', bd=1, anchor=SW, width=10, height=3, fg='yellow', bg='red')
b1.pack()


win.mainloop()