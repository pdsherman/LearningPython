from __future__ import print_function
from Tkinter import *

def showPosEvent(event):
	print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def showAllEvent(event):
	print(event)
	for attr in dir(event):
		if not attr.startswith('__'):
			print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
	print('Got key press:', event.char)

def onArrowKey(event):
	print('Got up arrow key press')

def onReturnKey(event):
	print('Got return key press')

def onLeftClick(event):
	print('Got left mouse button click:', end=' ')
	showPosEvent(event)

def onRightClick(event):
	print('Got right mouse button click:', end=' ')
	showPosEvent(event)

def onMiddleClick(event):
	print('Got middle mouse button click:', end=' ')
	showPosEvent(event)
	showAllEvent(event)

def onLeftDrag(event):
	print('Got left mouse drag:', end=' ')
	showPosEvent(event)

def onDoubleClick(event):
	print('Got double left mouse click', end=' ')
	showPosEvent(event)
	tkroot.quit()

tkroot = Tk()
labelfont = ('courier', 20, 'bold')
widget = Label(tkroot, text='Binding')
widget.config(bg='red', font=labelfont, height = 5, width = 20)
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Button-1>', onLeftClick)
widget.bind('<Button-2>', onMiddleClick)
widget.bind('<Button-3>', onRightClick)
widget.bind('<Double-1>', onDoubleClick)
widget.bind('<B1-Motion>', onLeftDrag)
widget.bind('<KeyPress>', onKeyPress)
widget.bind('<Up>', onArrowKey)
widget.bind('<Return>', onReturnKey)
widget.focus()

tkroot.title('Click')
tkroot.mainloop()
