"""
File:   piCam.py
Author: pdsherman
Date:   11 May 2016

Description: Program is meant to be run on raspberry pi with 
camera connected. Goal is to create GUI that can user can
dynamically interact with camera as well as platform to 
learn computer vision techniques.
"""
from Tkinter import *
from quitter import Quitter

#Create frame
root = Tk()
root.title('Computer Vision Playground')



Quitter(root).pack(fill = X)


#---------------#
#  Main Loop 
#---------------#
root.mainloop()
