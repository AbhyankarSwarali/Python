import tkinter as tk
import tkinter.messagebox as msg

win = tk.Tk()
win.title('MessageBox')
win.geometry('600x400+50+50')

def clicked(): 
    # ans = msg.askyesno('My', 'Do you want to continue?')
    # ans = msg.askokcancel('My', 'Do you want to continue?', default='cancel') # highlights the option
    # ans = msg.askokcancel('My', 'Do you want to continue?', default='cancel', parent=win) # dialog box appears in the parent window
    ans = msg.askquestion('My','Do you want ot continue', default='no') # can also add: parent=win
    print(ans)

btn = tk.Button(win, text='Click Me', command=clicked)
btn.pack()



win.mainloop()