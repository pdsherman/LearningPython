from Tkinter import *
from tkFileDialog import askopenfilename
from tkColorChooser import askcolor
from tkMessageBox import askquestion, showerror
from tkSimpleDialog import askfloat

demos = {
	'Open': askopenfilename,
	'Color': askcolor,
	'Query': lambda: askquestion('Warning', 'You typed "rm*"\nConfirm?'),
	'Error': lambda: showerror('Error!', "he's dead, Jim"),	
	'Input': lambda: askfloat('Entry', 'Enter credit card number')
}
