from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Event Class')
win.geometry('600x400+50+50')

def my_handler(e):
    print(e)
    # print(e.state)
    # print(e.x_root, e.y_root)
    
    # print(e.keycode)
    # print(e.keysym_num)
    # print(e.type)

ent = Entry(win)
ent.pack()
# ent.bind('<Button-1>', my_handler)
ent.bind('<KeyPress>', my_handler)


win.mainloop()