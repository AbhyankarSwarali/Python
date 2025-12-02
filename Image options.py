from tkinter import *

win = Tk()
win.title('Image options')
win.geometry('400x400+100+50')

bird = PhotoImage(file='Bird.gif')
cat = PhotoImage(file='Cat.png')
xbm = BitmapImage(file='cat_xbm.xbm')

l1 = Label(win, text='Birdyy', image=bird)
l1.pack()

l2 = Label(win, text='Kitty', image=cat)
l2.pack()

l3 = Label(win, text='Cat_xbm', image=xbm)
l3.pack()

win.mainloop()