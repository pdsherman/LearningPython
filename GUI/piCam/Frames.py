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
from tkMessageBox import askokcancel
from tkFileDialog import askopenfilename
from PIL import Image
from PIL.ImageTk import PhotoImage

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
            btn = Button(self, text=name, command=func, width=8, height=2)	
            btn.pack(side=RIGHT)
            self.btns.append(btn) 

        #Config and pack frame for button bar	
        self.config(bd=3, relief=RIDGE)
        self.pack(side=BOTTOM, fill=X)

class ToolBox(Frame):
    """ Frame to contain options and info for images """
    def __init__(self, parent, funcPixel=None, **options):
        Frame.__init__(self, parent, **options)
        
        self.pack(side=RIGHT, fill=BOTH)
        
        self.entX = Entry(self)
        self.entY = Entry(self)
        
        Label(self, text='Grid Positions').grid(columnspan=2)
        Label(self, text="-"*46).grid(columnspan=2, sticky=E) 
        Label(self, text='  X: ').grid()
        Label(self, text='  Y: ').grid()

        self.entX.grid(row=2, column=1)
        self.entY.grid(row=3, column=1)
        self.btn = Button(self, text='Pixel Value', command=self.calculatePixelValue,
                            width=7, height=1)

        self.btn.grid(row=4,column=1,sticky=E)        
        Label(self, text="-"*46).grid(columnspan=2, sticky=E)  
        self.result = Label(self, text='  Pixel Value: ??')
        self.result.grid(row=6,column=0, sticky=W, columnspan=2)

        if(funcPixel):
            self.funcPixel = funcPixel

     
    def calculatePixelValue(self):
        """ Get greyscale value for a specific pixel in image """ 
        x = int(self.entX.get())
        y = int(self.entY.get())        
        value = self.funcPixel(x, y) 
        self.result.config(text="  Pixel Value: "+str(value))
  
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
        self.updateImage()
        self.displayImage() 
       
    def updateImage(self):
        """ Updates image and thumbnail objects """
        self.imgObj   = Image.open(self.imgFilename)
        self.imgThumb = self.imgObj.copy()
        self.imgThumb.thumbnail((self.thumbWidth, self.thumbHeight),
                Image.ANTIALIAS)

    def displayImage(self):
        """
        Uses filename of an image and creates a resized
        version of the image. Resized image is then displayed
        in the GUI. If no filename argument is given, the
        current image filename saved to instance is used.
        """ 
        if self.imgFilename == None:
            return

        try:
            size = self.imgThumb.size;
            center=[size[0]/2, size[1]/2] 
            self.photo = PhotoImage(self.imgThumb)
            self.create_image((center[0], center[1]), image=self.photo, anchor=CENTER)	
        except:
            #File wasn't valid image
            print("Invalid Image")
            self.imgFilename = None

    def setNewImageFile(self, filename):
        self.image.newImage(filename)

    def convertToGreyscale(self):
        try:
            self.imgFilename = "./images/testPic.tiff"
            grey = self.imgObj.convert("L")
            grey.save(self.imgFilename)
            self.updateImage()
            self.displayImage()
        except IOError:
            print("Cannot convert")
            
    def getPixelValue(self, x, y):
        """ Return pixel value from desired pixel coordinate """
        #TODO: make sure x, y are in valid range
        return self.imgObj.getpixel((x, y))

    def createArray(self):
        data_str = self.imgObj.tostring()
        array = []
        for i in range(len(data_str)):
            array.append(255 - ord(data_str[i]))

        new_str = self.arrayToString(array)
        new_obj = Image.fromstring("L", (379, 565), new_str)
        new_obj.save(self.imgFilename)

        self.updateImage()
        self.displayImage()
        return array

    def arrayToString(self, array):
        data_str = ""
        for i in range(len(array)):
            data_str += chr(array[i])
        return data_str
