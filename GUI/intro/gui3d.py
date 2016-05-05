from __future__ import print_function
from Tkinter import *
import sys

class HelloClass:
	def __init__(self):
		self.msg = "Goodbye from __call__"

	def __call__(self):
		print(self.msg)
		sys.exit()


w = Button(None, text="Hello again", command = HelloClass())
w.pack()
w.mainloop()



