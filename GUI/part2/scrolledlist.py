"""
Example 9-9 from "Programming Python"

Simple customizable scrolled listbox component
"""
from Tkinter import *

class ScrolledList(Frame):
	def __init__(self, options, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.makeWidgets(options)

	def handleLists(self, event):
		index = self.listbox.curselection() #on list double-click
		label = self.listbox.get(index)     #fetch selection text
		self.runCommand(label)              #and call actions here 

	def makeWidgets(self, options):
		sbar = Scrollbar(self)
		list = Listbox(self, relief=SUNKEN)
		sbar.config(command=list.yview)
		list.config(yscrollcommand=sbar.set) #move one moves other

		sbar.pack(side=RIGHT, fill=Y) #list clipped first
		list.pack(side=LEFT, expand=YES, fill=BOTH)

		pos = 0
		for label in options:
			list.insert(pos, label) #or .insert(END, label)
			pos += 1

		list.bind('<Double-1>', self.handleLists)
		self.listbox=list

	def runCommand(self, selection):
		print('Selection: ' + selection)


if __name__ == "__main__":
	options = (('Lumberjack-%s' % x) for x in range(20))
	ScrolledList(options).mainloop()
