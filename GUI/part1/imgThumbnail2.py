"""
From book "Programming Python" Example 8-47
Requires PIL for JPEGs and thumbnail creation

Same as previous version of thumbnail viewer,
but now uses grid geometry to achieve more uniform
layout
"""
from __future__ import print_function
import sys, math
from Tkinter import *
from PIL.ImageTk import PhotoImage #JPEG capability
from imgThumbnail import makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, cols=None):
	"""
	custom version that uses gridding
	"""

	win = kind()
	win.title("Viewer: " + imgdir)
	thumbs = makeThumbs(imgdir)

	if not cols:
		cols = int(math.ceil(math.sqrt(len(thumbs))))

	rownum = 0
	savephotos = []
	
	while thumbs:
		thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
		colnum = 0
		for (imgfile, imgobj) in thumbsrow:
			photo = PhotoImage(imgobj)
			link = Button(win, image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
			link.config(command = handler)
			link.grid(row=rownum, column=colnum)
			savephotos.append(photo)
			colnum += 1

		rownum += 1

	Button(win, text="Quit", command=win.quit).grid(columnspan=cols, stick=EW)

	return win, savephotos

if __name__ == "__main__":
	imgdir = (len(sys.argv) > 1 and sys.argv[1]) or "images"
	main, save = viewer(imgdir, kind=Tk)
	main.mainloop()
