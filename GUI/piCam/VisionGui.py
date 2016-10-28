"""
File:   VisionGui.py
Author: pdsherman
Date:   Oct. 2016

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
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
from CvImage import CvImage
try:
    import picamera
    import picamera.array
    PICAM_ENABLE = True
except ImportError:
    print("PiCamera modules not imported")
    PICAM_ENABLE = False


def rgb2gray(rgb):
    """Convert array of RGB pixels to grayscale"""
    #TODO: not sure if working
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

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
    """Canvas object to hold and display images in GUI"""
    def __init__(self, parent=None, width=350, height=300, imgFile=None, **options):
        Canvas.__init__(self, parent, **options)
       
        #Store the width and height for resizing displayed images
        self.width = width
        self.height = height
 
        #Setup for Canvas on GUI window
        self.config(width=width, height=height, bd=3, relief=RIDGE)
        self.pack(fill=BOTH, expand=True, side=TOP)
       
        #Original image to display on canvas.
        self.image = CvImage(imgFile, width, height)
        self.createImage() 
        
    def createImage(self):
        """
        Uses filename of an image and creates a resized
        version of the image. Resized image is then displayed
        in the GUI. If no filename argument is given, the
        current image filename saved to instance is used.
        """
        filename = self.image.getImageFilename()
        
        if filename == None:
            return

        try:
            center=[self.image.getWidth()/2, self.image.getHeight()/2] 
            self.photo = PhotoImage(self.image.getImageObject())
            self.create_image(center[0], center[1],
                    image=self.photo, anchor=CENTER)	
        except:
            #File wasn't valid image
            print("Invalid Image")
            self.imgFile = None

    def testFunction(self):
        self.image.testFunction()
	
class MainGui():
    """
    Object to create and display the GUI for the PiCam
    program. Window contains button bar for user options
    and image canvas to display images
    """
    def __init__(self, camera, imgFile, **options):
        #Root of GUI	
        self.root = Tk()
        self.root.title("Computer Vision Playground")
	
        #List of texts and functions tuples for button bar
        self.buttons = []
        self.buttons.append(("Quit", self.quit)) 
        self.buttons.append(("Open Image", self.fileCmd))
        self.buttons.append(("Take Picture", self.takePicture))
        self.buttons.append(("Test Function", self.testFunction))

        #Populate GUI with button bar and canvas image
        self.btnBar = ButtonBar(self.root, self.buttons)
        self.cnvImg = ImageCanvas(self.root, imgFile=imgFile)
	
        #PI camera and saved image objects
        if not camera == None:
            self.camera = camera
        self.imgFile = "./temp.png"
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
            #self.camera.capture(self.imgFile, 'jpeg')
            #self.cnvImg.createImg(self.imgFile)
		
            self.rgbArray =  picamera.array.PiRGBArray(self.camera)
            self.camera.capture(self.rgbArray, 'rgb')
            
            self.gray = rgb2gray(self.rgbArray.array)
            plt.imshow(self.gray, cmap = plt.get_cmap('gray'))
            plt.show()
            print(self.gray.shape, self.gray.ndim)
            print(self.gray[0][2]) 
            self.img = Image.fromarray(self.rgbArray.array)
            self.img.save("./array.png")
            self.cnvImg.displayImg(self.img)
        except:
            print("Take picture error")

    def testFunction(self):
        self.cnvImg.testFunction()

    def getRGBarray():
        """ Returns numpy rgb array of last image
        captured by camera """
        return self.rgbArray
