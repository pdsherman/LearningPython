from Tkinter import *

root = Tk()
var = IntVar(0)

for i in range(10):
	rad = Radiobutton(root, text=str(i), value=i, variable=var).pack(side=LEFT)

root.mainloop()
print(var.get())
