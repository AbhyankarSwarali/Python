from tkinter import *

win = Tk()
win.title('Listbox 2')
win.geometry('600x400+50+50')

def clicked(e):
    var.set(lst.curselection())

var = StringVar()
ent = Entry(win, textvariable=var)
ent.pack()

lst = Listbox(win, activestyle=DOTBOX, selectmode=EXTENDED)
lst.insert(0, 'Python')
lst.insert(1, 'Java')
lst.insert(2, 'C++')
lst.insert(3, 'JavaScript')
lst.insert(4, 'Ruby')
lst.insert(5, 'C Lang')
lst.insert(6, 'PHP')
lst.insert(7, 'C#')
lst.insert(8, 'R')
lst.insert(9, 'Swift')
lst.insert(10, 'Android')
lst.insert(11, 'VB')
lst.insert(12, 'PERL')
lst.insert(13, 'Kotlin')
lst.insert(14, 'Go')
lst.insert(15, 'Scala')
lst.pack()

# btn = Button(win, text='Click Me', command=clicked)
btn = Button(win, text='Click Me')
btn.pack()

lst.bind('<<ListboxSelect>>', clicked)


win.mainloop()