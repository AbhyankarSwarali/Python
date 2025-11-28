from tkinter import *

win = Tk()
win.title('Command Options')
win.geometry('400x400+50+50')

scroll = Scrollbar(win, orient=VERTICAL)
t = Text(win)

t.config(yscrollcommand=scroll.set)
scroll.config(command=t.yview)

scroll.pack(side=RIGHT, fill=Y)
t.pack(side=LEFT, fill=Y)


win.mainloop()