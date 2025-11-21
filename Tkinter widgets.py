from tkinter import * 

win = Tk()
win.title('Tkinter Widgets')
win.geometry('600x400+100+100')

'''
l = Label(win,text='Hello World')
l.pack()

b = Button(win, text='Click Me')
b.pack()

l = Label(win, text='Name')
l.pack()
e = Entry(win)
e.pack()

t = Text(win, width=30, height=10)
t.pack()

c1 = Checkbutton(win, text='Yes')
c2 = Checkbutton(win, text='No')
c3 = Checkbutton(win, text='None')
c1.pack()
c2.pack()
c3.pack()

r1 = Radiobutton(win, text='Yes', variable='v', value=1)
r2 = Radiobutton(win, text='No', variable='v', value=2)
r1.pack()
r2.pack()

v = StringVar()
o = OptionMenu(win, v, 'Python', *('JavaScript', 'R', 'Java', 'C++'))
o.pack()

s = Scale(win, from_=0, to=50)
s.pack()
'''

win.mainloop()