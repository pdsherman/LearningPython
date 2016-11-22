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
            command=self.binaryImage).grid(row=9,column=1, sticky=E)
 
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
        """ Run invert image process on image """
        if self.image == None:
            return
        self.image.invertImage()
 
    def binaryImage(self):
        """ Run binary image proess on image """
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

