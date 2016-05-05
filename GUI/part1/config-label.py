from __future__ import print_function
from Tkinter import *
import sys

root = Tk()
labelfont = ('times', 20, 'bold') #family, size, style
widget = Label(root, text = 'Config')
widget.config(bg='black', fg='#ae0fda', font=labelfont, height=3, width=20)
widget.config(cursor='gumby')
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
