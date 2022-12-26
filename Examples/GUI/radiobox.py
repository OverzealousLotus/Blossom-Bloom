'''Radioboxes in Tkinter'''
from tkinter import Tk, Radiobutton, IntVar, PhotoImage

backgrounds = ['Sinister', 'Aerial', 'Inferno']

root = Tk()

sinister = PhotoImage(file='~/Pictures/Saved_Images/')
aerial = PhotoImage(file='~/Pictures/Saved_Images/aeternum3.png')
inferno = PhotoImage(file='~/Pictures/Saved_Images/aeternum.png')

background_images = [sinister, aerial, inferno]

x = IntVar()

for index in range(len(backgrounds)):

    quest_list = Radiobutton(
        root,
        text=backgrounds[index],  # Adds text to our buttons
        variable=x,  # Groups our buttons if they share the same variable
        value=index,  # Assigns each button a different value
        padx=15,
        pady=15,
        font=('Arial', 12, 'bold'),
        image=background_images[index])  # Assigns background image
    quest_list.pack(anchor='w')

root.mainloop()

# 49:56
