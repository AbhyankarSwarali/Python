from tkinter import *
from tkinter.messagebox import *
 
win = Tk()
win.title('Instance Level Handling')
win.geometry('600x400+50+50')

def button(e): 
    # print('Event is generated')
    showinfo('My Box', 'Event is generated')

def fun(msg):
    print(msg)

e = Entry(win, bg='red', fg='yellow')
e.place(x=100,y=30, width=300, height=40)

e.bind('<Button>', button)
e.bind('<Enter>', lambda event1:fun('Mouse pointer entered'))
e.bind('<Leave>', lambda event2:fun('Mouse pointer left'))
e.bind('<KeyPress>', lambda event3:fun('Keyboard key pressed'))

win.mainloop()