"""
From book "Programming Python" Example 8-45
Requires PIL for JPEGs and thumbnail creation
"""
from __future__ import print_function
import os, sys, math
from Tkinter import *
from PIL import Image #thumbnail creation
from PIL.ImageTk import PhotoImage #JPEG capability

def makeThumbs(imgdir, size=(100, 100), subdir="thumbs"):
	"""
	Get thumbnail images to all images in a directory. For each image, create
	and save a new thumb, or load and return an existing. Makes thumb
	directory if needed. Caller can also run listdir on thumb dir to load. 
	On bad file types, IOError could be rasied. 

	returns a list of (image filename, thumb image object).
	"""
	
	#Check if image directory exists	
	if not os.path.exists(imgdir):
		print("Error: Directory "+imgdir+" doesn't exist")
		sys.exit(0)
	
	#Thumb directory. Create new directory if needed
	thumbdir = os.path.join(imgdir, subdir)
	if not os.path.exists(thumbdir):
		print("Creating new directory for thumbnails")	
		os.mkdir(thumbdir)
	
	thumbs = []
	for imgfile in os.listdir(imgdir):
		thumbpath = os.path.join(thumbdir, imgfile)
		if os.path.exists(thumbpath):
			thumbobj = Image.open(thumbpath)
			thumbs.append((imgfile, thumbobj))
		else:
			print("making",thumbpath)
			imgpath = os.path.join(imgdir, imgfile)

			try:
				imgobj = Image.open(imgpath)
				imgobj.thumbnail(size, Image.ANTIALIAS)
				imgobj.save(thumbpath)

				thumbs.append((imgfile, imgobj))
			except:
				print("Skipping: ", imgpath)

	return thumbs

class ViewOne(Toplevel):
	"""
	Open a single image in a pop-up window when
	created. Photoimage must be saved. Images are
	erased if object is reclaimed
	"""
	def __init__(self, imgdir, imgfile):
		Toplevel.__init__(self)
		self.title(imgfile)
		imgpath = os.path.join(imgdir, imgfile)
		imgobj = PhotoImage(file=imgpath)
		Label(self, image = imgobj).pack()
		print(imgpath, imgobj.width(), imgobj.height())
		self.savephoto = imgobj #Keep reference on me

def viewer(imgdir, kind = Toplevel, cols = None):
	"""
	Make thumb links window for an image directory. One thumb button
	per image. Use kind = Tk to show in main app window, or Frame
	container (pack). Imgfile differs per loop, must save with a default.
	PhotoImage objs must be saved as objs is erased if reclaimed. 
	Packed row frames (versus grid, fixed-sizes, canvas)
	"""
	win = kind()
	win.title("Viewer: " + imgdir)
	quit = Button(win, text="Quit", command=win.quit, bg='beige')
	quit.pack()
	thumbs = makeThumbs(imgdir)

	if not cols:
		cols = int(math.ceil(math.sqrt(len(thumbs))))
	
	print(cols)
	
	savephotos = []
	while thumbs:
		thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
		row = Frame(win)
		row.pack(fill = BOTH)
		for (imgfile, imgobj) in thumbsrow:
			photo = PhotoImage(imgobj)
			link  = Button(row, image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
			link.config(command=handler)
			link.pack(side=LEFT, expand=YES)
			savephotos.append(photo)
	
	return win, savephotos
	
if __name__ == "__main__":
	imgdir = (len(sys.argv) > 1 and sys.argv[1]) or "images"
	main, save = viewer(imgdir, kind=Tk)
	#main = viewer(imgdir, kind=Tk)	
	main.mainloop()

	
