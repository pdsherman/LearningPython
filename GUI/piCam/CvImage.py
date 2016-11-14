"""
File:   CvImage.py
Author: pdsherman
Date:   Oct. 2016

Description: Python class to hold and manipulate an image
from a file for use with computer vision playground.
"""
from __future__ import print_function

from os import path
from PIL import Image
from PIL.ImageTk import PhotoImage

class CvImage():
    """ 
    Object to hold and manipulate images from a file 
    for use with computer vision algorithms
    """
    def __init__(self, imgFilename=None, width=350, height=300, **options):
        self.imgFilename = imgFilename
        self.thumbWidth = width
        self.thumbHeight = height
       
        self.updateImages() 

    def updateImages(self):
        """Updates image object and thumbnail object"""
        self.imgObj   = Image.open(self.imgFilename)
        self.imgThumb = self.imgObj.copy()
        self.imgThumb.thumbnail((self.thumbWidth, self.thumbHeight), 
                Image.ANTIALIAS)

    def testFunction(self):
        self.convertImage(None)

    def getImageThumb(self, width = None, height = None):
        """Return resized PhotoImage of image"""
        if(width != None and height != None):
            self.width = width
            self.height = height
            self.updateImages()
        
        return self.imgThumb
       
    def getSize(self):
        """Return the width"""
        return self.imgObj.size()

    def getThumbSize(self):
        """Return size of the thumbnail size """
        return (self.thumbWidth, self.thumbHeight)

    def newImage(self, filename):
        """ Set the filenaame of the image to display
        in the main window. Throw an exception if
        invalid file is given. """
        if(path.isfile(filename)):
            self.imgFilename = filename
            self.updateImages()
        else:
            self.imgFilename = None
            #TODO throw exception

    def getImageFilename(self):
        return self.imgFilename


    def getPixelValue(self, x, y):
        return self.grey.getpixel((x,y))  
    
    def convertImage(self, imgType):
        try:
            self.grey = self.imgObj.convert("L")
            self.grey.save("./images/testPic.tiff")
            self.imgFilename = "./images/testPic.tiff" 
            self.updateImages()
        except IOError:
            print("Cannot convert")
