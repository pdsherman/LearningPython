"""
File:   CvImage.py
Author: pdsherman
Date:   Oct. 2016

Description: Python class to hold and manipulate an image
from a file for use with computer vision playground.
"""
from __future__ import print_function

from PIL import Image
from PIL.ImageTk

class CvImage():
    """ 
    Object to hold and manipulate images from a file 
    for use with computer vision algorithms
    """
    def __init__(self, imgFilename=None, **options):
        self.imgFilename = imgFilename


    def setImageFilename(self, filename):
        """ Set the filenaame of the image to display
        in the main window. Throw an exception if
        invalid file is given. """
        if(path.isFile(filename)):
            self.imgFilename = filename
        else:
            self.imgFilename = None
            #TODO throw exception

    def getImageFilename(self):
        return self.imgFilename

    
