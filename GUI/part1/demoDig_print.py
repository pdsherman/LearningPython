from Tkinter import *
from dialogTable import demos
from quitter import Quitter

class Demo(Frame):
	def __init__(self, parent=None, **options):
		Frame.__init__(self, parent, **options)
		self.pack()
		Label(self, text='Demos: printit()').pack()
		for key in demos:
			func = (lambda key = key: self.printit(key))
			Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
		Quitter(self).pack(side=TOP, fill=BOTH)

	def printit(self, name):
		print(name, "returns => ", demos[name]())

if __name__ == '__main__':
	Demo().mainloop()
