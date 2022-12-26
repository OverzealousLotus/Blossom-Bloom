'''Buttons in Tkinter'''
from tkinter import Tk, PhotoImage, Button

root = Tk()


def click():
    """When clicked, prints."""
    print('**GGLURG~~ SLLURRP~ MMMFH!~')


head = PhotoImage(file='~/Pictures/Saved_Images/NSFW/you.png')

switch = Button(  # Button creation
    root,
    text='Make her go faster!!!~',
    font=('Arial', 11, 'bold'),
    fg='purple',
    bg='black',
    activeforeground='pink',  # When button is hovered over, or pressed
    activebackground='purple',
    image=head,
    compound='top',
    command=click)  # A command to do when button is pressed
switch.pack()

root.mainloop()
# 0:24:04
