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
        self.width = width
        self.height = height
       
        self.imgObj = Image.open(self.imgFilename)
        self.imgObj.thumbnail((self.width, self.height), Image.ANTIALIAS)

    def getImageObject(self):
        """Return resized PhotoImage of image"""
        return self.imgObj
       
    def getWidth(self):
        """Return the width"""
        return self.width

    def getHeight(self):
        """Return height of image"""
        return self.height

    def setImageFilename(self, filename):
        """ Set the filenaame of the image to display
        in the main window. Throw an exception if
        invalid file is given. """
        if(path.isfile(filename)):
            self.imgFilename = filename
        else:
            self.imgFilename = None
            #TODO throw exception

    def getImageFilename(self):
        return self.imgFilename
