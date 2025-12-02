from tkinter import *

win = Tk()
win.title('Entry')
win.geometry('600x400+50+50')

def my_handler(txt): 
    if txt.isdigit(): 
        return False
    else: 
        return True
    
handle = (win.register(my_handler), '%S')

var = StringVar(value='Python')
# ent = Entry(win, textvariable=var, show='*')
ent = Entry(win, textvariable=var, validate='key', validatecommand=handle)
ent.pack()

# ent.focus()
# ent.icursor(4)
# ent.select_range(2,10)

# ent.insert(0, 'ABCD')
# ent.delete(0,3)


win.mainloop()