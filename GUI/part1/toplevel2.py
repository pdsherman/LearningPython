from Tkinter import *

root = Tk()

trees = [('Larch','light blue'),('Pine','light green'),('Redwood','red')]

for (tr, clr) in trees:
	win = Toplevel(root)
	win.title('Tree')
	win.protocol('WM_DELETE_WINDOW',lambda:None)
	#win.iconbitmap('py-blue-trans-out.ico')
	
	msg = Button(win, text=tr, command=win.destroy)
	msg.pack(expand=YES, fill=BOTH)
	msg.config(padx=10, pady=10, bd=10, relief=RAISED)
	msg.config(bg='black', fg=clr, font=('times', 30, 'bold italic'))

root.title('Example')
Label(root, text='Main Window', width=30).pack()
Button(root, text='Quit All', command=root.quit).pack()
root.mainloop()
