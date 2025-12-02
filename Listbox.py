from tkinter import *

win = Tk()
win.title('Listbox 1')
win.geometry('600x400+50+50')

lst = Listbox(win, activestyle=DOTBOX, selectmode=SINGLE)
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

lst.insert(5, 'DJango')
print(lst.get(3, last=7))
lst.delete(5)

lst.itemconfig(3, background='red', foreground='yellow')
print('Background colour:', lst.itemcget(3, 'background'))

lst.selection_set(3,8)
lst.selection_clear(4,6)
print(lst.selection_includes(7))

print('Total items:', lst.size())
lst.see(13)

win.mainloop()