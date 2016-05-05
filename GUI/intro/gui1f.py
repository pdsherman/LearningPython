from Tkinter import *

root = Tk()
widget = Label(root)
widget.config(text="Hello")
widget.pack(side=TOP, expand = YES, fill=BOTH)
root.title('gui.py')
root.mainloop()
