"""
File:   VisionGui.py
Author: pdsherman
Date:   Oct. 2016

Description: Program is meant to be run on raspberry pi with 
camera connected. Goal is to create GUI that can user can
dynamically interact with camera as well as platform to 
learn computer vision techniques. This file defines the
MainGui which puts together all the frames imported by Frames.py
"""
from __future__ import print_function

from os import sys, path

# 3rd Party GUI Library
from Tkinter import *
from tkMessageBox import askokcancel
from tkFileDialog import askopenfilename

# Frames to make GUI program
from ButtonBar   import ButtonBar
from ImageCanvas import ImageCanvas
from ToolBox     import ToolBox

try:
    import picamera
    import picamera.array
    PICAM_ENABLED = True
except ImportError:
    print("PiCamera modules not imported")
    PICAM_ENABLED = False

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
        self.buttons.append(("Quit",          self.quit)) 
        self.buttons.append(("Convert to\nGreyscale", self.convertImageToGrey))
        self.buttons.append(("Reset Image", self.resetImage))  
        self.buttons.append(("Take Picture",  self.takePicture))
        self.buttons.append(("Open Image\nFrom File",    self.fileCmd))

        #Populate GUI with button bar and canvas images
        self.toolbox = ToolBox(self.root ,width = 300, bd=3, relief=RIDGE)
        self.btnBar = ButtonBar(self.root, self.buttons)
        self.cnvImgOrig = ImageCanvas(self.root, width=500, height=500, imgFilename=imgFile)
        self.cnvImgNew  = ImageCanvas(self.root, width=500, height=500, imgFilename=imgFile)

        #Give toolbox reference to new image canves
        self.toolbox.setImage(self.cnvImgNew)

        #PI camera and saved image objects
        if not camera == None:
            self.camera = camera

    def mainloop(self):
        """ Run program """
        self.root.mainloop()

    def fileCmd(self):
        """ Get flename to of image to open on ImageCanvas """
        filename = askopenfilename()   
        self.cnvImgOrig.displayImage(filename)
        self.cnvImgNew.displayImage(filename)

    def quit(self):
        """ Brings up dialog box to ask user if they
        want to quit program """
        if askokcancel("Verify Exit", "Really quit?"):
            sys.exit(0)
	
    def takePicture(self):
        """ Use the PiCam to take a picture, save it
        and display in GUI """
        if not PICAM_ENABLED:
            return

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

    def convertImageToGrey(self):
        self.cnvImgNew.convertToGreyscale()

    def resetImage(self):
        filename = self.cnvImgOrig.getImageFilename()
        self.cnvImgNew.displayImage(filename)
