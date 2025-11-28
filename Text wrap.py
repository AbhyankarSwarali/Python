from tkinter import *

win = Tk()
win.title('Text Wrap')
win.geometry('600x400+50+50')

t = Text(win, wrap=WORD, spacing2=10)
t.pack()

l = Label(win, text='abcdefghijklmnopqrstuvwxyz', wraplength=100)
l.pack()

win.mainloop()