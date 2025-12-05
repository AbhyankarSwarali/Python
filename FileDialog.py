from tkinter import *
from tkinter.filedialog import *

win = Tk()
win.title('File Dialog')
win.geometry('600x400+50+50')

def Open(): 
    fname = askopenfile()
    txt = fname.read()
    text.insert('1.0', txt)


def Save(): 
    fname = asksaveasfile()
    fname.write(text.get('1.0', 'end-1c'))

def Clear(): 
    text.delete('1.0', 'end-1c') # gives last character of the last line of text widget

text = Text(win)
text.pack()

b1 = Button(win, text='Open', width=5, command=Open)
b1.pack()

b2 = Button(win, text='Save', width=5, command=Save)
b2.pack()

b3 = Button(win, text='Clear', width=5, command=Clear)
b3.pack()


win.mainloop()