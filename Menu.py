from tkinter import *

win = Tk()
win.title('Menu')
win.geometry('600x400+50+50')

def add_text(): 
    txt.insert(1.0, 'Python programming language')

def pop_handler(e): 
    file.tk_popup(e.x_root, e.y_root, 0)


txt = Text(win)
txt.pack(fill=BOTH)

menubar = Menu(win)
win['menu'] = menubar

file = Menu(menubar)
menubar.add_cascade(label='File', menu=file)

file.add_command(label='New', command=add_text)
file.add_command(label='Open')
file.add(itemType='command', label='Save')
file.add_separator()
file.add_checkbutton(label='Save As', onvalue=1, offvalue=0)

rad = Menu(file)
rad.add_radiobutton(label='Option 1')
rad.add_radiobutton(label='Option 2')
rad.add_radiobutton(label='Option 3')
file.add_cascade(label='More options..', menu=rad)

txt.bind('<Button-3>', pop_handler)

win.mainloop()