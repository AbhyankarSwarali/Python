from tkinter import *

win = Tk()
win.title('Text')
win.geometry('600x300+80+50')

def Undo(): 
    try:
        # txt.edit_undo()
        print(txt.get(1.0, 2.4)) # fron line 1 char 0th to line 2 char 4th
    except Exception as e: 
        print('Nothing to Undo')

def Redo(): 
    try:
        txt.edit_redo()
    except Exception as e:
        print('Nothing to Redo')


# vert_scroll = Scrollbar(win, orient=VERTICAL)
# vert_scroll.pack(side=RIGHT, fill=Y)

txt = Text(win, undo=True) # can add: yscrollcommand=vert_scroll.set inside Text()
txt.pack() # side=LEFT

undo_btn = Button(win, text='Undo', command=Undo)
undo_btn.pack()

redo_btn = Button(win, text='Redo', command=Redo)
redo_btn.pack()

# vert_scroll['command'] = txt.yview

win.mainloop()