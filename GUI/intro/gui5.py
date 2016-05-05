from __future__ import print_function
from Tkinter import *
import sys

class HelloButton(Button):
	def __init__(self, parent=None, **config):
		Button.__init__(self, parent, **config)
		self.pack()
		self.config(command=self.callback, fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)

	def callback(self):
		print('Goodbye')
		self.quit()

if __name__ == '__main__':
	HelloButton(text="Hello").mainloop()
