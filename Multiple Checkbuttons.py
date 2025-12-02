from tkinter import *

win = Tk()
win.title('Multiple Checkbuttons')
win.geometry('600x400+50+50')

def checked(): 
    l['text'] = c['text'] if var.get() == 1 else ' '
    l['text'] += c1['text'] if var1.get() == 1 else ' '
    l['text'] += c2['text'] if var2.get() == 1 else ' '


def clicked(): 
    # c.select()
    # c.toggle() # select and toggle won't generate event i.e. label doesn't change
    c.invoke()

l = Label(win, text='Label')
l.pack()

var = IntVar()
c = Checkbutton(win, text='Java', variable=var, command=checked)
c.pack()

var1 = IntVar()
c1 = Checkbutton(win, text='Python', variable=var1, command=checked)
c1.pack()

var2 = IntVar()
c2 = Checkbutton(win, text='C++', variable=var2, command=checked)
c2.pack()


win.mainloop()