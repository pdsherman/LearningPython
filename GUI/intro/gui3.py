from Tkinter import *

def quit():
	print('Good bye')
	sys.exit()


widget = Button(None, text="Hello", command=quit)
widget.pack(expand=YES, fill=X) #can also do fill=BOTH
widget.mainloop()
