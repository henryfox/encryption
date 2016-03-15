import encrypt
from Tkinter import *

class Btn:
	"""this is the class for making buttons"""

	def __init__(self, window, text, gridCol, gridRow, function):
		button  = Button(window, text=text, command=function)
		button.grid(column=gridCol, row=gridRow)

class Inp:
	"""this is the class for making buttons"""

	def __init__(self, window, gridCol, gridRow):
		inp = Entry(window)
		inp.grid(column=gridCol, row=gridRow)

class DropDown:
	"""this is the class for making buttons"""

	def __init__(self, window, options, gridCol, gridRow):
		dropdown = OptionMenu(window, *options)
		dropdown.grid(column=gridCol, row=gridRow)

root = Tk()

Inp(root, 1, 1)

root.mainloop()