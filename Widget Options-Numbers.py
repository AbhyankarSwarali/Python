from tkinter import *

win = Tk()
win.title('Numeric Options')
win.geometry('400x400+50+50')

spin = Spinbox(win, from_=0, to=100, format='%2.2f') # try: Scale
spin.pack()

var = IntVar(value=25)
scale = Scale(win, variable=var, from_=0, to=100, orient=HORIZONTAL)
scale.pack()


win.mainloop()