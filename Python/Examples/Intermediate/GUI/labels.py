'''Labels in Tkinter'''
from tkinter import Tk, Label, PhotoImage

root = Tk()

lewd = PhotoImage(file='~/Pictures/Saved_Imagesz/NSFW/yes.png')

our_label = Label(
    root,
    text='They are having fun!~',  # Actual text
    font=('Arial', 11, 'bold'),  # Font
    fg='purple',  # Foreground
    bg='black',  # Background
    relief='raised',  # Border type
    bd=10,  # Border perimeter
    padx=20,  # Text distance from border x
    pady=20,  # Text distance from border y
    image=lewd,  # Image
    compound='top')  # Location of image

our_label.pack()  # "Packs" our label
# our_label.place(x=0, y=0)  # Places our label in a set position

root.mainloop()
