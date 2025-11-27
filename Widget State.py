from tkinter import *

win = Tk()
win.title('Widget State')
win.geometry('600x400+50+50')

b1 = Button(win, text='Button 1', state=DISABLED, disabledforeground='red')
b1.pack()

b2 = Button(win, text='Button 2', state=ACTIVE, activebackground='red', activeforeground='yellow')
b2.pack(pady=5)

l1 = Listbox(win, activestyle=UNDERLINE) #activestyle = DOTBOX
l1.insert(0,'Python')
l1.insert(1,'Java')
l1.insert(2,'C++')
l1.insert(3,'JavaScript')
l1.pack()


win.mainloop()