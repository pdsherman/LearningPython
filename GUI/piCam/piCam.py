"""
File:   piCam.py
Author: pdsherman
Date:   May 2016

Description: Program is meant to be run on raspberry pi with 
camera connected. Goal is to create GUI that can user can
dynamically interact with camera as well as platform to 
learn computer vision techniques.
"""
from Tkinter import *
from tkMessageBox import askokcancel
from tkFileDialog import askopenfilename
from PIL import Image
from PIL.ImageTk import PhotoImage
from os import sys, path

class ButtonBar(Frame):
	"""
	Created a bar of buttons at the bottom of
   the main window.
	"""
	def __init__(self, parent=None, buttons=None, **options):
		Frame.__init__(self, parent, **options)
      
   	#List of all buttons in bar 
		self.btns = []

		#Loop through "buttons" to create all buttons in bar 
		for name, func in buttons.iteritems():
			btn = Button(self, text=name, command=func, width=10, height=2)	
			btn.pack(side=RIGHT)
     		self.btns.append(btn) 
	
		#Config and pack frame for button bar	
		self.config(bd=3, relief=RIDGE)
		self.pack(side=BOTTOM, fill=X)
  
class ImageCanvas(Canvas):
	"""
	Canvas object to hold and display object
	"""
	def __init__(self, parent=None, width=350, height=300, imgFile=None, **options):
		Canvas.__init__(self, parent, **options)
        
		#Setup for Canvas on GUI window
		self.config(width=width, height=height, bd=3, relief=RIDGE)
		self.pack(fill=BOTH, expand=True, side=TOP)
       
		#Image file name stored on canvas.
		self.createImg(imgFile)

	def createImg(self, filename=None):
		if(filename != None):
			self.setImageFile(filename)
        
		if(self.imgFile != None):
			#try:	
			self.imgObj = Image.open(self.imgFile)
			self.imgObj.thumbnail((350, 300), Image.ANTIALIAS)	
			self.photo = PhotoImage(self.imgObj)
		
			#self.config(width=self.img.width(), height=self.img.height())
			self.create_image(175, 150, image=self.photo, anchor=CENTER)
			#except:
			#File wasn't valid image
			self.imgFile = None

	def setImageFile(self, filename):
		#Check if valid file 
		#TODO: ?check if valid image file?
		if(filename != None and path.isfile(filename)):
			self.imgFile = filename
		else:
			self.imgFile = None

class PiCamGUI():
	"""
	Object to create and display the GUI for the PiCam
	program. Window contains button bar for user options
	and image canvas to display images
	"""
	def __init__(self, parent=None, **options):
		#Root of GUI	
		self.root = Tk()
		self.root.title("Computer Vision Playground")

		#Dictionary of texts and functions for button bar
		self.buttons = {"Quit": self.quit, "Open File": self.fileCmd}

		#Populate GUI with button bar and canvas image
		self.btnBar = ButtonBar(self.root, self.buttons)
		self.cnvImg = ImageCanvas(self.root, imgFile="./atlas.png")
	
	def mainloop(self):
		""" Run program """
		self.root.mainloop()

	def fileCmd(self):
		""" Update image file of ImageCanvas """
		self.cnvImg.createImg(askopenfilename())

	def quit(self):
		""" Brings up dialog box to ask user if they
		want to quit program """
		if askokcancel("Verify Exit", "Really quit?"):
			sys.exit(0)

if __name__ == "__main__":
	gui = PiCamGUI()
	gui.mainloop()
