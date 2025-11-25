from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Event Modifiers')
win.geometry('600x400+50+50')

def fun(e):
    showinfo('My Box', 'Mouse key pressed')

def fun1(e):
    # showinfo('My Box', e) # We called the upper event therefore, it prints upper events infor
    # shows which key is pressed along with some weird code, character and x and y coords (not accurate).
    # showinfo('My box', e.char) # shows only which letter/character is pressed
    showinfo('My box', 'Keyboard key pressed')

def fun2(e):
    showinfo('My Box', 'Mouse pointer entered widget')


e = Entry(win, bg='red', fg='yellow')
e.place(x=75, y=50, width=300, height=30)

e.bind('<Button-1>', fun)
e.bind('<KeyPress>', fun1, add='+')
e.bind('<Motion>', fun2, add='+')

win.mainloop()