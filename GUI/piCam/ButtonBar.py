"""
File:   ButtonBar.py
Author: pdsherman
Date:   Nov. 2016

Description: Defines a class that will create a frame
containing a row of buttons. Buttons and corresponding
callbacks are created from input to constructor
"""
from __future__ import print_function
from Tkinter import *

class ButtonBar(Frame):
    """
    Frame at bottom of main window that contains
    row of buttons for basic commands to display
    images.
    """
    def __init__(self, parent=None, buttons=None, **options):
        Frame.__init__(self, parent, **options)
    
        #List of all buttons in bar 
        self.btns = []

        #Loop through "buttons" to create all buttons in bar 
        for (name, func) in buttons:
            btn = Button(self, text=name, command=func, width=8, height=2)	
            btn.pack(side=RIGHT)
            self.btns.append(btn) 

        #Config and pack frame for button bar	
        self.config(bd=3, relief=RIDGE)
        self.pack(side=BOTTOM, fill=X)

