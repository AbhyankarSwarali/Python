from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title('Modifying Widget Options')
win.geometry('600x400+50+50')

def my_handler(e):
    print(label.cget('text'))

    showinfo('My box', label['bg'])
    label['bg'] = 'red'

    showinfo('My box', label.cget('bg'))
    label.config(bg='black')


def entry(e):
    label['bg'] = 'red'
    label['fg'] = 'yellow'
    label['text'] = 'Nice to meet you'

def exit(e):
    label['bg'] = 'blue'
    label['fg'] = 'white'
    label['text'] = 'Hello World'


def single_handler(e):
    if int(e.type) == 7:
        label['bg'] = 'red'
        label['fg'] = 'yellow'
        label['text'] = 'Nice to meet you'
    elif int(e.type) == 8:
        label['bg'] = 'blue'
        label['fg'] = 'white'
        label['text'] = 'Hello World'

        print(type(e.type))


label = Label(win, text='Hello World', bg='blue', fg='white', width=20, height=2)
label.pack()

label.bind('<Button-1>', my_handler)

label.bind('<Enter>', entry)
label.bind('<Leave>', exit, add='+')

label.bind('<Enter>', single_handler)
label.bind('<Leave>', single_handler, add='+')

win.mainloop()