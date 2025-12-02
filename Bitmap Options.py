from tkinter import *

win = Tk()
win.title('Bitmap options')
win.geometry('400x200+100+50')

b = Button(win, text='Button 1', bitmap='questhead')
b.pack()

win.mainloop()