from Tkinter import *

widget = Button(None, text="btn", command=sys.exit)
widget.pack(expand=YES, fill=X) #can also do fill=BOTH
widget.mainloop()
