from tkinter import *

win = Tk()
win.title('Place')
win.geometry('600x400')

b1 = Button(win, text='Button 1', bg='lightblue', fg='blue')
# b2 = Button(win, text='Button 2', bg='lightblue', fg='blue')
# b3 = Button(win, text='Button 3', bg='lightblue', fg='blue')
# b4 = Button(win, text='Button 4', bg='lightblue', fg='blue')

b1.place(relx=0.5, rely=0.5, relwidth=0.20, relheight=0.10)
# b2.place(x=200, y=150, width=100, height=50)
# b3.place(x=300, y=200, width=100, height=50)
# b4.place(x=300, y=100, width=100, height=50)


win.mainloop()