"""
File:   ToolBox.py
Author: pdsherman
Date:   Nov. 2016

Description: Implements frame to select various
vision alorithms to run on image canvas displayed
in GUI
"""
from __future__ import print_function

# 3rd party GUI library
from Tkinter import *

# Class that contains and displays image
from ImageCanvas import ImageCanvas

class ToolBox(Frame):
    """ Frame to contain options and info for images """
    def __init__(self, parent, **options):
        Frame.__init__(self, master=parent, **options) 
        self.image = None
        
        #----------------------------#
        #---- Create GUI objects ----#
        #----------------------------# 
        self.options = Frame(master=self, width=100, height=100, relief=RIDGE)
        self.tools   = Frame(master=self, width=100, height=400, relief=RIDGE)
                
        self.pack(side=RIGHT, fill=BOTH)
        self.options.grid(row=0, column=0)
        self.tools.grid(row=1, column=0)
        self.binaryOps()
 
    def binaryOps(self): 
        parent = self.tools
        # Get individual pixel value from specified coordinate 
        Label(parent, text="-"*46).grid(columnspan=2, sticky=E) 
        self.entX = Entry(parent, width=10)
        self.entY = Entry(parent, width=10)
        Label(parent, text='  X: ').grid(row=1, column=0, sticky=E)
        Label(parent, text='  Y: ').grid(row=2, column=0, sticky=E)
        self.entX.grid(row=1, column=1)
        self.entY.grid(row=2, column=1)

        self.btnPixel = Button(parent, text='Pixel Value', 
                command=self.calculatePixelValue, width=8, height=1)
        self.result = Label(parent, text='  Pixel Value:')
        self.btnPixel.grid(column=1, sticky=E)        
        self.result.grid(column=0, sticky=W, columnspan=2) 

        # Invert image
        Label(parent, text="-"*46).grid(columnspan=2, sticky=E)  
        self.btnInvert = Button(parent, text='Invert',
                command=self.invertImage, width=8, height=1)
        self.btnInvert.grid(columnspan=2, sticky=E)

        # Set create image with binary value pixels
        Label(parent, text="-"*46).grid(columnspan=2, sticky=E)
        Label(parent, text="Threshold [0-255]: ").grid(row=8, column=0, columnspan=2)
        self.entThreshold = Entry(parent, width=8)
        self.entThreshold.grid(row=9, column=0, sticky=E)
        self.btnThreshold = Button(parent, text='Threshold', width=8, height=1,
            command=self.binaryImage).grid(row=9,column=1, sticky=E)

        # Contrast streching for greyscale image
        Label(parent, text="-"*46).grid(columnspan=2, sticky=E)
        Label(parent, text="Constrast stretching:").grid(row=11, column=0, 
                columnspan=2, sticky=W)
        Label(parent, text="P0 = gamma*P0 + beta").grid(row=12, column=0,
                columnspan=2)
        self.entGamma = Entry(parent, width=10)
        self.entBeta  = Entry(parent, width=10)
        Label(parent, text='Gamma: ', width=10).grid(row=13, column=0, sticky=E)
        Label(parent, text='Beta: ', width=10).grid(row=14, column=0, sticky=E)
        self.entGamma.grid(row=13, column=1)
        self.entBeta.grid(row=14, column=1)
        self.btnContrast = Button(parent, text='Contrast', width=8, height=1,
                command=self.contrastImage).grid(row=15, column=1, sticky=E)

        # Dark area shrinking/expanding, edge detection
        Label(parent, text="-"*46).grid(columnspan=2, sticky=E)
        self.btnShrink = Button(parent, text="Shrink Dark\nSpots", width=8, height=2,
                command=self.shrinkDarkAreas).grid(row=17, column=1)
        self.btnExpand = Button(parent, text="Expand Dark\nSpots", width=8, height=2,
                command=self.expandDarkAreas).grid(row=17, column=0)
        self.btnEdge = Button(parent, text="Detect Edge", width=8, height=2,
                command=self.edgeDetect).grid(row=18, column=0)
        self.btnNoise = Button(parent, text="Reduce\nNoise", width=8, height=2,
                command=self.reduceNoise).grid(row=18, column=1)
       
        
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
        """ Run invert image operation on image """
        if self.image == None:
            return

        self.image.invertImage()
 
    def binaryImage(self):
        """ Run binary image operation on image """
        if self.image == None:
            return

        #Handle case where value is out of range or not an integer
        try:  
            value = max(0, min(255, int(self.entThreshold.get())))
        except ValueError:
            value = 127
            
        self.entThreshold.delete(0, END)
        self.entThreshold.insert(0, str(value))
        self.image.binaryImage(value)            

    def contrastImage(self):
        """ Run contrast stretching operation on image """
        if self.image == None:
            return
        
        # Handle case where value is out of range or not number
        try:
            gamma = max(1.0, min(255.0, float(self.entGamma.get())))
            beta  = max(-255.0, min(255.0, float(self.entBeta.get())))
        except ValueError:
            gamma = 1.0
            beta  = 0.0
    
        self.entBeta.delete(0, END)
        self.entGamma.delete(0, END)
        self.entBeta.insert(0, str(beta))
        self.entGamma.insert(0, str(gamma))

        self.image.contrastImage(gamma, beta)

    def shrinkDarkAreas(self):
        """ Run dark area shrinking operation on image """
        if self.image == None:
            return 
        self.image.shrinkDarkAreas()

    def expandDarkAreas(self):
        """ Run dark area expand operation on image """
        if self.image == None:
            return
        self.image.expandDarkAreas()

    def edgeDetect(self):
        """ Run edge detection operation on image """
        if self.image == None:
            return
        self.image.edgeDetection()

    def reduceNoise(self):
        """ Run noise reduction operation on image """
        if self.image == None:
            return
        self.image.reduceSaltnPeppaNoise() 
