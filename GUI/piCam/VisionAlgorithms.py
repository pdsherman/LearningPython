"""
File:   VisionAlgorithms.py
Author: pdsherman
Date:   Nov. 2016

Description: Implements computer vision alogrithm
functions. 
"""

from __future__ import print_function
import numpy as np

def stringToArray(data, shape):
    """ Convert string data buffer into a numpy array """
    (cols, rows) = shape
    pixels = np.zeros((rows, cols), dtype=int) 
    for y in range(rows):
        for x in range(cols):
            pixels[y,x] = ord(data[x+y*cols])

    return pixels

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
    """ Modify value of each element of numpy array
        using a user defined input function """
    (rows, cols) = pixels.shape
    for y in range(rows):
        for x in range(cols):
            pixels[y,x] = func(pixels[y,x])
    return pixels  

def stringToList(data):
    """ Convert a data string buffer into a list of each pixel value """ 
    return [ord(ch) for ch in data]

def listToString(pixels):
    """ Convert a list of pixel values into a single data string buffer """
    return "".join([chr(pxl) for pxl in pixels])

def invert(data, mode):
    """ Invert all pixel values """
    if mode != "L": #TODO: Invert for other modes??
        return data

    return listToString([255-x for x in stringToList(data)])

def binary(data, threshold, mode):
    """ Convert all pixels to binary values based on
        comparison to a desired threshold """
    if mode != "L":
        return data

    return listToString([255 if x > threshold else 0 for x in stringToList(data)])

def contrast(data, gamma, beta, mode):
    """ Stretch contrast of an image """
    if mode != "L":
        return data
    
    pixels = [min(255, max(0, int(x*gamma+beta))) for x in stringToList(data)]
    return listToString(pixels) 

def shrinkObjects(data, shape, threshold, mode):
    """ Shrink dark objects in binary pixel value image """
    if mode != "L":
        return data
   
    (cols, rows) = shape
    pxls = [255 if x > threshold else 0 for x in stringToList(data)]
    pxlsCopy  = list(pxls) #Need a copy of the original list (not pointer/reference)
    
    #For each pixel in list, need to check surrounding pixels. Ignore edge pixels.
    for i in range(len(pxls)):
        leftRight = (i % cols) == 0 or ((i+1) % cols) == 0
        topBottom = i < cols or i > (cols*rows)-1-cols
        
        if leftRight or topBottom:
            pxls[i] = pxlsCopy[i]
        else:
            sigma = (pxlsCopy[i-cols-1]+pxlsCopy[i-cols]+pxlsCopy[i-cols+1]+
                     pxlsCopy[i-1]                      +pxlsCopy[i+1]+
                     pxlsCopy[i+cols-1]+pxlsCopy[i+cols]+pxlsCopy[i+cols+1])/255

            if pxlsCopy[i] == 255 or sigma > 0:
                pxls[i] = 255
            else:
                pxls[i] = 0

    return listToString(pxls)









     
