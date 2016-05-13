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
from tkMessageBox import askokcancel
from os import sys

def quit():
	ans = askokcancel("Verify exit", "Really quit?")
	if ans:
		sys.exit(0)

#Create frame
root = Tk()
root.title('Computer Vision Playground')

#Add Quit button
row = Frame(root)
row.config(width=500)
btnQuit = Button(row, text="Quit", command=quit)
btnTest = Button(row, text="Test12")
btnQuit.pack(side=RIGHT)
btnTest.pack(side=RIGHT)
row.pack(side=BOTTOM)

#Add Canvas for showing images
cnvs = Canvas(root)
cnvs.pack(fill=BOTH, side=TOP)
cnvs.config(width=100, height=100)

#---------------#
#  Main Loop 
#---------------#
root.mainloop()
