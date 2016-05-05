from __future__ import print_function
from Tkinter import *
import sys

def greeting():
	print("Hello from 4")

win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='Hello', command=greeting).pack(side=LEFT, expand=YES, fill=Y)
Label(win, text="Label for GUI4").pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

win.mainloop()
