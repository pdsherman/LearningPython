"""
Quit button that verifies exit requests;
To reuse, attach an instance to other GUIs,
and repack as desired
"""
from Tkinter import *
from tkMessageBox import askokcancel

class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		widget=Button(self, text='Quit', command=self.quit).pack(side=LEFT, expand=YES, fill=BOTH)

	def quit(self):
		ans = askokcancel("Verify exit", "Really quit?")
		if ans:
			Frame.quit(self)

if __name__ == '__main__':
	Quitter().mainloop()
