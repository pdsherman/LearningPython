from __future__ import print_function
from Tkinter import *
from quitter import Quitter

demoModules = ['demoDig', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
	for demo in demoModules:
		module = __import__(demo)
		part = module.Demo(root) # could be: .Demo(root, bd=6, relieft=GROOVE) and get rid of .config() line
		#Previous 2 lines could also be:
		#exec('from %s import Demo' % demo)
		#part = eval('Demo')(root)
		part.config(bd=6, relief=GROOVE)
		part.pack(side=LEFT, expand=YES, fill=BOTH)
		parts.append(part)

def dumpState():
	for part in parts:
		print(part.__module__ + ':', end=' ')
		if hasattr(part, 'report'):
			part.report()
		else:
			print('none')

root = Tk()
root.title('Frames')
Label(root, text='Multiple frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
