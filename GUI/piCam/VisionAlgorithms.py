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
    data = ""
    for i in range(len(pixels)):
        data += chr(pixels[i])
        
    return data

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
    (rows, cols) = pixels.shape
    for y in range(rows):
        for x in range(cols):
            pixels[y,x] = func(pixels[y,x])
    return pixels  

def invertImage(data, shape, mode="L", flag = True):
    """ Takes in list returns an inverted version """
    if flag:
        pixels = stringToList(data)
    else:
        pixels = stringToArray(data, shape)
    
    if mode == "L":
        if flag:
            inverted = [255-x for x in pixels] 
            return listToString(inverted)
        else:
            inverted = modifyEachPixel(pixels, lambda x: 255-x)
            return arrayToString(pixels) 
    #TODO: Invert for other modes. For now return pixels
    return listToString(pixels)
