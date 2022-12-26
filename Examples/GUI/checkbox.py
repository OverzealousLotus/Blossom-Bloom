'''Checkboxes in Tkinter'''
from tkinter import Tk, Checkbutton, IntVar, PhotoImage


def display():
    if(x.get() == 1):
        print('You have agreed!')
    else:
        print('You do not agree ;-;')


root = Tk()

x = IntVar()  # Custom variables from Tkinter

soulsucker = PhotoImage(file='~/Pictures/Saved_Images/NSFW/dewfojwegjew.png')

check_button = Checkbutton(  # Our checkbox
    root,
    text='I agree to let her have my soul.',
    font=('Arial', 11, 'bold'),
    fg='white',
    bg='black',
    activeforeground='white',
    activebackground='black',
    padx=15,
    pady=15,
    image=soulsucker,
    compound='top',
    variable=x,  # Allows us to modify x with our check
    onvalue=1,  # defines x as 1 if active
    offvalue=0,  # defines x as 0 when inactive
    command=display
)
check_button.pack()

root.mainloop()
