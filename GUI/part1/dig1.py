from Tkinter import *
from tkMessageBox import *

def callback():
	if askyesno("verify: Do you want to quit?"):
		showwarning('Yes', 'Quit not yet implemented')
	else:
		showinfo('No', 'Quit has been cancelled')

errmsg="Sorry"
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('spam',errmsg))).pack(fill=X)
mainloop()
