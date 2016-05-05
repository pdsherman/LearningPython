from __future__ import print_function
from Tkinter import *
import sys

class HelloClass:
	def __init__(self):
		widget = Button(None, text="Hello again", command=self.quit)
		widget.pack(expand=YES, fill=X)

	def quit(self):
		print("Goodbye")
		sys.exit()

HelloClass()
mainloop()



