"""
File:   VisionAlgorithms.py
Author: pdsherman
Date:   Nov. 2016

Description: Implements computer vision alogrithm
functions. 
"""

from __future__ import print_function
import numpy as np

def stringToList(data):
    """ Convert a data string buffer to a list of each byte value """ 
    return [ord(ch) for ch in data]

def stringToArray(data, shape):
    """ Convert string data buffer into a numpy array """
    (cols, rows) = shape
    pixels = np.zeros((rows, cols), dtype=int) 
    for y in range(rows):
        for x in range(cols):
            pixels[y,x] = ord(data[x+y*cols])

    return pixels

def listToString(pixels):
    """ Convert a list of bytes into a single data string buffer """
    data = [chr(ch) for ch in pixels]
    return "".join(data)

def arrayToString(pixels):
    """ Convert numpy array into a string data buffer """
    (rows, cols) = pixels.shape 
    data = [0]*pixels.size
   
    c = 0 
    for y in range(rows):
        for x in range(cols):
            data[c] = chr(pixels[y,x])
            c += 1

    return "".join(data)

def modifyEachPixel(pixels, func):
    """ Modify each pixel value using a user defined
        input function """
    (rows, cols) = pixels.shape
    for y in range(rows):
        for x in range(cols):
            pixels[y,x] = func(pixels[y,x])
    return pixels  

def invert(data, shape, mode="L", flag = True):
    """ Invert all pixel values """
    pixels = stringToList(data)
    
    if mode == "L":
        pixels = [255-x for x in pixels] 
    #TODO: Invert for other modes. For now return pixels
   
    return listToString(pixels)

def binary(data, shape, threshold, mode="L"):
    """ Convert all pixels to binary values based on
        comparison to a desired threshold """
    pixels = stringToList(data)

    if mode == "L":
        pixels = [255 if x > threshold else 0 for x in pixels]
   
    return listToString(pixels)
