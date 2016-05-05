from __future__ import print_function
import Tkinter as tk
import sys

def hello(event):
	print("Double click right mouse button to exit")

def quit(event):
	print("Hello, I must be going...")
	sys.exit()

wid = tk.Button(None, text="Hello event")
wid.pack()
wid.bind('<Button-1>', hello)
wid.bind('<Double-3>', quit)
wid.mainloop()


