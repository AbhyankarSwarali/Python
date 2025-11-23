from tkinter import *

win = Tk()
win.title('Event Handling')
win.geometry('600x400+50+50')

def fun(msg): 
    print(msg)

b1 = Button(win, text='Button', command=lambda:fun('Button is clicked'))
b1.pack()
c1 = Checkbutton(win, text='Checkbutton', command=lambda:fun('Checkbutton is selected'))
c1.pack()
r1 = Radiobutton(win, text='Radiobutton', command=lambda:fun('Radiobutton is selected'))
r1.pack()


win.mainloop()