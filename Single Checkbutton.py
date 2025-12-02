from tkinter import *

win = Tk()
win.title('Checkbutton')
win.geometry('600x400+50+50')

def checked(): 
    l['text'] = c['text'] if var.get() == 1 else 'Label'


def clicked(): 
    # c.select()
    # c.toggle() # select and toggle won't generate event i.e. label doesn't change
    c.invoke()

l = Label(win, text='Label')
l.pack()

var = IntVar()
c = Checkbutton(win, text='Java', variable=var, command=checked)
c.pack()

b = Button(win, text='Click Me', command=clicked)
b.pack()

win.mainloop()