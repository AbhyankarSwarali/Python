from tkinter import *

win = Tk()
win.title('Spinbox')
win.geometry('600x400+50+50')

def item(): 
    var.set(spin.get())

    # spin.selection('to', 5)
    # spin.selection('range', 1, 4)
    # spin.selection_get()

lst = ['Amazon', 'Flipkart', 'eBay', 'Myntra', 'Meesho', 'Snapdeal']

var = StringVar()
ent = Entry(win, textvariable=var)
ent.pack()

# spin = Spinbox(win, from_=0, to=10, increment=0.5)
spin = Spinbox(win, values=lst)
spin.pack(pady=10)

btn = Button(win, text='Select', command=item)
btn.pack()


win.mainloop()