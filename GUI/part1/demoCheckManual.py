from __future__ import print_function
from Tkinter import *

states = []

def onPress(i):
	states[i] = not states[i]

root = Tk()
for i in range(10):
	chk = Checkbutton(root, text = str(i), command = (lambda i=i: onPress(i)) )
	chk.pack(side=LEFT)
	states.append(False)

Button(root, text='States', command = lambda : print(states)).pack(side=TOP)

root.mainloop()
print(states)
