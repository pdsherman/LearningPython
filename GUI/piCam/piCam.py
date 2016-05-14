"""
File:   piCam.py
Author: pdsherman
Date:   May 2016

Description: Program is meant to be run on raspberry pi with 
camera connected. Goal is to create GUI that can user can
dynamically interact with camera as well as platform to 
learn computer vision techniques.
"""
from Tkinter import *
from tkMessageBox import askokcancel
from tkFileDialog import askopenfilename
from PIL import Image
from PIL.ImageTk import PhotoImage
from os import sys, path

class ButtonBar(Frame):
    """
    Created a bar of buttons at the bottom of
    the main window. Buttons include following:
    Quit:       End the program
    Open File:  User picks file to open and display in window. 
    """
    def __init__(self, parent=None, cnvImg=None, **options):
        Frame.__init__(self, parent, **options)
       
        self.cnvImg = cnvImg

        btnQuit = Button(self, text="Quit", command=self.quit)
        btnFile = Button(self, text="Open File", command=self.getFile)
        
        self.btns = []
        self.btns.append(btnQuit) 
        self.btns.append(btnFile) 

        for btn in self.btns:
            btn.config(width=10, height=2)
            btn.pack(side=RIGHT)
      
        self.config(bd=3, relief=RIDGE)
        self.pack(side=BOTTOM, fill=X)

    def quit(self):
        """
        Brings up dialog box to ask user if they
        want to quit program
        """
        if askokcancel("Verify Exit", "Really quit?"):
            sys.exit(0)

    def getFile(self):
        """
        Open dialog box for user to select image from
        file system to display
        """
        if(self.cnvImg != None):
            cnvImg.createImg(askopenfilename())
    
    def setCanvasImage(self, cnvImg):
        """
        Set object canvas 
        """
        self.cnvImg = cnvImg

class CanvasImage(Canvas):
    """
    Canvas object to hold and display object
    """
    def __init__(self, parent=None, width=350, height=300, imgFile=None, **options):
        Canvas.__init__(self, parent, **options)
        
        #Setup for Canvas on GUI window
        self.config(width=width, height=height, bd=3, relief=RIDGE)
        self.pack(fill=BOTH, expand=True, side=TOP)
       
        #Image file name stored on canvas.
        self.createImg(imgFile)

    def createImg(self, filename=None):
        if(filename != None):
            self.setImageFile(filename)
        
        if(self.imgFile != None):
            self.img = PhotoImage(file=self.imgFile)
            self.config(width=self.img.width(), height=self.img.height())
            self.create_image(2, 2, image=self.img, anchor=NW)

    def setImageFile(self, filename):
        #Check if valid file 
        #TODO: check if valid image file
        if(filename != None and path.isfile(filename)):
            self.imgFile = filename
        else:
            self.imgFile = None

#Create frame
root = Tk()
root.title('Computer Vision Playground')

btnBar = ButtonBar(root)
cnvImg = CanvasImage(root, imgFile="./atlas.png")
btnBar.setCanvasImage(cnvImg)

#---------------#
#   Main Loop   #
#---------------#
root.mainloop()
