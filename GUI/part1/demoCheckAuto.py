
from __future__ import print_function
from Tkinter import *

root = Tk()
states = []

for i in range(10):
	var = IntVar()
	chk = Checkbutton(root, text=str(i), variable=var)
	chk.pack(side=LEFT)
	states.append(var)

Button(root, text='States', command = lambda : print([var.get() for var in states])).pack(side=BOTTOM)

root.mainloop()
print([var.get() for var in states])
# print(list(map(IntVar.get, states)))
# print(list(map(lambda var: var.get(), states)))
