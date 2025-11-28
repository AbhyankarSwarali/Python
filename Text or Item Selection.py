from tkinter import *

win = Tk()
win.title('Text/Item selection')
win.geometry('600x400+50+50')

e = Text(win, selectbackground='red', selectforeground='yellow', selectborderwidth=10)
e.pack()

lb = Listbox(win, selectbackground='red', selectforeground='yellow', 
             selectborderwidth=10, exportselection=False)
lb.insert(0, 'Python')
lb.insert(1, 'Java')
lb.insert(2, 'C++')
lb.insert(3, 'JavaScript')
lb.pack()


win.mainloop()