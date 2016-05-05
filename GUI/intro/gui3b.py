from __future__ import print_function
from Tkinter import *

def quit():
	print('Good bye')
	sys.exit()

def quit2(X, s):
	print(str(X) + " and " + s)
	sys.exit()

num = 42
#widget = Button(None, text="Hello", command=quit)
#widget = Button(None, text="Hello", command=(lambda: print("Goodbye") or sys.exit()) )
widget = Button(None, text="Hello", command = (lambda X=num: quit2(num, 'more')) )
num = 43
widget.pack(expand=YES, fill=X) #can also do fill=BOTH
widget.mainloop()
