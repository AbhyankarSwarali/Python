from tkinter import *

win = Tk()
win.title('Multiple Checkbuttons')
win.geometry('600x400+50+50')

def checked(): 
    l['text'] = var.get()


def clicked(): 
    # c.select()
    c.invoke()

l = Label(win, text='Label')
l.pack()

var = StringVar()
c = Radiobutton(win, text='Java', variable=var, value='Java', command=checked)
c.pack()

c1 = Radiobutton(win, text='Python', variable=var, value='Python', command=checked)
c1.pack()

c2 = Radiobutton(win, text='C++', variable=var, value='C++', command=checked)
c2.pack()


win.mainloop()