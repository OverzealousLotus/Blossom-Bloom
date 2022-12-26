'''Windows in Tkinter'''
from tkinter import Tk, PhotoImage

# Widgets are elements such as: buttons, textboxes, labels, and images
# Windows serve as containers for Widgets

root = Tk()  # instantiate an instance of a window
root.geometry('420x420')  # Define the dimensions of our window
root.title('My first GUI in Python!')  # The title of our window

# We can change the icon, but first, we must define our image as PhotoImage
icon = PhotoImage(file='~/Programming/Python/Examples/GUI/logo.png')
root.iconphoto(True, icon)  # Now, we call the modified image
root.config(background='black')  # Changes background color, can be hex

root.mainloop()  # Place window on screen, and listen for events
