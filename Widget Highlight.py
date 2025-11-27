from tkinter import * 

win = Tk()
win.title('Widget Highlight')
win.geometry('600x400+50+50')

e1 = Entry(win, highlightbackground='red', 
            highlightthickness=5, highlightcolor='yellow')
e1.pack(pady=10)

b1 = Button(win, text='Button 1', takefocus=0)
b1.pack()

c1 = Checkbutton(win, text='Yes', indicatoron=True)
c1.pack()


win.mainloop()