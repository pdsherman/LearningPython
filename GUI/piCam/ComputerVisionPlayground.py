"""
File:   ComputerVisionPlayground.py
Author: pdsherman
Date:   Oct. 2016

Description: Runs the main loop for GUI based program
created as platform to test out computer vision algorithms.
User should be able to dynamically interact with camera 
or images in a simple way. 

Originally intended for use with Raspberry Pi and PiCam hardware. 
"""
from __future__ import print_function

import VisionGui

#---------------------------#
#---- Main Program Loop ----#
#---------------------------#
# cam = picamer.camera.PiCamera()
cam = None
gui = VisionGui.MainGui(cam)
gui.mainloop()

if not cam == None:
    cam.close()
