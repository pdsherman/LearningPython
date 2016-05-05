from Tkinter import *

imgdir = "./"

win = Tk()
igm = PhotoImage(file="LoonyGears.gif")
Button(win, image=igm).pack()
win.mainloop()
