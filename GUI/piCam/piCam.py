"""
File:   piCam.py
Author: pdsherman
Date:   May 2016

Description: Program is meant to be run on raspberry pi with 
camera connected. Goal is to create GUI that can user can
dynamically interact with camera as well as platform to 
learn computer vision techniques.
"""
from __future__ import print_function

from Tkinter import *
from tkMessageBox import askokcancel
from tkFileDialog import askopenfilename
from PIL import Image
from PIL.ImageTk import PhotoImage
from os import sys, path

import picamera
import picamera.array
import numpy

class ButtonBar(Frame):
	"""
	Frame at bottom of main window that contains
	row of buttons.  
	"""
	def __init__(self, parent=None, buttons=None, **options):
		Frame.__init__(self, parent, **options)
      
		#List of all buttons in bar 
		self.btns = []

		#Loop through "buttons" to create all buttons in bar 
		for (name, func) in buttons:
			btn = Button(self, text=name, command=func, width=10, height=2)	
			btn.pack(side=RIGHT)
			self.btns.append(btn) 
	
		#Config and pack frame for button bar	
		self.config(bd=3, relief=RIDGE)
		self.pack(side=BOTTOM, fill=X)
  
class ImageCanvas(Canvas):
	"""
	Canvas object to hold and display images in GUI
	"""
	def __init__(self, parent=None, width=350, height=300, imgFile=None, **options):
		Canvas.__init__(self, parent, **options)
       
		#Store the width and height for resizing displayed images
		self.width = width
		self.height = height
 
		#Setup for Canvas on GUI window
		self.config(width=width, height=height, bd=3, relief=RIDGE)
		self.pack(fill=BOTH, expand=True, side=TOP)
       
		#Image file name stored on canvas.
		self.createImg(imgFile)

	def createImg(self, filename=None):
		"""
		Uses filename of an image and creates a resized
		version of the image. Resized image is then displayed
		in the GUI. If no filename argument is given, the
		current image filename saved to instance is used.
		"""
		if(filename != None):
			self.setImageFile(filename)
        
		if(self.imgFile != None):
			try:	
				self.imgObj = Image.open(self.imgFile)
				self.displayImg()		
			
			except:
				#File wasn't valid image
				self.imgFile = None

	def displayImg(self):
		""" Display resized PhotoImage in canvas object """
		self.imgObj.thumbnail((self.width, self.height), Image.ANTIALIAS)	
		self.photo = PhotoImage(self.imgObj)
		self.create_image(self.width/2, self.height/2, image=self.photo, anchor=CENTER)
	
	def setImageFile(self, filename):
		"""
		Sets the filename of the image to display
		in the main window. If invalid file is given
		None is used.
		"""	
		if(path.isfile(filename)):
			self.imgFile = filename
		else:
			self.imgFile = None

class CamGUI():
	"""
	Object to create and display the GUI for the PiCam
	program. Window contains button bar for user options
	and image canvas to display images
	"""
	def __init__(self, camera, **options):
		#Root of GUI	
		self.root = Tk()
		self.root.title("Computer Vision Playground")
	
		#List of texts and functions tuples for button bar
		self.buttons = []
		self.buttons.append(("Quit", self.quit)) 
		self.buttons.append(("Open Image", self.fileCmd))
		self.buttons.append(("Take Picture", self.takePicture))

		#Populate GUI with button bar and canvas image
		self.btnBar = ButtonBar(self.root, self.buttons)
		self.cnvImg = ImageCanvas(self.root, imgFile="./atlas.png")
	
		#PI camera and saved image objects
		self.camera = camera
		self.imgFile = "./temp.jpeg"
		self.rgbArray = None

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
	
	def takePicture(self):
		""" Use the PiCam to take a picture, save it
		and display in GUI """
		try:
			self.camera.capture(self.imgFile, 'jpeg')
			self.cnvImg.createImg(self.imgFile)
		
			self.rgbArray =  picamera.array.PiRGBArray(self.camera)
			self.camera.capture(self.rgbArray, 'rgb')
		except:
			print("Take picture error")

	def getRGBarray():
		""" Returns numpy rgb array of last image
		captured by camera """
		return self.rgbArray

if __name__ == "__main__":
	cam = picamera.camera.PiCamera()
	gui = CamGUI(cam)
	gui.mainloop()

	cam.close()
