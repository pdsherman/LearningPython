"""
File:   Frames.py
Author: pdsherman
Date:   Nov. 2016

Description: Defines all indiviudal parts for
the VisionGui program. Currently consisting of
ButtonBar
ImagesCanvas
TookBox
"""
from __future__ import print_function

from os import sys, path
from Tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

import VisionAlgorithms as va

class ButtonBar(Frame):
    """
    Frame at bottom of main window that contains
    row of buttons for basic commands to display
    images.
    """
    def __init__(self, parent=None, buttons=None, **options):
        Frame.__init__(self, parent, **options)
    
        #List of all buttons in bar 
        self.btns = []

        #Loop through "buttons" to create all buttons in bar 
        for (name, func) in buttons:
            btn = Button(self, text=name, command=func, width=8, height=2)	
            btn.pack(side=RIGHT)
            self.btns.append(btn) 

        #Config and pack frame for button bar	
        self.config(bd=3, relief=RIDGE)
        self.pack(side=BOTTOM, fill=X)

class ToolBox(Frame):
    """ Frame to contain options and info for images """
    def __init__(self, parent, **options):
        Frame.__init__(self, parent, **options)
        
        self.pack(side=RIGHT, fill=BOTH)
       
        # Get individual pixel value from specified coordinate 
        Label(self, text="-"*46).grid(columnspan=2, sticky=E) 
        self.entX = Entry(self, width=10)
        self.entY = Entry(self, width=10)
        Label(self, text='  X: ').grid(row=1, column=0, sticky=E)
        Label(self, text='  Y: ').grid(row=2, column=0, sticky=E)
        self.entX.grid(row=1, column=1)
        self.entY.grid(row=2, column=1)

        self.btnPixel = Button(self, text='Pixel Value', 
                command=self.calculatePixelValue, width=8, height=1)
        self.result = Label(self, text='  Pixel Value:')
        self.btnPixel.grid(column=1, sticky=E)        
        self.result.grid(column=0, sticky=W, columnspan=2) 

        # Invert image
        Label(self, text="-"*46).grid(columnspan=2, sticky=E)  
        self.btnInvert = Button(self, text='Invert',
                command=self.invertImage, width=8, height=1)
        self.btnInvert.grid(columnspan=2, sticky=E)

        # Set tolerance for setting binary values
        Label(self, text="-"*46).grid(columnspan=2, sticky=E)
        Label(self, text="Threshold [0-255]: ").grid(row=8, column=0, columnspan=2)
        self.entThreshold = Entry(self, width=8)
        self.entThreshold.grid(row=9, column=0, sticky=E)
        self.btnThreshold = Button(self, text='Threshold', width=8, height=1,
            command=self.thresholdImage).grid(row=9,column=1, sticky=E)
 
        self.image = None

    def setImage(self, image):
        """ Sets object member variable image """
        self.image = image

    def calculatePixelValue(self):
        """ Get greyscale value for a specific pixel in image """
        if self.image == None:
            return
       
        #Handle case where invalid, non-integer entries are made 
        try:
            x = int(self.entX.get())
            y = int(self.entY.get()) 
        except ValueError:
            x = 0
            y = 0 
            self.entX.delete(0, END)
            self.entY.delete(0, END)
            self.entX.insert(0, "0")
            self.entY.insert(0, "0")
  
        value = self.image.getPixelValue(x, y) 
        self.result.config(text="  Pixel Value: {}".format(value))

    def invertImage(self):
        if self.image == None:
            return
        self.image.invertImage()
 
    def thresholdImage(self):
        if self.image == None:
            return

        #Handle case where value is out of range or not an integer
        try:  
            value = max(0, min(255, int(self.entThreshold.get())))
        except ValueError:
            value = 127
            
        self.entThreshold.delete(0, END)
        self.entThreshold.insert(0, str(value))
        self.image.thresholdImage(value)            
        
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

    def getImageFilename(self):
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
        new_data = va.invertImage(self.imgObj.tostring(), self.imgObj.size,
                    self.imgObj.mode) 

        new_obj = Image.fromstring(self.imgObj.mode, self.imgObj.size, new_data)
        new_obj.save(self.imgFilename)
        self.displayImage()

    def thresholdImage(self, threshold):
        """ Return images with threshold """
        new_data = va.thresholdImage(self.imgObj.tostring(), self.imgObj.size,
                    threshold, self.imgObj.mode)

        new_obj = Image.fromstring(self.imgObj.mode, self.imgObj.size, new_data)
        new_obj.save(self.imgFilename)
        self.displayImage() 
        







