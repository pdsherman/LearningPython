"""
File:   ImageCanvas.py
Author: pdsherman
Date:   Nov. 2016

Description: Defines a GUI canvas object that can
display, modify and save images. Used as testing
platform for vision algorithms.
"""
from __future__ import print_function

# 3rd party GUI and image libraries
from Tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

# Set of functions implementing various vision algorithms
import VisionAlgorithms as va
       
class ImageCanvas(Canvas):
    """Canvas object to hold and display image from file
       in GUI and used to show computer vision alorithms """
    def __init__(self, parent=None, width=350, height=300, 
            imgFilename=None, **options):
        Canvas.__init__(self, parent, **options)
         
        #Setup for Canvas on GUI window
        self.config(width=width, height=height, bd=3, relief=RIDGE)
        self.pack(fill=BOTH, expand=True, side=LEFT)
 
        #Store the width and height for resizing displayed images
        self.thumbWidth = width
        self.thumbHeight = height
       
        #Original image to display on canvas.
        self.imgFilename = imgFilename 
        self.displayImage() 
       
    def updateImage(self, filename = None):
        """ Updates image and thumbnail objects """
        if filename != None:
            self.imgFilename = filename
        
        self.imgObj   = Image.open(self.imgFilename)
        self.imgThumb = self.imgObj.copy()
        self.imgThumb.thumbnail((self.thumbWidth, self.thumbHeight),
                Image.ANTIALIAS)

    def displayImage(self, filename = None):
        """
        Uses filename of an image and creates a resized
        version of the image. Resized image is then displayed
        in the GUI. If no filename argument is given, the
        current image filename saved to instance is used.
        """ 
        if self.imgFilename == None:
            return

        try:
            self.updateImage(filename)
            center=[self.thumbWidth/2, self.thumbHeight/2] 
            self.photo = PhotoImage(self.imgThumb)
            self.create_image((center[0], center[1]), 
                    image=self.photo, anchor=CENTER)	
        except:
            #File wasn't valid image
            print("Invalid Image")
            self.imgFilename = None

    def displayFromString(self, data):
        """ Update displayed image using new pixel data buffer """
        obj = Image.fromstring(self.imgObj.mode, self.imgObj.size, data)
        obj.save(self.imgFilename)
        self.displayImage()

    def getImageFilename(self):
        """ Get filename for current image being displayed """
        return self.imgFilename

    def convertToGreyscale(self):
        """ Convert image to greyscale with all pixels 
        of value in range [0, 255] """
        try:
            self.imgFilename = "./images/testPic.tiff"
            grey = self.imgObj.convert("L")
            grey.save(self.imgFilename)
            self.displayImage()
        except IOError:
            print("Cannot convert")
            
    def getPixelValue(self, x, y):
        """ Return pixel value from desired pixel coordinate """
        #TODO: make sure x, y are in valid range
        size = self.imgObj.size
        if(x > size[0] or y > size[1] or x < 0 or y < 0):
            print("Invalid coordinate. Returning zero")
            return 0

        return self.imgObj.getpixel((x, y))

    def invertImage(self):
        """ Invert image and display """
        data_inverted = va.invert(self.imgObj.tostring(), self.imgObj.size,
                    self.imgObj.mode) 

        self.displayFromString(data_inverted)

    def binaryImage(self, threshold):
        """ Convert image to binary pixel values """
        data_binary = va.binary(self.imgObj.tostring(), self.imgObj.size,
                    threshold, self.imgObj.mode)

        self.displayFromString(data_binary) 

    def contrastImage(self, gamma, beta):
        """ """
        data_contrast = va.contrast(self.imgObj.tostring(), self.imgObj.size,
                    gamma, beta, self.imgObj.mode)






