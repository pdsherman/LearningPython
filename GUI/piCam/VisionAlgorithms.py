"""
File:   VisionAlgorithms.py
Author: pdsherman
Date:   Nov. 2016

Description: Implements computer vision alogrithm
functions. 
"""

from __future__ import print_function
import numpy as np


def stringToList(data_str):
    """ Convert a data string buffer to a list of each byte value """ 
    return [ord(ch) for ch in data_str]

def stringToArray(data, size):
    pixels = np.zeros(size, dtype=int)
    i = 0
    for 

def listToString(data_list):
    """ Covert a list of bytes into a single data string buffer """
    data_str = ""
    for i in range(len(data_list)):
        data_str += chr(data_list[i])
        
    return data_str


def invertImage(data, size, mode="L"):
    """ Takes in list returns an inverted version """
    pixels = stringToList(data)
    stringToArray(data, size)
    if mode == "L":
        inverted = [255-x for x in pixels]
        return listToString(inverted)
    #TODO: Invert for other modes. For now return pixels
    return listToString(pixels)
